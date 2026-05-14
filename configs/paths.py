import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def asset_path(*parts):
    return os.path.join(BASE_DIR, "assets", *parts)
