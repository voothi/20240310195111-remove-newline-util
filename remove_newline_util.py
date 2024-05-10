import argparse
import pyperclip
import re

def get_clipboard_text():
    return pyperclip.paste()

def set_clipboard_text(text):
    pyperclip.copy(text)

def remove_newlines(text):
    return re.sub(r'\n', '', text)

def main():
    parser = argparse.ArgumentParser(description="Remove line breaks from clipboard content.")
    args = parser.parse_args()

    clipboard_content = get_clipboard_text()
    clipboard_content_without_newlines = remove_newlines(clipboard_content)
    set_clipboard_text(clipboard_content_without_newlines)

    print("Clipboard content after removing line breaks:")
    print(clipboard_content_without_newlines)

if __name__ == "__main__":
    main()
