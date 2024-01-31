from os import environ
from pathlib import Path


# Disabling grpc fork error log spam
environ["GRPC_ENABLE_FORK_SUPPORT"] = "false"

# Dirs
BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio"

# Keys
YANDEX_API_KEY = environ["YANDEX_API_KEY"]  

# Audio speeds
DEFAULT_WORD_AUDIO_SPEED = 0.8
DEFAULT_EXAMPLE_AUDIO_SPEED = 0.9
