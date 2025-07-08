# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT
import logging

from mfd_common_libs import log_func_info

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@log_func_info(logger)
def calling_someone(someone):
    pass


@log_func_info(logger)
def calling_someone_kwargs(someone):
    pass


@log_func_info(logger)
def calling():
    pass


calling_someone("Adam")
calling_someone_kwargs(someone="Adam")
calling()
