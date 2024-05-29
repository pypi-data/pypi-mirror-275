#  Copyright (c) 2018-2021 AnimatedLEDStrip
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

from typing import Optional, List

from .location import Location


class StripInfo(object):
    """Stores information about a LED strip"""

    def __init__(self,
                 num_leds: int = 0,
                 pin: Optional[int] = None,
                 render_delay: int = 10,
                 is_render_logging_enabled: bool = False,
                 render_log_file: str = '',
                 renders_between_log_saves: int = 1000,
                 is_1d_supported: bool = True,
                 is_2d_supported: bool = False,
                 is_3d_supported: bool = False,
                 led_locations: Optional[List['Location']] = None):
        self.num_leds: int = num_leds
        self.pin: Optional[int] = pin
        self.render_delay: int = render_delay
        self.is_render_logging_enabled: bool = is_render_logging_enabled
        self.render_log_file: str = render_log_file
        self.renders_between_log_saves: int = renders_between_log_saves
        self.is_1d_supported: bool = is_1d_supported
        self.is_2d_supported: bool = is_2d_supported
        self.is_3d_supported: bool = is_3d_supported

        if led_locations is None:
            self.led_locations: List['Location'] = []
        else:
            self.led_locations: List['Location'] = led_locations
