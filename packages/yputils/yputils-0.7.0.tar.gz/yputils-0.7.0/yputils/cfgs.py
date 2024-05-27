import tomllib
import os


def load_toml(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            return tomllib.load(f)
    else:
        return None

