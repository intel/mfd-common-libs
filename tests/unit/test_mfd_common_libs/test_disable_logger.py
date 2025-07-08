# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT
import pytest
import logging

from mfd_common_libs import DisableLogger, log_levels


class TestDisableLogger:
    """Class for tests of DisableLogger class."""

    test_log_message = "test"
    restored_log_message = "restored"

    @pytest.fixture()
    def logger(self):
        return logging.getLogger(__name__)

    def test_log_not_suppressed_by_default(self, logger, caplog):
        with caplog.at_level(log_levels.MODULE_DEBUG):
            logger.log(level=log_levels.MODULE_DEBUG, msg=self.test_log_message)
        assert self.test_log_message in caplog.messages

    def test_log_suppressed(self, logger, caplog):
        with caplog.at_level(log_levels.MODULE_DEBUG):
            with DisableLogger():
                logger.log(level=log_levels.MODULE_DEBUG, msg=self.test_log_message)
        assert self.test_log_message not in caplog.messages

    def test_log_ability_reversed_outside_of_context_manager(self, logger, caplog):
        with caplog.at_level(log_levels.MODULE_DEBUG):
            with DisableLogger():
                pass
            logger.log(level=log_levels.MODULE_DEBUG, msg=self.restored_log_message)

        assert self.restored_log_message in caplog.messages
