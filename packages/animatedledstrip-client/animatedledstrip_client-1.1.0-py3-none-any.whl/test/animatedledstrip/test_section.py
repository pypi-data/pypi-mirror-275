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

from animatedledstrip import *


def test_constructor():
    sect = Section()

    assert sect.name == ''
    assert sect.start_pixel == -1
    assert sect.end_pixel == -1
    assert sect.physical_start == -1
    assert sect.num_leds == 0


def test_name(caplog):
    sect = Section()

    sect.name = 'Test'
    assert sect.check_data_types() is True

    sect.name = 5
    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert sect.check_data_types() is False
        log_messages = {(log.msg, log.levelname) for log in caplog.records}
        assert log_messages == {("Bad data type for name: <class 'int'> (should be <class 'str'>)", 'ERROR')}

    try:
        sect.check_data_types()
        raise AssertionError
    except TypeError:
        pass


def test_start_pixel(caplog):
    sect = Section()

    sect.start_pixel = 3
    assert sect.check_data_types() is True

    sect.start_pixel = '5'
    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert sect.check_data_types() is False
        log_messages = {(log.msg, log.levelname) for log in caplog.records}
        assert log_messages == {("Bad data type for start_pixel: <class 'str'> (should be <class 'int'>)", 'ERROR')}

    try:
        sect.check_data_types()
        raise AssertionError
    except TypeError:
        pass


def test_end_pixel(caplog):
    sect = Section()

    sect.end_pixel = 3
    assert sect.check_data_types() is True

    sect.end_pixel = '5'
    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert sect.check_data_types() is False
        log_messages = {(log.msg, log.levelname) for log in caplog.records}
        assert log_messages == {("Bad data type for end_pixel: <class 'str'> (should be <class 'int'>)", 'ERROR')}

    try:
        sect.check_data_types()
        raise AssertionError
    except TypeError:
        pass


def test_physical_start(caplog):
    sect = Section()

    sect.physical_start = 3
    assert sect.check_data_types() is True

    sect.physical_start = '5'
    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert sect.check_data_types() is False
        log_messages = {(log.msg, log.levelname) for log in caplog.records}
        assert log_messages == {("Bad data type for physical_start: <class 'str'> (should be <class 'int'>)", 'ERROR')}

    try:
        sect.check_data_types()
        raise AssertionError
    except TypeError:
        pass


def test_num_leds(caplog):
    sect = Section()

    sect.num_leds = 3
    assert sect.check_data_types() is True

    sect.num_leds = '5'
    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert sect.check_data_types() is False
        log_messages = {(log.msg, log.levelname) for log in caplog.records}
        assert log_messages == {("Bad data type for num_leds: <class 'str'> (should be <class 'int'>)", 'ERROR')}

    try:
        sect.check_data_types()
        raise AssertionError
    except TypeError:
        pass


def test_json():
    sect = Section()

    sect.name = 'TEST'
    sect.start_pixel = 40
    sect.end_pixel = 50

    assert sect.json() == 'SECT:{"name":"TEST","startPixel":40,"endPixel":50}'


def test_json_bad_type():
    sect = Section()
    sect.start_pixel = 'bad'

    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert sect.json() == ''

    try:
        sect.json()
        raise AssertionError
    except TypeError:
        pass


def test_from_json():
    json_data = 'SECT:{"physicalStart":0,"numLEDs":240,"name":"section","startPixel":0,"endPixel":239}'

    sect = Section.from_json(json_data)
    assert sect.name == 'section'
    assert sect.start_pixel == 0
    assert sect.end_pixel == 239
    assert sect.physical_start == 0
    assert sect.num_leds == 240

    assert sect.json() == 'SECT:{"name":"section","startPixel":0,"endPixel":239}'
