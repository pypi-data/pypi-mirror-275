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


class AnimationParameter:
    """Specifies an animation parameter that can be sent to an animation"""

    def __init__(self, name: str = '', description: str = '', default=None, data_type=None):
        self.name: str = name
        self.description: str = description
        self.default = default
        self.data_type = data_type

    def json_dict(self) -> Dict:
        return {
            'name': self.name,
            'description': self.description,
            'default': self.default,
        }


class AnimationInfo:
    """Stores information about an animation the server can run"""

    def __init__(self,
                 name: str = '',
                 abbr: str = '',
                 description: str = '',
                 run_count_default: int = 0,
                 minimum_colors: int = 0,
                 unlimited_colors: bool = False,
                 dimensionality: Optional[List[str]] = None,
                 int_params: Optional[List[AnimationParameter]] = None,
                 double_params: Optional[List[AnimationParameter]] = None,
                 string_params: Optional[List[AnimationParameter]] = None,
                 location_params: Optional[List[AnimationParameter]] = None,
                 distance_params: Optional[List[AnimationParameter]] = None,
                 rotation_params: Optional[List[AnimationParameter]] = None,
                 equation_params: Optional[List[AnimationParameter]] = None):
        self.name: str = name
        self.abbr: str = abbr
        self.description: str = description
        self.run_count_default: int = run_count_default
        self.minimum_colors: int = minimum_colors
        self.unlimited_colors: bool = unlimited_colors

        if dimensionality is None:
            self.dimensionality: List[str] = []
        else:
            self.dimensionality: List[str] = dimensionality

        if int_params is None:
            self.int_params: List[AnimationParameter] = []
        else:
            self.int_params: List[AnimationParameter] = int_params

        if double_params is None:
            self.double_params: List[AnimationParameter] = []
        else:
            self.double_params: List[AnimationParameter] = double_params

        if string_params is None:
            self.string_params: List[AnimationParameter] = []
        else:
            self.string_params: List[AnimationParameter] = string_params

        if location_params is None:
            self.location_params: List[AnimationParameter] = []
        else:
            self.location_params: List[AnimationParameter] = location_params

        if distance_params is None:
            self.distance_params: List[AnimationParameter] = []
        else:
            self.distance_params: List[AnimationParameter] = distance_params

        if rotation_params is None:
            self.rotation_params: List[AnimationParameter] = []
        else:
            self.rotation_params: List[AnimationParameter] = rotation_params

        if equation_params is None:
            self.equation_params: List[AnimationParameter] = []
        else:
            self.equation_params: List[AnimationParameter] = equation_params

    def json_dict(self) -> Dict:
        return {
            'name': self.name,
            'abbr': self.abbr,
            'description': self.description,
            'runCountDefault': self.run_count_default,
            'minimumColors': self.minimum_colors,
            'unlimitedColors': self.unlimited_colors,
            'dimensionality': self.dimensionality,
            'intParams': self.int_params,
            "doubleParams": self.double_params,
            "stringParams": self.string_params,
            "locationParams": self.location_params,
            "distanceParams": self.distance_params,
            "rotationParams": self.rotation_params,
            "equationParams": self.equation_params,
        }
