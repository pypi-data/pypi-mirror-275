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
from urllib.request import Request, urlopen
from typing import Any, Dict, List, TYPE_CHECKING

from animatedledstrip.json_decoder import ALSJsonDecoder
from animatedledstrip.json_encoder import ALSJsonEncoder

if TYPE_CHECKING:
    from animatedledstrip.animation_info import AnimationInfo
    from animatedledstrip.animation_to_run_params import AnimationToRunParams
    from animatedledstrip.new_animation_group_info import NewAnimationGroupInfo
    from animatedledstrip.running_animation_params import RunningAnimationParams
    from animatedledstrip.section import Section
    from animatedledstrip.strip_info import StripInfo


class ALSHttpClient:

    def __init__(self, ip_address: str):
        self.ip_address = ip_address
        self.encoder = ALSJsonEncoder()
        self.decoder = ALSJsonDecoder()

    def _resolve_url(self, url: str) -> str:
        return 'http://' + self.ip_address + ':8080' + url

    def _get_data(self, url: str) -> Any:
        return urlopen(Request(self._resolve_url(url))).read()

    def _post_data(self, url: str, data: Any) -> Any:
        return urlopen(Request(self._resolve_url(url),
                               method='POST',
                               data=bytes(self.encoder.encode(data), 'utf-8'),
                               headers={'Content-Type': 'application/json'})).read()

    def _delete_data(self, url: str) -> Any:
        return urlopen(Request(self._resolve_url(url), method='DELETE')).read()

    def get_animation_info(self, anim_name: str) -> 'AnimationInfo':
        return self.decoder.decode_object_with_type(self._get_data('/animation/' + anim_name), 'AnimationInfo')

    def get_supported_animations(self) -> List['AnimationInfo']:
        return self.decoder.decode_list_with_type(self._get_data('/animations'), 'AnimationInfo')

    def get_supported_animations_map(self) -> Dict[str, 'AnimationInfo']:
        return self.decoder.decode_map_with_type(self._get_data('/animations/map'), 'AnimationInfo')

    def get_supported_animations_dict(self) -> Dict[str, 'AnimationInfo']:
        return self.get_supported_animations_map()

    def get_supported_animations_names(self) -> List[str]:
        return json.loads(self._get_data('/animations/names'))

    def create_new_group(self, new_group: 'NewAnimationGroupInfo'):
        return self.decoder.decode_object_with_type(self._post_data('/animations/newGroup', new_group), 'AnimationInfo')

    def get_running_animations(self) -> Dict[str, 'RunningAnimationParams']:
        return self.decoder.decode_map_with_type(self._get_data('/running'), 'RunningAnimationParams')

    def get_running_animations_ids(self) -> List[str]:
        return json.loads(self._get_data('/running/ids'))

    def get_running_animation_params(self, anim_id: str) -> 'RunningAnimationParams':
        return self.decoder.decode_object_with_type(self._get_data('/running/' + anim_id), 'RunningAnimationParams')

    def end_animation(self, anim_id: str) -> 'RunningAnimationParams':
        return self.decoder.decode_object_with_type(self._delete_data('/running/' + anim_id), 'RunningAnimationParams')

    def get_section(self, section_name: str) -> 'Section':
        return self.decoder.decode_object_with_type(self._get_data('/sections/' + section_name), 'Section')

    def get_sections(self) -> List['Section']:
        return self.decoder.decode_list_with_type(self._get_data('/sections'), 'Section')

    def create_new_section(self, new_section: 'Section') -> 'Section':
        return self.decoder.decode_object_with_type(self._post_data('/sections', new_section), 'Section')

    def get_sections_map(self) -> Dict[str, 'Section']:
        return self.decoder.decode_map_with_type(self._get_data('/sections/map'), 'Section')

    def get_sections_dict(self) -> Dict[str, 'Section']:
        return self.get_sections_map()

    def start_animation(self, anim_params: 'AnimationToRunParams') -> 'RunningAnimationParams':
        return self.decoder.decode_object_with_type(self._post_data('/start', anim_params), 'RunningAnimationParams')

    def save_animation(self, anim_params: 'AnimationToRunParams') -> str:
        return self._post_data('/save', anim_params)

    def get_saved_animations(self) -> List['AnimationToRunParams']:
        return self.decoder.decode_list_with_type(self._get_data('/saved'), 'AnimationToRunParams')

    def clear_strip(self):
        # TODO: Fix 404
        self._post_data('/strip/clear', None)

    def get_current_strip_color(self) -> List[int]:
        return json.loads(self._get_data('/strip/color'))

    def get_strip_info(self) -> 'StripInfo':
        return self.decoder.decode_object_with_type(self._get_data('/strip/info'), 'StripInfo')

    def end_animation_from_params(self, anim_params: 'RunningAnimationParams') -> 'RunningAnimationParams':
        return self.end_animation(anim_params.anim_id)

    def get_full_strip_section(self) -> 'Section':
        return self.get_section('fullStrip')
