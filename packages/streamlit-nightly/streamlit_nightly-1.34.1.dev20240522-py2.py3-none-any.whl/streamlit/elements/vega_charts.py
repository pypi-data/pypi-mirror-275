# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Collection of chart commands that are rendered via our vega-lite chart component."""

from __future__ import annotations

import hashlib
import json
import re
from contextlib import nullcontext
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Any,
    Final,
    Iterable,
    Literal,
    Sequence,
    TypedDict,
    cast,
    overload,
)

from typing_extensions import TypeAlias

import streamlit.elements.lib.dicttools as dicttools
from streamlit import type_util
from streamlit.elements.lib.built_in_chart_utils import (
    AddRowsMetadata,
    ChartType,
    generate_chart,
)
from streamlit.elements.lib.event_utils import AttributeDictionary
from streamlit.errors import StreamlitAPIException
from streamlit.proto.ArrowVegaLiteChart_pb2 import (
    ArrowVegaLiteChart as ArrowVegaLiteChartProto,
)
from streamlit.runtime.metrics_util import gather_metrics
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.runtime.state import register_widget
from streamlit.runtime.state.common import compute_widget_id
from streamlit.type_util import Key, to_key
from streamlit.util import HASHLIB_KWARGS

if TYPE_CHECKING:
    import altair as alt

    from streamlit.color_util import Color
    from streamlit.delta_generator import DeltaGenerator
    from streamlit.elements.arrow import Data
    from streamlit.runtime.state import WidgetCallback

# See https://vega.github.io/vega-lite/docs/encoding.html
_CHANNELS: Final = {
    "x",
    "y",
    "x2",
    "y2",
    "xError",
    "xError2",
    "yError",
    "yError2",
    "longitude",
    "latitude",
    "color",
    "opacity",
    "fillOpacity",
    "strokeOpacity",
    "strokeWidth",
    "size",
    "shape",
    "text",
    "tooltip",
    "href",
    "key",
    "order",
    "detail",
    "facet",
    "row",
    "column",
}

VegaLiteSpec: TypeAlias = "dict[str, Any]"


class VegaLiteState(TypedDict, total=False):
    """
    A dictionary representing the current selection state of the VegaLite chart.
    Attributes
    ----------
    selection : AttributeDictionary
        The state of the `on_select` event.
    """

    selection: AttributeDictionary


@dataclass
class VegaLiteStateSerde:
    """VegaLiteStateSerde is used to serialize and deserialize the VegaLite Chart state."""

    selection_parameters: Sequence[str]

    def deserialize(self, ui_value: str | None, widget_id: str = "") -> VegaLiteState:
        empty_selection_state: VegaLiteState = {
            "selection": AttributeDictionary(
                # Initialize the select state with empty dictionaries for each selection parameter.
                {param: {} for param in self.selection_parameters}
            ),
        }

        selection_state = (
            empty_selection_state
            if ui_value is None
            else cast(VegaLiteState, AttributeDictionary(json.loads(ui_value)))
        )

        if "selection" not in selection_state:
            selection_state = empty_selection_state

        return cast(VegaLiteState, AttributeDictionary(selection_state))

    def serialize(self, selection_state: VegaLiteState) -> str:
        return json.dumps(selection_state, default=str)


def _prepare_vega_lite_spec(
    spec: VegaLiteSpec,
    use_container_width: bool = False,
    **kwargs,
) -> VegaLiteSpec:
    if len(kwargs):
        # Support passing in kwargs. Example:
        #   marshall(proto, {foo: 'bar'}, baz='boz')
        # Merge spec with unflattened kwargs, where kwargs take precedence.
        # This only works for string keys, but kwarg keys are strings anyways.
        spec = dict(spec, **dicttools.unflatten(kwargs, _CHANNELS))
    else:
        # Clone the spec dict, since we may be mutating it.
        spec = dict(spec)

    if len(spec) == 0:
        raise StreamlitAPIException("Vega-Lite charts require a non-empty spec dict.")

    if "autosize" not in spec:
        # type fit does not work for many chart types. This change focuses
        # on vconcat with use_container_width=True as there are unintended
        # consequences of changing the default autosize for all charts.
        # fit-x fits the width and height can be adjusted.
        if "vconcat" in spec and use_container_width:
            spec["autosize"] = {"type": "fit-x", "contains": "padding"}
        else:
            spec["autosize"] = {"type": "fit", "contains": "padding"}

    return spec


def _serialize_data(data: Any) -> bytes:
    """Serialize the any type of data structure to Arrow IPC format (bytes)."""
    import pyarrow as pa

    if isinstance(data, pa.Table):
        return type_util.pyarrow_table_to_bytes(data)

    df = type_util.convert_anything_to_df(data)
    return type_util.data_frame_to_bytes(df)


def _marshall_chart_data(
    proto: ArrowVegaLiteChartProto,
    spec: VegaLiteSpec,
    data: Data = None,
) -> None:
    """Adds the data to the proto and removes it from the spec dict.
    These operations will happen in-place."""

    # Pull data out of spec dict when it's in a 'datasets' key:
    #   datasets: {foo: df1_bytes, bar: df2_bytes}, ...}
    if "datasets" in spec:
        for dataset_name, dataset_data in spec["datasets"].items():
            dataset = proto.datasets.add()
            dataset.name = str(dataset_name)
            dataset.has_name = True
            # The ID transformer (id_transform function registered before conversion to dict)
            # already serializes the data into Arrow IPC format (bytes) when the Altair object
            # gets converted into the vega-lite spec dict.
            # If its already in bytes, we don't need to serialize it here again.
            # We just need to pass the data information into the correct proto fields.

            # TODO(lukasmasuch): Are there any other cases where we need to serialize the data
            #                    or can we remove the _serialize_data here?
            dataset.data.data = (
                dataset_data
                if isinstance(dataset_data, bytes)
                else _serialize_data(dataset_data)
            )
        del spec["datasets"]

    # Pull data out of spec dict when it's in a top-level 'data' key:
    #   {data: df}
    #   {data: {values: df, ...}}
    #   {data: {url: 'url'}}
    #   {data: {name: 'foo'}}
    if "data" in spec:
        data_spec = spec["data"]

        if isinstance(data_spec, dict):
            if "values" in data_spec:
                data = data_spec["values"]
                del spec["data"]
        else:
            data = data_spec
            del spec["data"]

    if data is not None:
        proto.data.data = _serialize_data(data)


