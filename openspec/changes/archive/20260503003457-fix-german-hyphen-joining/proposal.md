## Why

The utility's hyphen-joining logic was too aggressive, incorrectly collapsing German compositional hyphens (like `Luft- und`) and accidental matches with dashes. This caused text corruption in multilingual contexts where hyphens are part of grammatical structures rather than just word splits.

## What Changes

- **Intelligent Hyphen Handling**: Updated the cleaning engine to distinguish between word splits (intended for joining) and compositional hyphens or dashes (intended for preservation).
- **Conjunction Awareness**: The logic now excludes common German conjunctions (`und`, `oder`, `sowie`, `bzw`, `bis`) from being joined.
- **Dash Protection**: Prevents joining when a hyphen is preceded by a space, correctly identifying it as a dash or range separator.
- **Consistent Newline Processing**: Applies the same "smart" joining logic to hyphens at the end of a line, ensuring `Luft-\nund` becomes `Luft- und` instead of `Luftund`.

## Capabilities

### New Capabilities
- `intelligent-hyphen-handling`: Logic to intelligently process hyphens during newline removal and same-line cleaning to preserve grammatical meaning.

### Modified Capabilities
<!-- Empty -->

## Impact

- **Core Logic**: Modifies the `clean_text` function in `remove_newline_util.py`.
- **Regex engine**: Introduces lookbehind and lookahead assertions for more precise character matching.
- **Accuracy**: Significantly improves processing quality for German and other languages using compositional hyphens.
