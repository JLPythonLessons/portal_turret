import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_DIR = os.path.join(CURRENT_DIR, 'sounds')
CATEGORIES = {
    'startup': 'turret_autosearch',
    'shutdown': 'turret_retire',
    'target_found': 'turret_active',
    'target_lost': 'turret_search',
    'quote': 'different_',
    'fire': 'turret_fire',
    'error': 'turret_tipped',
}


def load_files(categories=CATEGORIES):
    files = {category: list() for category in CATEGORIES.keys()}

    for file in os.listdir(SOUND_DIR):
        file = file.lower()
        # Check that file is wav
        if file.endswith('.wav'):
            for category, prefix in CATEGORIES.items():
                # Attempt to match file prefix
                if file.startswith(prefix):
                    # Add file to output dictionary
                    files[category].append(os.path.join(SOUND_DIR, file))

    return files