def _convert_altair_to_vega_lite_spec(altair_chart: alt.Chart) -> VegaLiteSpec:
    """Convert an Altair chart object to a Vega-Lite chart spec."""
    import altair as alt

    # Normally altair_chart.to_dict() would transform the dataframe used by the
    # chart into an array of dictionaries. To avoid that, we install a
    # transformer that replaces datasets with a reference by the object id of
    # the dataframe. We then fill in the dataset manually later on.

    datasets = {}

    def id_transform(data) -> dict[str, str]:
        """Altair data transformer that serializes the data,
        creates a stable name based on the hash of the data,
        stores the bytes into the datasets mapping and
        returns this name to have it be used in Altair.
        """
        # Already serialize the data to be able to create a stable
        # dataset name:
        data_bytes = _serialize_data(data)
        # Use the md5 hash of the data as the name:
        h = hashlib.new("md5", **HASHLIB_KWARGS)
        h.update(str(data_bytes).encode("utf-8"))
        name = h.hexdigest()

        datasets[name] = data_bytes
        return {"name": name}

    alt.data_transformers.register("id", id_transform)  # type: ignore[attr-defined,unused-ignore]

    # The default altair theme has some width/height defaults defined
    # which are not useful for Streamlit. Therefore, we change the theme to
    # "none" to avoid those defaults.
    with alt.themes.enable("none") if alt.themes.active == "default" else nullcontext():  # type: ignore[attr-defined,unused-ignore]
        with alt.data_transformers.enable("id"):  # type: ignore[attr-defined,unused-ignore]
            chart_dict = altair_chart.to_dict()

    # Put datasets back into the chart dict:
    chart_dict["datasets"] = datasets
    return chart_dict


def _disallow_multi_view_charts(spec: VegaLiteSpec) -> None:
    """Raise an exception if the spec contains a multi-view chart (view composition).

    This is intended to be used as a temporary solution to prevent selections on
    multi-view charts. There are too many edge cases to handle selections on these
    charts correctly, so we're disallowing them for now.

    More information about view compositions: https://vega.github.io/vega-lite/docs/composition.html
    """

    if (
        any(key in spec for key in ["layer", "hconcat", "vconcat", "concat", "spec"])
        or "encoding" not in spec
    ):
        raise StreamlitAPIException(
            "Selections are not yet supported for multi-view charts (chart compositions). "
            "If you would like to use selections on multi-view charts, please upvote "
            "this [Github issue](https://github.com/streamlit/streamlit/issues/8643)."
        )


def _extract_selection_parameters(spec: VegaLiteSpec) -> set[str]:
    """Extract the names of all valid selection parameters from the spec."""
    if not spec or "params" not in spec:
        return set()

    param_names = set()

    for param in spec["params"]:
        # Check if it looks like a valid selection parameter:
        # https://vega.github.io/vega-lite/docs/selection.html
        if param.get("name") and param.get("select"):
            # Selection found, just return here to not show the exception.
            param_names.add(param["name"])

    return param_names


def _parse_selection_mode(
    spec: VegaLiteSpec,
    selection_mode: str | Iterable[str] | None,
) -> list[str]:
    """Parse and check the user provided selection modes.

    This will raise an exception if no valid selection parameters are found in the spec
    or if the user provided selection modes are not defined in the spec.

    Parameters
    ----------
    spec : VegaLiteSpec
        The Vega-Lite chart specification.

    selection_mode : str, Iterable[str], or None
        The user provided selection mode(s).

    Returns
    -------
    list[str]
        The parsed selection mode(s) that should be activated.
    """

    # Extract all selection parameters from the spec:
    all_selection_params = _extract_selection_parameters(spec)

    if not all_selection_params:
        raise StreamlitAPIException(
            "Selections are activated, but the provided chart spec does not "
            "have any selections defined. To add selections to `st.altair_chart`, check out the documentation "
            "[here](https://altair-viz.github.io/user_guide/interactions.html#selections-capturing-chart-interactions). "
            "For adding selections to `st.vega_lite_chart`, take a look "
            "at the specification [here](https://vega.github.io/vega-lite/docs/selection.html)."
        )

    if selection_mode is None:
        # Activate all selection parameters:
        return sorted(list(all_selection_params))

    if isinstance(selection_mode, str):
        # Convert single string to list:
        selection_mode = [selection_mode]

    # Check that all provided selection parameters are defined in the spec:
    for selection_name in selection_mode:
        if selection_name not in all_selection_params:
            raise StreamlitAPIException(
                f"Selection parameter '{selection_name}' is not defined in the chart spec. "
                f"Available selection parameters are: {all_selection_params}."
            )
    return sorted(list(selection_mode))


