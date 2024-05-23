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

"""Streamlit version utilities."""

from __future__ import annotations

import random
from importlib.metadata import version as _version
from typing import TYPE_CHECKING, Final

import streamlit.logger as logger

if TYPE_CHECKING:
    from packaging.version import Version


_LOGGER: Final = logger.get_logger(__name__)

PYPI_STREAMLIT_URL = "https://pypi.org/pypi/streamlit/json"

# Probability that we'll make a network call to PyPI to check
# the latest version of streamlit. This is used each time
# should_show_new_version_notice() is called.
CHECK_PYPI_PROBABILITY = 0.10

STREAMLIT_VERSION_STRING: Final[str] = _version("streamlit-nightly")


def _version_str_to_obj(version_str: str) -> Version:
    from packaging.version import Version

    return Version(version_str)


def _get_installed_streamlit_version() -> Version:
    """Return the streamlit version string from setup.py.

    Returns
    -------
    str
        The version string specified in setup.py.

    """
    return _version_str_to_obj(STREAMLIT_VERSION_STRING)


def _get_latest_streamlit_version(timeout: float | None = None) -> Version:
    """Request the latest streamlit version string from PyPI.

    NB: this involves a network call, so it could raise an error
    or take a long time.

    Parameters
    ----------
    timeout : float or None
        The request timeout.

    Returns
    -------
    str
        The version string for the latest version of streamlit
        on PyPI.

    """
    import requests

    rsp = requests.get(PYPI_STREAMLIT_URL, timeout=timeout)
    try:
        version_str = rsp.json()["info"]["version"]
    except Exception as e:
        raise RuntimeError("Got unexpected response from PyPI", e)
    return _version_str_to_obj(version_str)


def should_show_new_version_notice() -> bool:
    """True if streamlit should show a 'new version!' notice to the user.

    We need to make a network call to PyPI to determine the latest streamlit
    version. Since we don't want to do this every time streamlit is run,
    we'll only perform the check ~5% of the time.

    If we do make the request to PyPI and there's any sort of error,
    we log it and return False.

    Returns
    -------
    bool
        True if we should tell the user that their streamlit is out of date.

    """
    if random.random() >= CHECK_PYPI_PROBABILITY:
        # We don't check PyPI every time this function is called.
        _LOGGER.debug("Skipping PyPI version check")
        return False

    try:
        installed_version = _get_installed_streamlit_version()
        latest_version = _get_latest_streamlit_version(timeout=1)
    except Exception as ex:
        # Log this as a debug. We don't care if the user sees it.
        _LOGGER.debug("Failed PyPI version check.", exc_info=ex)
        return False

    return latest_version > installed_version
