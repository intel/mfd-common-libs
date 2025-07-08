# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT
"""Tests for TimeoutCounter."""

from mfd_common_libs import TimeoutCounter


class TestTimeoutCounter:
    def test_first_check_start_default(self, mocker):
        time_mock = mocker.patch("mfd_common_libs.timeout_counter.time", autospec=True, spec_set=True)
        time_mock.return_value = 0
        obj = TimeoutCounter(10)
        time_mock.return_value += 11
        assert bool(obj) is False
        time_mock.return_value += 5
        assert bool(obj) is False
        time_mock.return_value += 6
        assert bool(obj) is True

    def test_first_check_start_off(self, mocker):
        time_mock = mocker.patch("mfd_common_libs.timeout_counter.time", autospec=True, spec_set=True)
        time_mock.return_value = 0
        obj = TimeoutCounter(10, first_check_start=False)
        time_mock.return_value += 11
        assert bool(obj) is True

    def test_repeatable_requests_after_timeout(self):
        obj = TimeoutCounter(10)
        obj._time_is_up = True
        assert bool(obj) is True
        assert bool(obj) is True
