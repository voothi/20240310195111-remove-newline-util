import argparse
import pyperclip
import re

def get_clipboard_text():
    return pyperclip.paste()

def set_clipboard_text(text):
    pyperclip.copy(text)

def clean_text(text):
    # Handle the case where &nbsp; and <br> appear together
    cleaned_text = re.sub(r'&nbsp;(<br>|<br>&nbsp;)', ' ', text)
    cleaned_text = re.sub(r'(<br>&nbsp;|<br>)&nbsp;', ' ', cleaned_text)
    # Add a space if there's no other space next to <br>
    cleaned_text = re.sub(r'(?<=<br>)(?!\s)', ' ', cleaned_text)
    # Remove HTML tags
    cleaned_text = re.sub(r'<[^<]+?>', '', cleaned_text)
    # Add a space if there's no other space next to &nbsp
    cleaned_text = re.sub(r'(?<=&nbsp;)(?!\s)', ' ', cleaned_text)
    # Remove special symbols
    cleaned_text = re.sub(r'&\w+;', '', cleaned_text)
    # Remove non-printable characters
    cleaned_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', cleaned_text)
    # Replace multiple spaces with a single space
    cleaned_text = re.sub(r'\s{2,}', ' ', cleaned_text)
    # Remove space before punctuation marks
    cleaned_text = re.sub(r'\s+([:;,.!?])', r'\1', cleaned_text)
    # Remove trailing whitespace
    cleaned_text = cleaned_text.strip()
    return cleaned_text

def combine_clipboard_text():
    clipboard_content = get_clipboard_text()
    # Combine lines and remove line breaks
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