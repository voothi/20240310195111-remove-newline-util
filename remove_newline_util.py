import argparse
import pyperclip
import re

def get_clipboard_text():
    return pyperclip.paste()

def set_clipboard_text(text):
    pyperclip.copy(text)

def clean_text(text):
    # Обработка случая, когда &nbsp; и <br> стоят вместе
    cleaned_text = re.sub(r'&nbsp;(<br>|<br>&nbsp;)', ' ', text)
    cleaned_text = re.sub(r'(<br>&nbsp;|<br>)&nbsp;', ' ', cleaned_text)
    # Добавляем пробел, если рядом с <br> нет другого пробела
    cleaned_text = re.sub(r'(?<=<br>)(?!\s)', ' ', cleaned_text)
    # Удаляем HTML теги
    cleaned_text = re.sub(r'<[^<]+?>', '', cleaned_text)
    # Добавляем пробел, если рядом с &nbsp нет другого пробела
    cleaned_text = re.sub(r'(?<=&nbsp;)(?!\s)', ' ', cleaned_text)
    # Удаляем специальные символы типа &nbsp;
    # cleaned_text = re.sub(r'&nbsp;', ' ', cleaned_text)
    # Удаляем специальные символы;
    cleaned_text = re.sub(r'&\w+;', '', cleaned_text)
    # Удаляем непечатаемые символы
    cleaned_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', cleaned_text)
    return cleaned_text

def combine_clipboard_text():
    clipboard_content = get_clipboard_text()
    # Объединяем строки и удаляем переносы строк
    combined_text = ' '.join(clipboard_content.splitlines())
    return combined_text

def main():
    parser = argparse.ArgumentParser(description="Combine and clean clipboard content.")
    args = parser.parse_args()

    clipboard_content = combine_clipboard_text()
    cleaned_content = clean_text(clipboard_content)
    set_clipboard_text(cleaned_content)

    print("Clipboard content after combining, cleaning, and removing line breaks:")
    print(cleaned_content)

if __name__ == "__main__":
    main()
