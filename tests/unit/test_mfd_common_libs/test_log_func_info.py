# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT
import logging

import pytest

from mfd_common_libs import log_func_info, log_levels


class TestLogFuncInfo:
    @pytest.fixture()
    def logger(self, mocker):
        return mocker.create_autospec(logging.Logger)

    def test_clean_function(self, logger):
        @log_func_info(logger)
        def calling():
            pass

        calling()
        logger.log.assert_called_with(level=log_levels.MODULE_DEBUG, msg="Calling func: calling")

    def test_function_with_args(self, logger):
        @log_func_info(logger)
        def calling_with_args(argument):
            pass

        calling_with_args("arg")
        logger.log.assert_called_with(
            level=log_levels.MODULE_DEBUG, msg="Calling func: calling_with_args with arguments: ['arg']"
        )

    def test_function_with_kwargs(self, logger):
        @log_func_info(logger)
        def calling_with_kwargs(argument):
            pass

        calling_with_kwargs(argument="arg")
        logger.log.assert_called_with(
            level=log_levels.MODULE_DEBUG,
            msg=("Calling func: calling_with_kwargs " "with keyword arguments: {'argument': 'arg'}"),
        )

    def test_function_with_args_and_kwargs(self, logger):
        @log_func_info(logger)
        def calling_with_args_kwargs(arg, kwarg):
            pass

        calling_with_args_kwargs("arg", kwarg="kwarg")
        logger.log.assert_called_with(
            level=log_levels.MODULE_DEBUG,
            msg=(
                "Calling func: calling_with_args_kwargs "
                "with arguments: ['arg'] "
                "keyword arguments: {'kwarg': 'kwarg'}"
            ),
        )
