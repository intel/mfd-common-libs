# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT

from mfd_common_libs import add_logging_level, log_levels


class TestCustomLogger:
    def test_successfully_added_custom_loggers(self):
        add_logging_level(level_name="CMD", level_value=log_levels.CMD)
        add_logging_level(level_name="MODULE_DEBUG", level_value=log_levels.MODULE_DEBUG)
        add_logging_level(level_name="MFD_DEBUG", level_value=log_levels.MFD_DEBUG)
        add_logging_level(level_name="MFD_INFO", level_value=log_levels.MFD_INFO)
        add_logging_level(level_name="MFD_STEP", level_value=log_levels.MFD_STEP)
        add_logging_level(level_name="BL_DEBUG", level_value=log_levels.BL_DEBUG)
        add_logging_level(level_name="BL_INFO", level_value=log_levels.BL_INFO)
        add_logging_level(level_name="BL_STEP", level_value=log_levels.BL_STEP)
        add_logging_level(level_name="TEST_DEBUG", level_value=log_levels.TEST_DEBUG)
        add_logging_level(level_name="TEST_INFO", level_value=log_levels.TEST_INFO)
        add_logging_level(level_name="TEST_STEP", level_value=log_levels.TEST_STEP)
        add_logging_level(level_name="TEST_PASS", level_value=log_levels.TEST_PASS)
        add_logging_level(level_name="TEST_FAIL", level_value=log_levels.TEST_FAIL)

    def test_double_import_of_logger(self):
        add_logging_level(level_name="CMD", level_value=log_levels.CMD)
        add_logging_level(level_name="CMD", level_value=log_levels.CMD)
