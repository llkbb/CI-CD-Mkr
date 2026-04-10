import re
from collections import Counter

def read_file(file_path: str) -> str:
    """Зчитує текст із файлу."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def get_top_words(text: str, top_n: int = 10) -> list:
    """Знаходить top_n найпопулярніших слів у тексті."""
    words = re.findall(r'\b\w+\b', text.lower())
    counter = Counter(words)
    return counter.most_common(top_n)

def write_results(file_path: str, top_words: list) -> None:
    """Записує результат у файл у форматі 'слово-кількість'."""
    with open(file_path, 'w', encoding='utf-8') as file:
        for word, count in top_words:
            file.write(f"{word}-{count}\n")