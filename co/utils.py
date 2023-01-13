import os
import subprocess
from co.constants import COHERE_API_KEY, COHERE_MODEL, DEFAULT_MODEL


def get_key():
    if COHERE_API_KEY not in os.environ:
        raise KeyError(f"Environment variable {COHERE_API_KEY} not set. "
                       f"You can set it with: export {COHERE_API_KEY}=<your key>")
    key = os.environ[COHERE_API_KEY]
    return key

def get_model():
    if COHERE_MODEL in os.environ:
        return os.environ[COHERE_MODEL]
    else:
        return DEFAULT_MODEL

def get_distro_info():
    return subprocess.run(['lsb_release', '-a'], capture_output=True).stdout.decode('utf-8')