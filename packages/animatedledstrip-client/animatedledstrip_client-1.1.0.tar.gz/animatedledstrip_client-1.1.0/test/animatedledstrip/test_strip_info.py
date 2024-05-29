#   Copyright (c) 2019-2020 AnimatedLEDStrip
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#   THE SOFTWARE.
from unittest import mock

from animatedledstrip import StripInfo


def test_constructor():
    info = StripInfo()

    assert info.num_leds == 0
    assert info.pin is None
    assert info.image_debugging is False
    assert info.file_name is None
    assert info.renders_before_save is None
    assert info.thread_count == 100


def test_num_leds(caplog):
    info = StripInfo()

    info.num_leds = 100
    assert info.check_data_types() is True

    info.num_leds = 1.0
    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert info.check_data_types() is False
        log_messages = {(log.msg, log.levelname) for log in caplog.records}
        assert log_messages == {("Bad data type for num_leds: <class 'float'> (should be <class 'int'>)", 'ERROR')}

    try:
        info.check_data_types()
        raise AssertionError
    except TypeError:
        pass


def test_pin(caplog):
    info = StripInfo()

    info.pin = 10
    assert info.check_data_types() is True

    info.pin = None
    assert info.check_data_types() is True

    info.pin = 1.0
    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert info.check_data_types() is False
        log_messages = {(log.msg, log.levelname) for log in caplog.records}
        assert log_messages == {("Bad data type for pin: <class 'float'> (should be <class 'int'> or None)", 'ERROR')}

    try:
        info.check_data_types()
        raise AssertionError
    except TypeError:
        pass


def test_image_debugging(caplog):
    info = StripInfo()

    info.image_debugging = True
    assert info.check_data_types() is True

    info.image_debugging = 1.0
    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert info.check_data_types() is False
        log_messages = {(log.msg, log.levelname) for log in caplog.records}
        assert log_messages == {
            ("Bad data type for image_debugging: <class 'float'> (should be <class 'bool'>)", 'ERROR')
        }

    try:
        info.check_data_types()
        raise AssertionError
    except TypeError:
        pass


def test_file_name(caplog):
    info = StripInfo()

    info.file_name = 'file.csv'
    assert info.check_data_types() is True

    info.file_name = None
    assert info.check_data_types() is True

    info.file_name = 1.0
    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert info.check_data_types() is False
        log_messages = {(log.msg, log.levelname) for log in caplog.records}
        assert log_messages == {
            ("Bad data type for file_name: <class 'float'> (should be <class 'str'> or None)", 'ERROR')
        }

    try:
        info.check_data_types()
        raise AssertionError
    except TypeError:
        pass


def test_renders_before_save(caplog):
    info = StripInfo()

    info.renders_before_save = 10
    assert info.check_data_types() is True

    info.renders_before_save = None
    assert info.check_data_types() is True

    info.renders_before_save = 1.0
    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert info.check_data_types() is False
        log_messages = {(log.msg, log.levelname) for log in caplog.records}
        assert log_messages == {
            ("Bad data type for renders_before_save: <class 'float'> (should be <class 'int'> or None)", 'ERROR')
        }

    try:
        info.check_data_types()
        raise AssertionError
    except TypeError:
        pass


def test_thread_count(caplog):
    info = StripInfo()

    info.thread_count = 100
    assert info.check_data_types() is True

    info.thread_count = 1.0
    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert info.check_data_types() is False
        log_messages = {(log.msg, log.levelname) for log in caplog.records}
        assert log_messages == {("Bad data type for thread_count: <class 'float'> (should be <class 'int'>)", 'ERROR')}

    try:
        info.check_data_types()
        raise AssertionError
    except TypeError:
        pass
