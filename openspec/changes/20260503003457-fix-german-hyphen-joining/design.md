## Context

The utility's core logic for joining hyphenated words was implemented using a simple regex `[{marks}]\s+`. While effective for basic word splits, it failed to account for German grammar where a hyphen followed by a space often represents a compositional part of a list (e.g., `Luft- und Seefracht`). The current state results in "sticky" words like `Luftund`.

## Goals / Non-Goals

**Goals:**
- Differentiate between word-splitting hyphens (OCR errors) and compositional hyphens (grammatical structures).
- Support both intra-line and cross-line hyphen handling.
- Preserve spaces after hyphens when followed by common conjunctions.
- Prevent accidental joining of standalone dashes.

**Non-Goals:**
- Full linguistic analysis or dictionary-based word verification.
- Handling of every possible language; focus is primarily on German/English common patterns.

## Decisions

### 1. Enhanced Regex with Lookaround Assertions
To identify valid join candidates, we move from a simple character set match to a context-aware pattern:
- **Negative Lookbehind `(?<!\s)`**: Ensures the hyphen is immediately preceded by a character, filtering out standalone dashes or range separators that are preceded by a space.
- **Negative Lookahead `(?!(?:und|oder|sowie|bzw|bis)\b)`**: Excludes common German conjunctions from being joined. If one of these follows the hyphen+space, the hyphen is preserved.

### 2. Multi-Stage Newline Processing
For newlines, a two-step approach is used:
1. **Preservation Pass**: Match hyphens followed by a newline and a conjunction. Replace only the whitespace/newline with a single space, keeping the hyphen.
2. **Joining Pass**: Match all remaining hyphen+newline patterns and remove them entirely.
This ensures that `Luft-\nund` becomes `Luft- und` while `Hy-\nphen` still becomes `Hyphen`.

### 3. Centralized Conjunction List
Define a local `conjunctions` regex variable within `clean_text` to keep the logic readable and easily maintainable if more words need to be added.

## Risks / Trade-offs

- **Risk**: A word split at the end of a line might accidentally match a conjunction on the next line (e.g., `Ab-\nund` where it was meant to be `Abund`).
- **Mitigation**: In German, this is extremely rare as `und` is almost never a suffix. The benefit of fixing the frequent compositional hyphen issue far outweighs this edge case.
- **Trade-off**: Slightly increased regex complexity may impact performance minimally, but given the utility's typical usage on clipboard text, this is negligible.
