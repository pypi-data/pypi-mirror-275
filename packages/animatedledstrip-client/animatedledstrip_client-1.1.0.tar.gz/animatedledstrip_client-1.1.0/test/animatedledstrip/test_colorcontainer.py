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

import json
from unittest import mock

from animatedledstrip import ColorContainer


def test_add_color():
    color = ColorContainer()

    color.add_color(0xFF)
    assert color.colors == [255]

    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        # noinspection PyTypeChecker
        color.add_color(None)
    assert color.colors == [255]

    try:
        # noinspection PyTypeChecker
        color.add_color(None)
        raise AssertionError
    except TypeError:
        pass


def test_eq():
    assert ColorContainer().add_color(0xFF) == ColorContainer().add_color(255)
    assert not ColorContainer().add_color(0xFF) == ColorContainer().add_color(0xFE)


def test_json():
    assert ColorContainer().add_color(0xFF).add_color(0x0F).json() == '{"colors":[255,15]}'
    assert ColorContainer().add_color(0x0F).json() == '{"colors":[15]}'
    assert ColorContainer().json() == '{"colors":[]}'


def test_from_json():
    color_json = json.loads('{"colors":[255]}')
    assert ColorContainer.from_json(color_json).colors == [255]

    color_json = json.loads('{"colors":[]}')
    assert ColorContainer.from_json(color_json).colors == []

    color_json = json.loads('{"colors":["test"]}')
    with mock.patch('animatedledstrip.global_vars.STRICT_TYPE_CHECKING', False):
        assert ColorContainer.from_json(color_json).colors == []

    try:
        ColorContainer.from_json(color_json)
        raise AssertionError
    except TypeError:
        pass