def _reset_counter_pattern(prefix: str, vega_spec: str) -> str:
    """Altair uses a global counter for unnamed parameters and views.
    We need to reset these counters on a spec-level to make the
    spec stable across reruns and avoid changes to the element ID.
    """
    pattern = re.compile(rf'"{prefix}\d+"')
    # Get all matches without duplicates in order of appearance.
    # Using a set here would not guarantee the order of appearance,
    # which might lead to different replacements on each run.
    # The order of the spec from Altair is expected to stay stable
    # within the same session / Altair version.
    # The order might change with Altair updates, but that's not really
    # a case that is relevant for us since we mainly care about having
    # this stable within a session.
    if matches := list(dict.fromkeys(pattern.findall(vega_spec))):
        # Add a prefix to the replacement to avoid
        # replacing instances that already have been replaced before.
        # The prefix here is arbitrarily chosen with the main goal
        # that its extremely unlikely to already be part of the spec:
        replacement_prefix = "__replace_prefix_o9hd101n22e1__"

        # Replace all matches with a counter starting from 1
        # We start from 1 to imitate the altair behavior.
        for counter, match in enumerate(matches, start=1):
            vega_spec = vega_spec.replace(
                match, f'"{replacement_prefix}{prefix}{counter}"'
            )

        # Remove the prefix again from all replacements:
        vega_spec = vega_spec.replace(replacement_prefix, "")
    return vega_spec


def _stabilize_vega_json_spec(vega_spec: str) -> str:
    """Makes the chart spec stay stable across reruns and sessions.

    Altair auto creates names for unnamed parameters & views. It uses a global counter
    for the naming which will result in a different spec on every rerun.
    In Streamlit, we need the spec to be stable across reruns and sessions to prevent the chart
    from getting a new identity. So we need to replace the names with counter with a stable name.
    Having a stable chart spec is also important for features like forward message cache,
    where we don't want to have changing messages on every rerun.

    Parameter counter:
    https://github.com/vega/altair/blob/f345cd9368ae2bbc98628e9245c93fa9fb582621/altair/vegalite/v5/api.py#L196

    View counter:
    https://github.com/vega/altair/blob/f345cd9368ae2bbc98628e9245c93fa9fb582621/altair/vegalite/v5/api.py#L2885

    This is temporary solution waiting for a fix for this issue:
    https://github.com/vega/altair/issues/3416

    Other solutions we considered:
     - working on the dict object: this would require to iterate through the object and do the
       same kind of replacement; though we would need to know the structure and since we need
       the spec in String-format anyways, we deemed that executing the replacement on the
       String is the better alternative
     - resetting the counter: the counter is incremented already when the chart object is created
       (see this GitHub issue comment https://github.com/vega/altair/issues/3416#issuecomment-2098530464),
       so it would be too late here to reset the counter with a thread-lock to prevent interference
       between sessions
    """

    # We only want to apply these replacements if it is really necessary
    # since there is a risk that we replace names that where chosen by the user
    # and thereby introduce unwanted side effects.

    # We only need to apply the param_ fix if there are actually parameters defined
    # somewhere in the spec. We can check for this by looking for the '"params"' key.
    # This isn't a perfect check, but good enough to prevent unnecessary executions
    # for the majority of charts.
    if '"params"' in vega_spec:
        vega_spec = _reset_counter_pattern("param_", vega_spec)

    # Simple check if the spec contains a composite chart:
    # https://vega.github.io/vega-lite/docs/composition.html
    # Other charts will not contain the `view_` name,
    # so its better to not replace this pattern.
    if re.search(r'"(vconcat|hconcat|facet|layer|concat|repeat)"', vega_spec):
        vega_spec = _reset_counter_pattern("view_", vega_spec)
    return vega_spec


