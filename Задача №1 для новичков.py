import string

def analyze_text(text):
    # Приведение текста к нижнему регистру и удаление знаков препинания
    text = text.lower().translate(str.maketrans('', '', string.punctuation))

    # Разбиение текста на слова
    words = text.split()

    # Создание словаря для подсчета частоты слов
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Сортировка слов по частоте и алфавитному порядку
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    # Вывод результата
    for word, count in sorted_words:
        print(f'{word}: {count}')

# Ввод текста от пользователя
user_text = input("Введите текст для анализа: ")

# Вызов функции для анализа текста
analyze_text(user_text)
