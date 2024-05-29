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
import json
from json import JSONDecoder
from typing import Dict, Any

from .animation_info import AnimationInfo, AnimationParameter
from .animation_to_run_params import AnimationToRunParams
from .color_container import ColorContainer, PreparedColorContainer
from .distance import AbsoluteDistance, PercentDistance
from .json_encoder import ALSJsonEncoder
from .location import Location
from .rotation import DegreesRotation, RadiansRotation
from .running_animation_params import RunningAnimationParams
from .section import Section
from .strip_info import StripInfo


def add_dicts(dict1: Dict, dict2: Dict) -> Dict:
    dict1.update(dict2)
    return dict1


class ALSJsonDecoder(JSONDecoder):

    def __init__(self, *args, **kwargs):
        JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

        self.encoder = ALSJsonEncoder()

    def decode_dict(self, json: Dict) -> Any:
        return self.decode(self.encoder.encode(json))

    def decode_object_with_type(self, obj, data_type: str):
        return self.decode_dict(add_dicts(json.loads(obj), {"type": data_type}))

    def decode_list_with_type(self, obj, data_type: str):
        json_list = json.loads(obj)
        decoded_list = []
        for o in json_list:
            decoded_list.append(self.decode_dict(add_dicts(o, {"type": data_type})))
        return decoded_list

    def decode_map_with_type(self, obj, data_type: str):
        json_dict = json.loads(obj)
        decoded_dict = {}
        for k in json_dict:
            decoded_dict.update({k: self.decode_dict(add_dicts(json_dict[k], {"type": data_type}))})
        return decoded_dict

    def object_hook(self, obj):
        data_type = obj.get('type', '')
        if data_type == 'AbsoluteDistance':
            return AbsoluteDistance(obj['x'], obj['y'], obj['z'])
        elif data_type == 'AnimationInfo':
            return AnimationInfo(
                name=obj['name'],
                abbr=obj['abbr'],
                description=obj['description'],
                run_count_default=obj['runCountDefault'],
                minimum_colors=obj['minimumColors'],
                unlimited_colors=obj['unlimitedColors'],
                dimensionality=obj['dimensionality'],
                int_params=[self.decode_dict(add_dicts(param, {'type': 'AnimationParameter',
                                                               'data_type': 'int'}))
                            for param in obj['intParams']],
                double_params=[self.decode_dict(add_dicts(param, {'type': 'AnimationParameter',
                                                                  'data_type': 'float'}))
                               for param in obj['doubleParams']],
                string_params=[self.decode_dict(add_dicts(param, {'type': 'AnimationParameter',
                                                                  'data_type': 'str'}))
                               for param in obj['stringParams']],
                location_params=[self.decode_dict(add_dicts(param, {'type': 'AnimationParameter',
                                                                    'data_type': 'Location'}))
                                 for param in obj['locationParams']],
                distance_params=[self.decode_dict(add_dicts(param, {'type': 'AnimationParameter',
                                                                    'data_type': 'Distance'}))
                                 for param in obj['distanceParams']],
                rotation_params=[self.decode_dict(add_dicts(param, {'type': 'AnimationParameter',
                                                                    'data_type': 'Rotation'}))
                                 for param in obj['rotationParams']],
                equation_params=[self.decode_dict(add_dicts(param, {'type': 'AnimationParameter',
                                                                    'data_type': 'Equation'}))
                                 for param in obj['equationParams']],
            )
        elif data_type == 'AnimationParameter':
            if hasattr(obj, 'default'):
                if obj['data_type'] == 'Location':
                    obj['default'] = self.decode_dict(add_dicts(obj['default'], {'type': 'Location'}))
                elif obj['data_type'] == 'Equation':
                    obj['default'] = self.decode_dict(add_dicts(obj['default'], {'type': 'Equation'}))
                else:
                    obj['default'] = self.decode_dict(obj['default'])
            return AnimationParameter(name=obj['name'],
                                      description=obj['description'],
                                      default=obj['default'],
                                      data_type=obj['data_type'])
        elif data_type == 'AnimationToRunParams':
            return AnimationToRunParams(
                animation=obj['animation'],
                colors=[self.decode_dict(param) for param in obj['colors']],
                anim_id=obj['id'],
                run_count=obj['runCount'],
                int_params=obj['intParams'],
                double_params=obj['doubleParams'],
                string_params=obj['stringParams'],
                location_params={key: self.decode_dict(add_dicts(param, {'type': 'Location'}))
                                 for (key, param) in obj['locationParams']},
                distance_params={key: self.decode_dict(param) for (key, param) in obj['distanceParams']},
                rotation_params={key: self.decode_dict(param) for (key, param) in obj['rotationParams']},
                equation_params={key: self.decode_dict(add_dicts(param, {'type': 'Equation'}))
                                 for (key, param) in obj['equationParams']},
            )
        elif data_type == 'ColorContainer':
            return ColorContainer(obj['colors'])
        elif data_type == 'DegreesRotation':
            return DegreesRotation(obj['xRotation'], obj['yRotation'], obj['zRotation'], obj['rotationOrder'])
        elif data_type == 'Location':
            return Location(obj['x'], obj['y'], obj['z'])
        elif data_type == 'PercentDistance':
            return PercentDistance(obj['x'], obj['y'], obj['z'])
        elif data_type == 'PreparedColorContainer':
            return PreparedColorContainer(obj['colors'], obj['originalColors'])
        elif data_type == 'RadiansRotation':
            return RadiansRotation(obj['xRotation'], obj['yRotation'], obj['zRotation'], obj['rotationOrder'])
        elif data_type == 'RunningAnimationParams':
            return RunningAnimationParams(
                animation_name=obj['animationName'],
                colors=[self.decode_dict(param) for param in obj['colors']],
                anim_id=obj['id'],
                run_count=obj['runCount'],
                int_params=obj['intParams'],
                double_params=obj['doubleParams'],
                string_params=obj['stringParams'],
                location_params={key: self.decode_dict(add_dicts(param, {'type': 'Location'}))
                                 for (key, param) in obj['locationParams'].items()},
                distance_params={key: self.decode_dict(add_dicts(param, {'type': 'AbsoluteDistance'}))
                                 for (key, param) in obj['distanceParams'].items()},
                rotation_params={key: self.decode_dict(add_dicts(param, {'type': 'RadiansRotation'}))
                                 for (key, param) in obj['rotationParams'].items()},
                equation_params={key: self.decode_dict(add_dicts(param, {'type': 'Equation'}))
                                 for (key, param) in obj['equationParams'].items()},
                source_params=self.decode_dict(obj['sourceParams'])
            )
        elif data_type == 'Section':
            return Section(obj['name'], obj['pixels'], obj['parentSectionName'])
        elif data_type == 'StripInfo':
            return StripInfo(
                num_leds=obj['numLEDs'],
                pin=obj['pin'],
                render_delay=obj['renderDelay'],
                is_render_logging_enabled=obj['isRenderLoggingEnabled'],
                render_log_file=obj['renderLogFile'],
                renders_between_log_saves=obj['rendersBetweenLogSaves'],
                is_1d_supported=obj['is1DSupported'],
                is_2d_supported=obj['is2DSupported'],
                is_3d_supported=obj['is3DSupported'],
                led_locations=[self.decode_dict(add_dicts(param, {'type': 'Location'}))
                               for param in obj['ledLocations']] if obj['ledLocations'] is not None else None,
            )
        else:
            return obj