class VegaChartsMixin:
    """Mix-in class for all vega-related chart commands.

    Altair is a python wrapper on top of the vega-lite spec. And our
    built-in chart commands are just another layer on-top of Altair.
    All of these chart commands will be eventually converted to a vega-lite
    spec and rendered using the same vega-lite chart component.
    """

    @gather_metrics("line_chart")
    def line_chart(
        self,
        data: Data = None,
        *,
        x: str | None = None,
        y: str | Sequence[str] | None = None,
        color: str | Color | list[Color] | None = None,
        width: int = 0,
        height: int = 0,
        use_container_width: bool = True,
    ) -> DeltaGenerator:
        """Display a line chart.

        This is syntax-sugar around ``st.altair_chart``. The main difference
        is this command uses the data's own column and indices to figure out
        the chart's spec. As a result this is easier to use for many "just plot
        this" scenarios, while being less customizable.

        If ``st.line_chart`` does not guess the data specification
        correctly, try specifying your desired chart using ``st.altair_chart``.

        Parameters
        ----------
        data : pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, snowflake.snowpark.table.Table, Iterable, dict or None
            Data to be plotted.

        x : str or None
            Column name to use for the x-axis. If None, uses the data index for the x-axis.

        y : str, Sequence of str, or None
            Column name(s) to use for the y-axis. If a Sequence of strings,
            draws several series on the same chart by melting your wide-format
            table into a long-format table behind the scenes. If None, draws
            the data of all remaining columns as data series.

        color : str, tuple, Sequence of str, Sequence of tuple, or None
            The color to use for different lines in this chart.

            For a line chart with just one line, this can be:

            * None, to use the default color.
            * A hex string like "#ffaa00" or "#ffaa0088".
            * An RGB or RGBA tuple with the red, green, blue, and alpha
              components specified as ints from 0 to 255 or floats from 0.0 to
              1.0.

            For a line chart with multiple lines, where the dataframe is in
            long format (that is, y is None or just one column), this can be:

            * None, to use the default colors.
            * The name of a column in the dataset. Data points will be grouped
              into lines of the same color based on the value of this column.
              In addition, if the values in this column match one of the color
              formats above (hex string or color tuple), then that color will
              be used.

              For example: if the dataset has 1000 rows, but this column only
              contains the values "adult", "child", and "baby", then those 1000
              datapoints will be grouped into three lines whose colors will be
              automatically selected from the default palette.

              But, if for the same 1000-row dataset, this column contained
              the values "#ffaa00", "#f0f", "#0000ff", then then those 1000
              datapoints would still be grouped into three lines, but their
              colors would be "#ffaa00", "#f0f", "#0000ff" this time around.

            For a line chart with multiple lines, where the dataframe is in
            wide format (that is, y is a Sequence of columns), this can be:

            * None, to use the default colors.
            * A list of string colors or color tuples to be used for each of
              the lines in the chart. This list should have the same length
              as the number of y values (e.g. ``color=["#fd0", "#f0f", "#04f"]``
              for three lines).

        width : int
            The chart width in pixels. If 0, selects the width automatically.

        height : int
            The chart height in pixels. If 0, selects the height automatically.

        use_container_width : bool
            If True, set the chart width to the column width. This takes
            precedence over the width argument.

        Examples
        --------
        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        >>>
        >>> st.line_chart(chart_data)

        .. output::
           https://doc-line-chart.streamlit.app/
           height: 440px

        You can also choose different columns to use for x and y, as well as set
        the color dynamically based on a 3rd column (assuming your dataframe is in
        long format):

        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(
        ...    {
        ...        "col1": np.random.randn(20),
        ...        "col2": np.random.randn(20),
        ...        "col3": np.random.choice(["A", "B", "C"], 20),
        ...    }
        ... )
        >>>
        >>> st.line_chart(chart_data, x="col1", y="col2", color="col3")

        .. output::
           https://doc-line-chart1.streamlit.app/
           height: 440px

        Finally, if your dataframe is in wide format, you can group multiple
        columns under the y argument to show multiple lines with different
        colors:

        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
        >>>
        >>> st.line_chart(
        ...    chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
        ... )

        .. output::
           https://doc-line-chart2.streamlit.app/
           height: 440px

        """

        chart, add_rows_metadata = generate_chart(
            chart_type=ChartType.LINE,
            data=data,
            x_from_user=x,
            y_from_user=y,
            color_from_user=color,
            size_from_user=None,
            width=width,
            height=height,
        )
        return cast(
            "DeltaGenerator",
            self._altair_chart(
                chart,
                use_container_width=use_container_width,
                theme="streamlit",
                add_rows_metadata=add_rows_metadata,
            ),
        )

    @gather_metrics("area_chart")
    def area_chart(
        self,
        data: Data = None,
        *,
        x: str | None = None,
        y: str | Sequence[str] | None = None,
        color: str | Color | list[Color] | None = None,
        width: int = 0,
        height: int = 0,
        use_container_width: bool = True,
    ) -> DeltaGenerator:
        """Display an area chart.

        This is syntax-sugar around ``st.altair_chart``. The main difference
        is this command uses the data's own column and indices to figure out
        the chart's spec. As a result this is easier to use for many "just plot
        this" scenarios, while being less customizable.

        If ``st.area_chart`` does not guess the data specification
        correctly, try specifying your desired chart using ``st.altair_chart``.

        Parameters
        ----------
        data : pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, snowflake.snowpark.table.Table, Iterable, or dict
            Data to be plotted.

        x : str or None
            Column name to use for the x-axis. If None, uses the data index for the x-axis.

        y : str, Sequence of str, or None
            Column name(s) to use for the y-axis. If a Sequence of strings,
            draws several series on the same chart by melting your wide-format
            table into a long-format table behind the scenes. If None, draws
            the data of all remaining columns as data series.

        color : str, tuple, Sequence of str, Sequence of tuple, or None
            The color to use for different series in this chart.

            For an area chart with just 1 series, this can be:

            * None, to use the default color.
            * A hex string like "#ffaa00" or "#ffaa0088".
            * An RGB or RGBA tuple with the red, green, blue, and alpha
              components specified as ints from 0 to 255 or floats from 0.0 to
              1.0.

            For an area chart with multiple series, where the dataframe is in
            long format (that is, y is None or just one column), this can be:

            * None, to use the default colors.
            * The name of a column in the dataset. Data points will be grouped
              into series of the same color based on the value of this column.
              In addition, if the values in this column match one of the color
              formats above (hex string or color tuple), then that color will
              be used.

              For example: if the dataset has 1000 rows, but this column only
              contains the values "adult", "child", and "baby", then those 1000
              datapoints will be grouped into three series whose colors will be
              automatically selected from the default palette.

              But, if for the same 1000-row dataset, this column contained
              the values "#ffaa00", "#f0f", "#0000ff", then then those 1000
              datapoints would still be grouped into 3 series, but their
              colors would be "#ffaa00", "#f0f", "#0000ff" this time around.

            For an area chart with multiple series, where the dataframe is in
            wide format (that is, y is a Sequence of columns), this can be:

            * None, to use the default colors.
            * A list of string colors or color tuples to be used for each of
              the series in the chart. This list should have the same length
              as the number of y values (e.g. ``color=["#fd0", "#f0f", "#04f"]``
              for three lines).

        width : int
            The chart width in pixels. If 0, selects the width automatically.

        height : int
            The chart height in pixels. If 0, selects the height automatically.

        use_container_width : bool
            If True, set the chart width to the column width. This takes
            precedence over the width argument.

        Examples
        --------
        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        >>>
        >>> st.area_chart(chart_data)

        .. output::
           https://doc-area-chart.streamlit.app/
           height: 440px

        You can also choose different columns to use for x and y, as well as set
        the color dynamically based on a 3rd column (assuming your dataframe is in
        long format):

        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(
        ...    {
        ...        "col1": np.random.randn(20),
        ...        "col2": np.random.randn(20),
        ...        "col3": np.random.choice(["A", "B", "C"], 20),
        ...    }
        ... )
        >>>
        >>> st.area_chart(chart_data, x="col1", y="col2", color="col3")

        .. output::
           https://doc-area-chart1.streamlit.app/
           height: 440px

        Finally, if your dataframe is in wide format, you can group multiple
        columns under the y argument to show multiple series with different
        colors:

        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
        >>>
        >>> st.area_chart(
        ...    chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
        ... )

        .. output::
           https://doc-area-chart2.streamlit.app/
           height: 440px

        """

        chart, add_rows_metadata = generate_chart(
            chart_type=ChartType.AREA,
            data=data,
            x_from_user=x,
            y_from_user=y,
            color_from_user=color,
            size_from_user=None,
            width=width,
            height=height,
        )
        return cast(
            "DeltaGenerator",
            self._altair_chart(
                chart,
                use_container_width=use_container_width,
                theme="streamlit",
                add_rows_metadata=add_rows_metadata,
            ),
        )

    @gather_metrics("bar_chart")
    def bar_chart(
        self,
        data: Data = None,
        *,
        x: str | None = None,
        y: str | Sequence[str] | None = None,
        color: str | Color | list[Color] | None = None,
        width: int = 0,
        height: int = 0,
        use_container_width: bool = True,
    ) -> DeltaGenerator:
        """Display a bar chart.

        This is syntax-sugar around ``st.altair_chart``. The main difference
        is this command uses the data's own column and indices to figure out
        the chart's spec. As a result this is easier to use for many "just plot
        this" scenarios, while being less customizable.

        If ``st.bar_chart`` does not guess the data specification
        correctly, try specifying your desired chart using ``st.altair_chart``.

        Parameters
        ----------
        data : pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, snowflake.snowpark.table.Table, Iterable, or dict
            Data to be plotted.

        x : str or None
            Column name to use for the x-axis. If None, uses the data index for the x-axis.

        y : str, Sequence of str, or None
            Column name(s) to use for the y-axis. If a Sequence of strings,
            draws several series on the same chart by melting your wide-format
            table into a long-format table behind the scenes. If None, draws
            the data of all remaining columns as data series.

        color : str, tuple, Sequence of str, Sequence of tuple, or None
            The color to use for different series in this chart.

            For a bar chart with just one series, this can be:

            * None, to use the default color.
            * A hex string like "#ffaa00" or "#ffaa0088".
            * An RGB or RGBA tuple with the red, green, blue, and alpha
              components specified as ints from 0 to 255 or floats from 0.0 to
              1.0.

            For a bar chart with multiple series, where the dataframe is in
            long format (that is, y is None or just one column), this can be:

            * None, to use the default colors.
            * The name of a column in the dataset. Data points will be grouped
              into series of the same color based on the value of this column.
              In addition, if the values in this column match one of the color
              formats above (hex string or color tuple), then that color will
              be used.

              For example: if the dataset has 1000 rows, but this column only
              contains the values "adult", "child", and "baby", then those 1000
              datapoints will be grouped into three series whose colors will be
              automatically selected from the default palette.

              But, if for the same 1000-row dataset, this column contained
              the values "#ffaa00", "#f0f", "#0000ff", then then those 1000
              datapoints would still be grouped into 3 series, but their
              colors would be "#ffaa00", "#f0f", "#0000ff" this time around.

            For a bar chart with multiple series, where the dataframe is in
            wide format (that is, y is a Sequence of columns), this can be:

            * None, to use the default colors.
            * A list of string colors or color tuples to be used for each of
              the series in the chart. This list should have the same length
              as the number of y values (e.g. ``color=["#fd0", "#f0f", "#04f"]``
              for three lines).

        width : int
            The chart width in pixels. If 0, selects the width automatically.

        height : int
            The chart height in pixels. If 0, selects the height automatically.

        use_container_width : bool
            If True, set the chart width to the column width. This takes
            precedence over the width argument.

        Examples
        --------
        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        >>>
        >>> st.bar_chart(chart_data)

        .. output::
           https://doc-bar-chart.streamlit.app/
           height: 440px

        You can also choose different columns to use for x and y, as well as set
        the color dynamically based on a 3rd column (assuming your dataframe is in
        long format):

        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(
        ...    {
        ...        "col1": list(range(20)) * 3,
        ...        "col2": np.random.randn(60),
        ...        "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
        ...    }
        ... )
        >>>
        >>> st.bar_chart(chart_data, x="col1", y="col2", color="col3")

        .. output::
           https://doc-bar-chart1.streamlit.app/
           height: 440px

        Finally, if your dataframe is in wide format, you can group multiple
        columns under the y argument to show multiple series with different
        colors:

        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(
        ...    {"col1": list(range(20)), "col2": np.random.randn(20), "col3": np.random.randn(20)}
        ... )
        >>>
        >>> st.bar_chart(
        ...    chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
        ... )

        .. output::
           https://doc-bar-chart2.streamlit.app/
           height: 440px

        """

        chart, add_rows_metadata = generate_chart(
            chart_type=ChartType.BAR,
            data=data,
            x_from_user=x,
            y_from_user=y,
            color_from_user=color,
            size_from_user=None,
            width=width,
            height=height,
        )
        return cast(
            "DeltaGenerator",
            self._altair_chart(
                chart,
                use_container_width=use_container_width,
                theme="streamlit",
                add_rows_metadata=add_rows_metadata,
            ),
        )

    @gather_metrics("scatter_chart")
    def scatter_chart(
        self,
        data: Data = None,
        *,
        x: str | None = None,
        y: str | Sequence[str] | None = None,
        color: str | Color | list[Color] | None = None,
        size: str | float | int | None = None,
        width: int = 0,
        height: int = 0,
        use_container_width: bool = True,
    ) -> DeltaGenerator:
        """Display a scatterplot chart.

        This is syntax-sugar around ``st.altair_chart``. The main difference
        is this command uses the data's own column and indices to figure out
        the chart's spec. As a result this is easier to use for many "just plot
        this" scenarios, while being less customizable.

        If ``st.scatter_chart`` does not guess the data specification correctly,
        try specifying your desired chart using ``st.altair_chart``.

        Parameters
        ----------
        data : pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, snowflake.snowpark.table.Table, Iterable, dict or None
            Data to be plotted.

        x : str or None
            Column name to use for the x-axis. If None, uses the data index for the x-axis.

        y : str, Sequence of str, or None
            Column name(s) to use for the y-axis. If a Sequence of strings,
            draws several series on the same chart by melting your wide-format
            table into a long-format table behind the scenes. If None, draws
            the data of all remaining columns as data series.

        color : str, tuple, Sequence of str, Sequence of tuple, or None
            The color of the circles representing each datapoint.

            This can be:

            * None, to use the default color.
            * A hex string like "#ffaa00" or "#ffaa0088".
            * An RGB or RGBA tuple with the red, green, blue, and alpha
              components specified as ints from 0 to 255 or floats from 0.0 to
              1.0.
            * The name of a column in the dataset where the color of that
              datapoint will come from.

              If the values in this column are in one of the color formats
              above (hex string or color tuple), then that color will be used.

              Otherwise, the color will be automatically picked from the
              default palette.

              For example: if the dataset has 1000 rows, but this column only
              contains the values "adult", "child", and "baby", then those 1000
              datapoints be shown using three colors from the default palette.

              But if this column only contains floats or ints, then those
              1000 datapoints will be shown using a colors from a continuous
              color gradient.

              Finally, if this column only contains the values "#ffaa00",
              "#f0f", "#0000ff", then then each of those 1000 datapoints will
              be assigned "#ffaa00", "#f0f", or "#0000ff" as appropriate.

            If the dataframe is in wide format (that is, y is a Sequence of
            columns), this can also be:

            * A list of string colors or color tuples to be used for each of
              the series in the chart. This list should have the same length
              as the number of y values (e.g. ``color=["#fd0", "#f0f", "#04f"]``
              for three series).

        size : str, float, int, or None
            The size of the circles representing each point.

            This can be:

            * A number like 100, to specify a single size to use for all
              datapoints.
            * The name of the column to use for the size. This allows each
              datapoint to be represented by a circle of a different size.

        width : int
            The chart width in pixels. If 0, selects the width automatically.

        height : int
            The chart height in pixels. If 0, selects the height automatically.

        use_container_width : bool
            If True, set the chart width to the column width. This takes
            precedence over the width argument.

        Examples
        --------
        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        >>>
        >>> st.scatter_chart(chart_data)

        .. output::
           https://doc-scatter-chart.streamlit.app/
           height: 440px

        You can also choose different columns to use for x and y, as well as set
        the color dynamically based on a 3rd column (assuming your dataframe is in
        long format):

        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
        >>> chart_data['col4'] = np.random.choice(['A','B','C'], 20)
        >>>
        >>> st.scatter_chart(
        ...     chart_data,
        ...     x='col1',
        ...     y='col2',
        ...     color='col4',
        ...     size='col3',
        ... )

        .. output::
           https://doc-scatter-chart1.streamlit.app/
           height: 440px

        Finally, if your dataframe is in wide format, you can group multiple
        columns under the y argument to show multiple series with different
        colors:

        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(np.random.randn(20, 4), columns=["col1", "col2", "col3", "col4"])
        >>>
        >>> st.scatter_chart(
        ...     chart_data,
        ...     x='col1',
        ...     y=['col2', 'col3'],
        ...     size='col4',
        ...     color=['#FF0000', '#0000FF'],  # Optional
        ... )

        .. output::
           https://doc-scatter-chart2.streamlit.app/
           height: 440px

        """

        chart, add_rows_metadata = generate_chart(
            chart_type=ChartType.SCATTER,
            data=data,
            x_from_user=x,
            y_from_user=y,
            color_from_user=color,
            size_from_user=size,
            width=width,
            height=height,
        )
        return cast(
            "DeltaGenerator",
            self._altair_chart(
                chart,
                use_container_width=use_container_width,
                theme="streamlit",
                add_rows_metadata=add_rows_metadata,
            ),
        )

    @overload
    def altair_chart(
        self,
        altair_chart: alt.Chart,
        *,
        use_container_width: bool = False,
        theme: Literal["streamlit"] | None = "streamlit",
        key: Key | None = None,
        on_select: Literal["ignore"],  # No default value here to make it work with mypy
        selection_mode: str | Iterable[str] | None = None,
    ) -> DeltaGenerator:
        ...

    @overload
    def altair_chart(
        self,
        altair_chart: alt.Chart,
        *,
        use_container_width: bool = False,
        theme: Literal["streamlit"] | None = "streamlit",
        key: Key | None = None,
        on_select: Literal["rerun"] | WidgetCallback = "rerun",
        selection_mode: str | Iterable[str] | None = None,
    ) -> VegaLiteState:
        ...

    @gather_metrics("altair_chart")
    def altair_chart(
        self,
        altair_chart: alt.Chart,
        *,
        use_container_width: bool = False,
        theme: Literal["streamlit"] | None = "streamlit",
        key: Key | None = None,
        on_select: Literal["rerun", "ignore"] | WidgetCallback = "ignore",
        selection_mode: str | Iterable[str] | None = None,
    ) -> DeltaGenerator | VegaLiteState:
        """Display a chart using the Altair library.

        Parameters
        ----------
        altair_chart : altair.Chart
            The Altair chart object to display.

        use_container_width : bool
            If True, set the chart width to the column width. This takes
            precedence over Altair's native ``width`` value.

        theme : "streamlit" or None
            The theme of the chart. Currently, we only support "streamlit" for the Streamlit
            defined design or None to fallback to the default behavior of the library.

        key : str
            An optional string to use as the unique key for this element when used in combination
            with ```on_select```. If this is omitted, a key will be generated for the widget based
            on its content. Multiple widgets of the same type may not share the same key.

        on_select : "ignore" or "rerun" or callable
            Controls the behavior in response to selection events on the charts. Can be one of:
            - "ignore" (default): Streamlit will not react to any selection events in the chart.
            - "rerun: Streamlit will rerun the app when the user selects data in the chart. In this case,
              ```st.altair_chart``` will return the selection data as a dictionary.
            - callable: If a callable is provided, Streamlit will rerun and execute the callable as a
              callback function before the rest of the app. The selection data can be retrieved through
              session state by setting the key parameter.

        Example
        -------

        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>> import altair as alt
        >>>
        >>> chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        >>>
        >>> c = (
        ...    alt.Chart(chart_data)
        ...    .mark_circle()
        ...    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
        ... )
        >>>
        >>> st.altair_chart(c, use_container_width=True)

        .. output::
           https://doc-vega-lite-chart.streamlit.app/
           height: 300px

        Examples of Altair charts can be found at
        https://altair-viz.github.io/gallery/.

        """
        return self._altair_chart(
            altair_chart=altair_chart,
            use_container_width=use_container_width,
            theme=theme,
            key=key,
            on_select=on_select,
            selection_mode=selection_mode,
        )

    @overload
    def vega_lite_chart(
        self,
        data: Data = None,
        spec: VegaLiteSpec | None = None,
        *,
        use_container_width: bool = False,
        theme: Literal["streamlit"] | None = "streamlit",
        key: Key | None = None,
        on_select: Literal["ignore"],  # No default value here to make it work with mypy
        selection_mode: str | Iterable[str] | None = None,
        **kwargs: Any,
    ) -> DeltaGenerator:
        ...

    @overload
    def vega_lite_chart(
        self,
        data: Data = None,
        spec: VegaLiteSpec | None = None,
        *,
        use_container_width: bool = False,
        theme: Literal["streamlit"] | None = "streamlit",
        key: Key | None = None,
        on_select: Literal["rerun"] | WidgetCallback = "rerun",
        selection_mode: str | Iterable[str] | None = None,
        **kwargs: Any,
    ) -> VegaLiteState:
        ...

    @gather_metrics("vega_lite_chart")
    def vega_lite_chart(
        self,
        data: Data = None,
        spec: VegaLiteSpec | None = None,
        *,
        use_container_width: bool = False,
        theme: Literal["streamlit"] | None = "streamlit",
        key: Key | None = None,
        on_select: Literal["rerun", "ignore"] | WidgetCallback = "ignore",
        selection_mode: str | Iterable[str] | None = None,
        **kwargs: Any,
    ) -> DeltaGenerator | VegaLiteState:
        """Display a chart using the Vega-Lite library.

        Parameters
        ----------
        data : pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, Iterable, dict, or None
            Either the data to be plotted or a Vega-Lite spec containing the
            data (which more closely follows the Vega-Lite API).

        spec : dict or None
            The Vega-Lite spec for the chart. If the spec was already passed in
            the previous argument, this must be set to None. See
            https://vega.github.io/vega-lite/docs/ for more info.

        use_container_width : bool
            If True, set the chart width to the column width. This takes
            precedence over Vega-Lite's native `width` value.

        theme : "streamlit" or None
            The theme of the chart. Currently, we only support "streamlit" for the Streamlit
            defined design or None to fallback to the default behavior of the library.

        key : str
            An optional string to use as the unique key for this element when used in combination
            with ```on_select```. If this is omitted, a key will be generated for the widget based
            on its content. Multiple widgets of the same type may not share the same key.

        on_select : "ignore" or "rerun" or callable
            Controls the behavior in response to selection events on the charts. Can be one of:
            - "ignore" (default): Streamlit will not react to any selection events in the chart.
            - "rerun: Streamlit will rerun the app when the user selects data in the chart. In this case,
              ```st.vega_lite_chart``` will return the selection data as a dictionary.
            - callable: If a callable is provided, Streamlit will rerun and execute the callable as a
              callback function before the rest of the app. The selection data can be retrieved through
              session state by setting the key parameter.

        **kwargs : any
            Same as spec, but as keywords.

        Example
        -------
        >>> import streamlit as st
        >>> import pandas as pd
        >>> import numpy as np
        >>>
        >>> chart_data = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
        >>>
        >>> st.vega_lite_chart(
        ...    chart_data,
        ...    {
        ...        "mark": {"type": "circle", "tooltip": True},
        ...        "encoding": {
        ...            "x": {"field": "a", "type": "quantitative"},
        ...            "y": {"field": "b", "type": "quantitative"},
        ...            "size": {"field": "c", "type": "quantitative"},
        ...            "color": {"field": "c", "type": "quantitative"},
        ...        },
        ...    },
        ... )

        .. output::
           https://doc-vega-lite-chart.streamlit.app/
           height: 300px

        Examples of Vega-Lite usage without Streamlit can be found at
        https://vega.github.io/vega-lite/examples/. Most of those can be easily
        translated to the syntax shown above.

        """
        return self._vega_lite_chart(
            data=data,
            spec=spec,
            use_container_width=use_container_width,
            theme=theme,
            key=key,
            on_select=on_select,
            selection_mode=selection_mode,
            **kwargs,
        )

    def _altair_chart(
        self,
        altair_chart: alt.Chart,
        use_container_width: bool = False,
        theme: Literal["streamlit"] | None = "streamlit",
        key: Key | None = None,
        on_select: Literal["rerun", "ignore"] | WidgetCallback = "ignore",
        selection_mode: str | Iterable[str] | None = None,
        add_rows_metadata: AddRowsMetadata | None = None,
    ) -> DeltaGenerator | VegaLiteState:
        """Internal method to enqueue a vega-lite chart element based on an Altair chart.

        See the `altair_chart` method docstring for more information.
        """

        if type_util.is_altair_version_less_than("5.0.0") and on_select != "ignore":
            raise StreamlitAPIException(
                "Streamlit does not support selections with Altair 4.x. Please upgrade to Version 5. "
                "If you would like to use Altair 4.x with selections, please upvote "
                "this [Github issue](https://github.com/streamlit/streamlit/issues/8516)."
            )

        vega_lite_spec = _convert_altair_to_vega_lite_spec(altair_chart)
        return self._vega_lite_chart(
            data=None,  # The data is already part of the spec
            spec=vega_lite_spec,
            use_container_width=use_container_width,
            theme=theme,
            key=key,
            on_select=on_select,
            selection_mode=selection_mode,
            add_rows_metadata=add_rows_metadata,
        )

    def _vega_lite_chart(
        self,
        data: Data = None,
        spec: VegaLiteSpec | None = None,
        use_container_width: bool = False,
        theme: Literal["streamlit"] | None = "streamlit",
        key: Key | None = None,
        on_select: Literal["rerun", "ignore"] | WidgetCallback = "ignore",
        selection_mode: str | Iterable[str] | None = None,
        add_rows_metadata: AddRowsMetadata | None = None,
        **kwargs: Any,
    ) -> DeltaGenerator | VegaLiteState:
        """Internal method to enqueue a vega-lite chart element based on a vega-lite spec.

        See the `vega_lite_chart` method docstring for more information.
        """

        if theme not in ["streamlit", None]:
            raise StreamlitAPIException(
                f'You set theme="{theme}" while Streamlit charts only support theme=”streamlit” or theme=None to fallback to the default library theme.'
            )

        if on_select not in ["ignore", "rerun"] and not callable(on_select):
            raise StreamlitAPIException(
                f"You have passed {on_select} to `on_select`. But only 'ignore', 'rerun', or a callable is supported."
            )

        key = to_key(key)
        is_selection_activated = on_select != "ignore"

        if is_selection_activated:
            # Run some checks that are only relevant when selections are activated

            # Import here to avoid circular imports
            from streamlit.elements.utils import (
                check_cache_replay_rules,
                check_callback_rules,
                check_session_state_rules,
            )

            check_cache_replay_rules()
            if callable(on_select):
                check_callback_rules(self.dg, on_select)
            check_session_state_rules(default_value=None, key=key, writes_allowed=False)

        # Support passing data inside spec['datasets'] and spec['data'].
        # (The data gets pulled out of the spec dict later on.)
        if isinstance(data, dict) and spec is None:
            spec = data
            data = None

        if spec is None:
            spec = {}

        vega_lite_proto = ArrowVegaLiteChartProto()

        spec = _prepare_vega_lite_spec(spec, use_container_width, **kwargs)
        _marshall_chart_data(vega_lite_proto, spec, data)

        # Prevent the spec from changing across reruns:
        vega_lite_proto.spec = _stabilize_vega_json_spec(json.dumps(spec))
        vega_lite_proto.use_container_width = use_container_width
        vega_lite_proto.theme = theme or ""

        if is_selection_activated:
            # Import here to avoid circular imports
            from streamlit.elements.form import current_form_id

            # Load the stabilized spec again as a dict:
            final_spec = json.loads(vega_lite_proto.spec)
            # Temporary limitation to disallow multi-view charts (compositions) with selections.
            _disallow_multi_view_charts(final_spec)

            # Parse and check the specified selection modes
            parsed_selection_modes = _parse_selection_mode(final_spec, selection_mode)
            vega_lite_proto.selection_mode.extend(parsed_selection_modes)

            vega_lite_proto.form_id = current_form_id(self.dg)

            ctx = get_script_run_ctx()
            vega_lite_proto.id = compute_widget_id(
                "arrow_vega_lite_chart",
                user_key=key,
                key=key,
                vega_lite_spec=vega_lite_proto.spec,
                # The data is either in vega_lite_proto.data.data
                # or in a named dataset in vega_lite_proto.datasets
                vega_lite_data=vega_lite_proto.data.data,
                # Its enough to just use the names here since they are expected
                # to contain hashes based on the dataset data.
                named_datasets=[dataset.name for dataset in vega_lite_proto.datasets],
                theme=theme,
                use_container_width=use_container_width,
                selection_mode=parsed_selection_modes,
                form_id=vega_lite_proto.form_id,
                page=ctx.page_script_hash if ctx else None,
            )

            serde = VegaLiteStateSerde(parsed_selection_modes)

            widget_state = register_widget(
                "vega_lite_chart",
                vega_lite_proto,
                user_key=key,
                on_change_handler=on_select if callable(on_select) else None,
                deserializer=serde.deserialize,
                serializer=serde.serialize,
                ctx=ctx,
            )

            self.dg._enqueue(
                "arrow_vega_lite_chart",
                vega_lite_proto,
                add_rows_metadata=add_rows_metadata,
            )
            return cast(VegaLiteState, widget_state.value)
        # If its not used with selections activated, just return
        # the delta generator related to this element.
        return self.dg._enqueue(
            "arrow_vega_lite_chart",
            vega_lite_proto,
            add_rows_metadata=add_rows_metadata,
        )

    @property
    def dg(self) -> DeltaGenerator:
        """Get our DeltaGenerator."""
        return cast("DeltaGenerator", self)
