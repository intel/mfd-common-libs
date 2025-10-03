# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT
"""Module for DisableLogger context manager."""

import logging
from .log_levels import MODULE_DEBUG


class DisableLogger:
    """Class for context manager temporarily suppressing logging."""

    def __init__(self, level: int = MODULE_DEBUG):
        """Initialize DisableLogger."""
        self.level = level

    def __enter__(self):
        logging.disable(self.level)

    def __exit__(self, exit_type, exit_value, exit_traceback):  # noqa: ANN001
        logging.disable(logging.NOTSET)
