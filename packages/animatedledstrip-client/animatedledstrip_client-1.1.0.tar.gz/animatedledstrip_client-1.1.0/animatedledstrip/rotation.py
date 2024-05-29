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

from typing import Optional, List, Dict


class DegreesRotation:
    """A rotation specified in degrees"""

    def __init__(self,
                 x_rotation: float = 0.0,
                 y_rotation: float = 0.0,
                 z_rotation: float = 0.0,
                 rotation_order: Optional[List[str]] = None):
        self.x_rotation: float = x_rotation
        self.y_rotation: float = y_rotation
        self.z_rotation: float = z_rotation

        if rotation_order is None:
            self.rotation_order = ['ROTATE_Z', 'ROTATE_X']
        else:
            self.rotation_order = rotation_order

    def json_dict(self) -> Dict:
        return {
            'type': 'DegreesRotation',
            'xRotation': self.x_rotation,
            'yRotation': self.y_rotation,
            'zRotation': self.z_rotation,
            'rotationOrder': self.rotation_order,
        }


class RadiansRotation:
    """A rotation specified in radians"""

    def __init__(self,
                 x_rotation: float = 0.0,
                 y_rotation: float = 0.0,
                 z_rotation: float = 0.0,
                 rotation_order: Optional[List[str]] = None):
        self.x_rotation: float = x_rotation
        self.y_rotation: float = y_rotation
        self.z_rotation: float = z_rotation

        if rotation_order is None:
            self.rotation_order = ['ROTATE_Z', 'ROTATE_X']
        else:
            self.rotation_order = rotation_order

    def json_dict(self) -> Dict:
        return {
            'type': 'RadiansRotation',
            'xRotation': self.x_rotation,
            'yRotation': self.y_rotation,
            'zRotation': self.z_rotation,
            'rotationOrder': self.rotation_order,
        }
