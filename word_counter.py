import re
from collections import Counter

def read_file(file_path: str) -> str:
    """Зчитує текст із файлу."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()