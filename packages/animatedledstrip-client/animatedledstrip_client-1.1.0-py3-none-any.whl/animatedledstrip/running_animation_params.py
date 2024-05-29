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

from typing import List, Dict, Optional, TYPE_CHECKING

from .animation_to_run_params import AnimationToRunParams

if TYPE_CHECKING:
    from animatedledstrip.color_container import PreparedColorContainer
    from animatedledstrip.distance import AbsoluteDistance
    from animatedledstrip.equation import Equation
    from animatedledstrip.location import Location
    from animatedledstrip.rotation import RadiansRotation


class RunningAnimationParams:
    """Describes the properties of a currently running animation"""

    def __init__(self,
                 animation_name: str = "",
                 colors: Optional[List['PreparedColorContainer']] = None,
                 anim_id: str = "",
                 section: str = "",
                 run_count: int = 0,
                 int_params: Optional[Dict[str, int]] = None,
                 double_params: Optional[Dict[str, float]] = None,
                 string_params: Optional[Dict[str, str]] = None,
                 location_params: Optional[Dict[str, 'Location']] = None,
                 distance_params: Optional[Dict[str, 'AbsoluteDistance']] = None,
                 rotation_params: Optional[Dict[str, 'RadiansRotation']] = None,
                 equation_params: Optional[Dict[str, 'Equation']] = None,
                 source_params: 'AnimationToRunParams' = AnimationToRunParams()):
        self.animation_name: str = animation_name
        self.anim_id: str = anim_id
        self.section: str = section
        self.run_count: int = run_count
        self.source_params: 'AnimationToRunParams' = source_params

        if colors is None:
            self.colors: List['PreparedColorContainer'] = []
        else:
            self.colors: List['PreparedColorContainer'] = colors

        if int_params is None:
            self.int_params: Dict[str, int] = {}
        else:
            self.int_params: Dict[str, int] = int_params

        if double_params is None:
            self.double_params: Dict[str, float] = {}
        else:
            self.double_params: Dict[str, float] = double_params

        if string_params is None:
            self.string_params: Dict[str, str] = {}
        else:
            self.string_params: Dict[str, str] = string_params

        if location_params is None:
            self.location_params: Dict[str, 'Location'] = {}
        else:
            self.location_params: Dict[str, 'Location'] = location_params

        if distance_params is None:
            self.distance_params: Dict[str, 'AbsoluteDistance'] = {}
        else:
            self.distance_params: Dict[str, 'AbsoluteDistance'] = distance_params

        if rotation_params is None:
            self.rotation_params: Dict[str, 'RadiansRotation'] = {}
        else:
            self.rotation_params: Dict[str, 'RadiansRotation'] = rotation_params

        if equation_params is None:
            self.equation_params: Dict[str, 'Equation'] = {}
        else:
            self.equation_params: Dict[str, 'Equation'] = equation_params

    def json_dict(self) -> Dict:
        return {
            "animationName": self.animation_name,
            "colors": self.colors,
            "id": self.anim_id,
            "section": self.section,
            "runCount": self.run_count,
            "intParams": self.int_params,
            "doubleParams": self.double_params,
            "stringParams": self.string_params,
            "locationParams": self.location_params,
            "distanceParams": self.distance_params,
            "rotationParams": self.rotation_params,
            "equationParams": self.equation_params,
            "sourceParams": self.source_params,
        }
