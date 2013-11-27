"""Global smashery config"""

import yaml
import os

_settings_file = "settings.yaml"
settings = {}

if os.path.exists(_settings_file):
  with open(_settings_file) as s:
    settings = yaml.load(s)

