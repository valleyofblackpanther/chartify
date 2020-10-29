# -*- coding: utf-8 -*-
#
# Copyright (c) 2017-2020 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from tempfile import TemporaryDirectory

STYLE_SETTINGS_CONFIG = '''\
foo:
  baz.bar: 0.25
  quux: deadbeef
bar:
  baz: bar quux
'''


def test_colors_config(monkeypatch):
    with TemporaryDirectory() as tmp:
        with open(os.path.join(tmp, 'style_settings_config.yaml'), 'w') as f:
            f.write(STYLE_SETTINGS_CONFIG)

        # XXX (dano): CHARTIFY_CONFIG_DIR must end with /
        monkeypatch.setenv('CHARTIFY_CONFIG_DIR', os.path.join(tmp, ''))

        # Check that the expected style is loaded
        import chartify._core.style
        style = chartify._core.style.Style(None, '')

        import yaml
        expected_settings = yaml.safe_load(STYLE_SETTINGS_CONFIG)

        for key, expected_value in expected_settings.items():
            actual_value = style.settings[key]
            assert expected_value == actual_value

