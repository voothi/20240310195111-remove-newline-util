import argparse
import pyperclip
import re
import configparser
import os

def load_config():
    """Loads configuration from config.ini."""
    config = {
        'hyphenation_marks': '-¬',
        'join_same_line_hyphens': True,
        'collapse_multiple_spaces': True
    }
    
    config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
    if os.path.exists(config_file):
        cp = configparser.ConfigParser()
        try:
            cp.read(config_file, encoding='utf-8')
            if 'Cleaning' in cp:
                section = cp['Cleaning']
                config['hyphenation_marks'] = section.get('hyphenation_marks', config['hyphenation_marks'])
                config['join_same_line_hyphens'] = section.getboolean('join_same_line_hyphens', config['join_same_line_hyphens'])
                config['collapse_multiple_spaces'] = section.getboolean('collapse_multiple_spaces', config['collapse_multiple_spaces'])
        except Exception as e:
            print(f"Warning: Could not read config.ini: {e}")
            
    return config

def get_clipboard_text():
    """Gets text from the clipboard."""
    return pyperclip.paste()

def set_clipboard_text(text):
    """Puts text into the clipboard."""
    pyperclip.copy(text)

def clean_text(text, config=None):
    """
    Cleans the text: handles word hyphenation, removes HTML tags,
    extra spaces, and other unnecessary characters.
    """
    if config is None:
        config = load_config()

    marks = re.escape(config['hyphenation_marks'])

    # 1. Handle hyphenated word breaks.
    # This command looks for a hyphen/configured mark followed by optional whitespace and a newline,
    # and removes them, joining the parts of the word.
    cleaned_text = re.sub(fr'[{marks}]\s*\n\s*', '', text)
    
    # Also handle the case where the symbol is present but followed by a space on the same line,
    # if it's clearly intended as a hyphen (common in some PDF extractions).
    if config['join_same_line_hyphens']:
        cleaned_text = re.sub(fr'[{marks}]\s+', '', cleaned_text)

    # 2. Replace remaining newlines with spaces.
    # This will join lines that were not part of a word break.
    cleaned_text = re.sub(r'\n', ' ', cleaned_text)
    
    # 3. The following are original cleaning rules.
    # Handle cases where   and <br> appear together
    cleaned_text = re.sub(r' (<br>|<br> )', ' ', cleaned_text)
    cleaned_text = re.sub(r'(<br> |<br>) ', ' ', cleaned_text)
    # Add a space if there's no other space next to <br>
    cleaned_text = re.sub(r'(?<=<br>)(?!\s)', ' ', cleaned_text)
    # Remove HTML tags
    cleaned_text = re.sub(r'<[^<]+?>', '', cleaned_text)
    # Add a space if there's no other space next to  
    cleaned_text = re.sub(r'(?<= )(?!\s)', ' ', cleaned_text)
    # Remove special symbols
    cleaned_text = re.sub(r'&\w+;', '', cleaned_text)
    # Remove non-printable characters
    cleaned_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', cleaned_text)
    
    # Replace multiple spaces with a single space
    if config['collapse_multiple_spaces']:
        cleaned_text = re.sub(r'\s{2,}', ' ', cleaned_text)
        
    # Remove space before punctuation marks
    cleaned_text = re.sub(r'\s+([:;,.!?])', r'\1', cleaned_text)
    # Remove leading/trailing whitespace
    cleaned_text = cleaned_text.strip()
    
    return cleaned_text

def main():
    parser = argparse.ArgumentParser(description="Combine and clean clipboard content.")
    args = parser.parse_args()
    
    # Load configuration
    config = load_config()
    
    # Get the original text from the clipboard
    clipboard_content = get_clipboard_text()
    
    # Pass it directly to the updated cleaning function
    cleaned_content = clean_text(clipboard_content, config)
    
    # Copy the result back to the clipboard
    set_clipboard_text(cleaned_content)
    
    print("Clipboard content after combining, cleaning, and removing line breaks:")
    print(cleaned_content)

if __name__ == "__main__":
    main()