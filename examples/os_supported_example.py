# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT
from mfd_connect import SSHConnection
from mfd_typing import OSName

from mfd_common_libs import os_supported


class MyModule:
    def __init__(self, *, connection):
        self._conn = connection


class MyModuleWithInherit(MyModule):
    __init__ = os_supported(OSName.LINUX)(MyModule.__init__)


class MyModuleWithoutInherit:
    @os_supported(OSName.LINUX)
    def __init__(self, *, connection):
        self._conn = connection


conn = SSHConnection(ip="10.10.10.10", username="a", password="a")
# will raise UnexpectedOSException when try to use connection to other OS than Linux
my_module = MyModuleWithInherit(connection=conn)
my_module2 = MyModuleWithoutInherit(connection=conn)
