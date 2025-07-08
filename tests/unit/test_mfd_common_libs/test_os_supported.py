# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT

import pytest
import sys
from mfd_typing import OSName

from mfd_common_libs import os_supported
from mfd_common_libs.exceptions import UnexpectedOSException, OSSupportedDecoratorError


class TestOSSupportedDecorator:
    @pytest.fixture()
    def mocked_connection(self, mocker):
        sys.modules["mfd_connect"] = mocker.MagicMock()
        mocker.patch("mfd_common_libs.os_supported_decorator.isinstance", return_value=True)
        return mocker.Mock()

    def test_supported(self, mocked_connection, mocker):
        class Module:
            @os_supported(OSName.WINDOWS)
            def __init__(self, *, conn):
                self._conn = conn

        mocked_connection.get_os_name.return_value = OSName.WINDOWS
        Module(conn=mocked_connection)

    def test_unsupported(self, mocked_connection):
        class Module:
            @os_supported(OSName.LINUX)
            def __init__(self, *, connection):
                self._conn = connection

        mocked_connection.get_os_name.return_value = OSName.WINDOWS
        with pytest.raises(UnexpectedOSException):
            Module(connection=mocked_connection)

    def test_supported_list(self, mocked_connection):
        class Module:
            @os_supported(OSName.LINUX, OSName.WINDOWS)
            def __init__(self, *, connection):
                self._conn = connection

        mocked_connection.get_os_name.return_value = OSName.WINDOWS
        Module(connection=mocked_connection)

    def test_unsupported_list(self, mocked_connection):
        class Module:
            @os_supported(OSName.LINUX, OSName.WINDOWS)
            def __init__(self, *, connection):
                self._conn = connection

        mocked_connection.get_os_name.return_value = OSName.FREEBSD
        with pytest.raises(UnexpectedOSException):
            Module(connection=mocked_connection)

    def test_missing_connection(self, mocker):
        sys.modules["mfd_connect"] = mocker.MagicMock()
        mocker.patch("mfd_common_libs.os_supported_decorator.isinstance", return_value=False)

        class Module:
            @os_supported(OSName.LINUX, OSName.WINDOWS)
            def __init__(self, *, ip):
                self._ip = ip

        with pytest.raises(OSSupportedDecoratorError):
            Module(ip="10.10.10.10")
