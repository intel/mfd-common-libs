# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT
import logging
from mfd_common_libs import add_logging_level, add_logging_group, log_levels, LevelGroup

logger = logging.getLogger(__name__)
logging.basicConfig(level=log_levels.MODULE_DEBUG)

# You can set log levels one by one
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

add_logging_level("MODULE_DEBUG", log_levels.MODULE_DEBUG)
add_logging_level("CMD", log_levels.CMD)

# Or you can use addition of whole groups
add_logging_group(LevelGroup.BL)
add_logging_group(LevelGroup.MFD)
add_logging_group(LevelGroup.TEST)

logger.log(level=log_levels.TEST_STEP, msg="TEST_STEP message")
logger.log(level=log_levels.TEST_INFO, msg="TEST_INFO message")
logger.log(level=log_levels.TEST_DEBUG, msg="TEST_DEBUG message")
logger.log(level=log_levels.BL_STEP, msg="BL_STEP message")
logger.log(level=log_levels.BL_INFO, msg="BL_INFO message")
logger.log(level=log_levels.BL_DEBUG, msg="BL_DEBUG message")
logger.log(level=log_levels.MFD_STEP, msg="MFD_STEP message")
logger.log(level=log_levels.MFD_INFO, msg="MFD_INFO message")
logger.log(level=log_levels.MFD_DEBUG, msg="MFD_DEBUG message")
logger.log(level=log_levels.MODULE_DEBUG, msg="MODULE_DEBUG message")
logger.log(level=log_levels.CMD, msg="CMD message")
logger.log(level=log_levels.TEST_PASS, msg="TEST_PASS message")
logger.log(level=log_levels.TEST_FAIL, msg="TEST_FAIL message")
