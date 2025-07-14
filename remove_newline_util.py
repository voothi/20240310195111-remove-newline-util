import argparse
import pyperclip
import re

def get_clipboard_text():
    """Получает текст из буфера обмена."""
    return pyperclip.paste()

def set_clipboard_text(text):
    """Помещает текст в буфер обмена."""
    pyperclip.copy(text)

def clean_text(text):
    """
    Очищает текст: обрабатывает переносы слов, удаляет HTML-теги,
    лишние пробелы и другие ненужные символы.
    """
    # 1. Обрабатываем перенос слов с дефисом.
    # Эта команда ищет дефис, за которым могут следовать пробелы и перенос строки,
    # и удаляет их, соединяя части слова.
    # Пример: "betre-\n ten" станет "betreten".
    cleaned_text = re.sub(r'-\s*\n\s*', '', text)

    # 2. Заменяем оставшиеся переносы строк на пробелы.
    # Это объединит строки, которые не были частью переноса слова.
    cleaned_text = re.sub(r'\n', ' ', cleaned_text)
    
    # 3. Далее идут ваши оригинальные правила очистки.
    # Обработка случаев, когда   и <br> появляются вместе
    cleaned_text = re.sub(r' (<br>|<br> )', ' ', cleaned_text)
    cleaned_text = re.sub(r'(<br> |<br>) ', ' ', cleaned_text)
    # Добавляем пробел, если после <br> нет другого пробела
    cleaned_text = re.sub(r'(?<=<br>)(?!\s)', ' ', cleaned_text)
    # Удаление HTML-тегов
    cleaned_text = re.sub(r'<[^<]+?>', '', cleaned_text)
    # Добавляем пробел, если после   нет другого пробела
    cleaned_text = re.sub(r'(?<= )(?!\s)', ' ', cleaned_text)
    # Удаление специальных символов
    cleaned_text = re.sub(r'&\w+;', '', cleaned_text)
    # Удаление непечатаемых символов
    cleaned_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', cleaned_text)
    # Замена нескольких пробелов одним
    cleaned_text = re.sub(r'\s{2,}', ' ', cleaned_text)
    # Удаление пробелов перед знаками препинания
    cleaned_text = re.sub(r'\s+([:;,.!?])', r'\1', cleaned_text)
    # Удаление пробелов в начале и конце строки
    cleaned_text = cleaned_text.strip()
    
    return cleaned_text

def main():
    parser = argparse.ArgumentParser(description="Объединение и очистка содержимого буфера обмена.")
    args = parser.parse_args()
    
    # Получаем оригинальный текст из буфера обмена
    clipboard_content = get_clipboard_text()
    
    # Передаем его напрямую в обновленную функцию очистки
    cleaned_content = clean_text(clipboard_content)
    
    # Копируем результат обратно в буфер обмена
    set_clipboard_text(cleaned_content)
    
    print("Содержимое буфера обмена после объединения, очистки и удаления переносов строк:")
    print(cleaned_content)

if __name__ == "__main__":
    main()