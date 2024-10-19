import random
import re
import string
import json

def sanitize_string(string: str) -> str:
    """
    Given the string, returns a sanitized version of it.
    """
    return re.sub(r"[\"<>:/\|\\?\*\[\]]+", "__", string)

def generate_random_string(length=8):
    """
    Generates a random string of the given length.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def load_json(file_path, encoding=None):
    """
    Loads a JSON file and returns the contents as a dictionary.
    """
    with open(file_path, 'r', encoding=encoding) as file:
        return json.load(file)
