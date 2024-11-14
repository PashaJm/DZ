import re

def count_words_regex(text):
    """
    Функция для подсчета количества слов в строке с использованием регулярных выражений.

    :param text: Входная строка
    :return: Количество слов в строке
    """
    # Паттерн для слов, включая апострофы и дефисы внутри слов
    pattern = r"\b\w+(?:['-]\w+)*\b"
    words = re.findall(pattern, text)
    return len(words)

# Пример использования
example_text = "It's a well-known fact that well-being is important."
print(f"Количество слов: {count_words_regex(example_text)}")
