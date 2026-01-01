# Remove Newline Utility

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](https://github.com/voothi/20240310195111-remove-newline-util)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight utility for cleaning and formatting text from the clipboard, specifically designed to fix issues with line breaks and hyphenated words in copied text.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Kardenwort](#kardenwort)
- [License](#license)

---

## Description
`remove-newline-util` is a focused tool that processes the current clipboard content. It is particularly useful when copying text from documents where words are split with hyphens at the end of lines, or when text is formatted in columns that introduce unwanted line breaks.

[Return to Top](#remove-newline-utility)

## Features
- **Smart Hyphenation Handling**: Joins words split by hyphens and newlines (e.g., `word-\n break` → `wordbreak`).
- **Flatten Text**: Replaces all internal newlines with single spaces.
- **HTML Cleanup**: Removes HTML tags and special entities often found in clipboard content from web or OCR sources.
- **Smart Spacing**: Normalizes multiple spaces and ensures proper spacing around punctuation.
- **Fast Execution**: Designed to be run as a quick background utility.

[Return to Top](#remove-newline-utility)

## Installation

### From Source
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install pyperclip
   ```
3. Run the script:
   ```bash
   python remove_newline_util.py
   ```

### Standalone Executable
You can find pre-built executables in the `dist/` folder or under the Releases section.

[Return to Top](#remove-newline-utility)

## Usage

1. **Copy** the messy text to your clipboard.
2. **Execute** `remove_newline_util.exe` (or the script).
3. **Paste** the cleaned text into your destination.

The terminal will display the cleaned content for quick verification.

[Return to Top](#remove-newline-utility)

## Kardenwort Ecosystem

This project is part of the **[Kardenwort](https://github.com/kardenwort)** environment, designed to create a focused and efficient learning ecosystem.

[Return to Top](#table-of-contents)

## License
MIT License. See LICENSE file for details.

[Return to Top](#remove-newline-utility)
