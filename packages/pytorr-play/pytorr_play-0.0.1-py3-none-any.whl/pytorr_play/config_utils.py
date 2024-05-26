import os
import yaml
from pytorr_play import PyTorrPlay


def generate_config():
    config_dir = PyTorrPlay.CONFIG_DIR
    config_file = PyTorrPlay.CONFIG_FILE

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    config = {
        "JACKETT_API_KEY": "your_api_key_here",
        "JACKET_PORT": 9117,
        "JACKET_ADDRESS": "127.0.0.1"
    }

    with open(config_file, 'w') as f:
        yaml.dump(config, f)

    print(f"Configuration file generated at {config_file}")


def load_config():
    config_file = PyTorrPlay.CONFIG_FILE
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return yaml.load(f, Loader=yaml.SafeLoader)
    else:
        print(f"Configuration file not found at {config_file}. Run with --generate-config to create one.")
        exit(1)


def load_config_from_path(config_path):
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.load(f, Loader=yaml.SafeLoader)
    else:
        print(f"Configuration file not found at {config_path}. Run with --generate-config to create one.")
        exit(1)
