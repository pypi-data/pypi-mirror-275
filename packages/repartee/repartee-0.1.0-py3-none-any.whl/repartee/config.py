import os
import yaml

def load_config():
    config_path = os.path.expanduser('~/.repartee_config.yaml')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    else:
        return {}

def api_key_available(api):
    keys = load_config().get('api_keys', {})
    return keys.get(api) is not None