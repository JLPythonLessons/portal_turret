import file_manager
import random
import subprocess
from typing import Optional

FILES = file_manager.load_files()


def get_random_sound(category: str) -> Optional[str]:
    if (file_list := FILES.get(category)):
        return random.choice(file_list)


def play_file(file: str):
    subprocess.call(['afplay', file])


def play_random_sound(category: str) -> bool:
    file = get_random_sound(category)
    if file:
        subprocess.Popen(['afplay', file])
    return file is not None
