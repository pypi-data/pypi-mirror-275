import os

def check_env_exists():
    return os.path.isfile('.env')
