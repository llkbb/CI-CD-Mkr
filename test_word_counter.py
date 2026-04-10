import pytest
from word_counter import read_file, get_top_words, write_results


# --- Фікстури ---
@pytest.fixture
def sample_input_file(tmp_path):
    """Фікстура створює тимчасовий вхідний файл для тестів."""
    file_path = tmp_path / "test_input.txt"
    file_path.write_text("Hello world! Hello Python. Python is great.", encoding='utf-8')
    return file_path


@pytest.fixture
def sample_output_file(tmp_path):
    """Фікстура повертає шлях до тимчасового вихідного файлу."""
    return tmp_path / "test_output.txt"


# --- Тести ---
def test_read_file(sample_input_file):
    content = read_file(sample_input_file)
    assert "Hello Python" in content


@pytest.mark.parametrize("text, top_n, expected", [
    ("apple banana apple", 1, [("apple", 2)]),
    ("one two two three three three", 2, [("three", 3), ("two", 2)]),
    ("Hello, hello! World.", 2, [("hello", 2), ("world", 1)]),
    ("", 5, [])  # Порожній рядок
])
def test_get_top_words(text, top_n, expected):
    assert get_top_words(text, top_n) == expected


def test_write_results(sample_output_file):
    data = [("apple", 5), ("banana", 3)]
    write_results(sample_output_file, data)

    content = sample_output_file.read_text(encoding='utf-8')
    assert "apple-5\n" in content
    assert "banana-3\n" in content
