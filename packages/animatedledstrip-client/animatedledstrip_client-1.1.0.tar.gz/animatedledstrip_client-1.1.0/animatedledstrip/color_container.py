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

from typing import List, Optional, Dict


class ColorContainer:
    """Stores an array of colors"""

    def __init__(self, colors: Optional[List[int]] = None):
        if colors is None:
            self.colors = []
        else:
            self.colors = colors

    def __eq__(self, other) -> bool:
        return isinstance(other, ColorContainer) and self.colors == other.colors

    def add_color(self, color: int) -> 'ColorContainer':
        """Add a color to the ColorContainer's list of colors"""
        self.colors.append(color)

        # Return this instance so method calls can be chained
        return self

    def json_dict(self) -> Dict:
        return {
            'type': 'ColorContainer',
            'colors': self.colors,
        }


class PreparedColorContainer:

    def __init__(self, colors: Optional[List[int]] = None, original_colors: Optional[List[int]] = None):
        if colors is None:
            self.colors = []
        else:
            self.colors = colors

        if original_colors is None:
            self.original_colors = []
        else:
            self.original_colors = original_colors

    def json_dict(self) -> Dict:
        return {
            'type': 'PreparedColorContainer',
            'colors': self.colors,
            'originalColors': self.original_colors,
        }
