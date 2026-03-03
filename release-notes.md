
## v1.0.2 (2026-03-03)
**Enhanced Hyphenation & Testing**

- **Feature**: **Support for `¬ ` Hyphenation**. Added support for the logical negation symbol (`¬`) common in OCR text. Now handles sequences like `leuch¬ tet` or `leuch¬\ntet`.
- **Feature**: **Unit Test Suite**. Established a formal testing framework in `tests/` to ensure reliability and prevent regressions in cleaning logic.
- **Improvement**: Optimized internal regex to consistently handle whitespace around hyphenation points.

## v1.0.0 (2026-01-01)
**Initial Release**

- **Feature**: **Smart Clipboard Cleaning**. Automatically joins hyphenated words split across lines (e.g., `betre-\n ten` becomes `betreten`).
- **Feature**: **Newline Normalization**. Replaces all newlines with single spaces to flatten text copied from PDFs or narrow columns.
- **Feature**: **HTML & Symbol Removal**. Strips HTML tags (`<br>`, `<div>`, etc.) and special character entities.
- **Feature**: **Whitespace Optimization**. Normalizes multiple spaces and removes redundant spaces before punctuation marks.
- **Feature**: **Clipboard Integration**. Seamlessly reads from and writes back to the system clipboard.
- **Feature**: **AutoHotkey v2 Integration**. Added support for seamless "Copy-Process-Paste" workflow via `remove-newline.ahk`.
- **Feature**: **Python Execution**. Optimized for direct execution via Python interpreter for integration workflows.
