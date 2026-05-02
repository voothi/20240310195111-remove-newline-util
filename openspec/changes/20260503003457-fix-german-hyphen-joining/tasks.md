## 1. Script Refactoring

- [ ] 1.1 Define the common German conjunctions regex variable within `clean_text`.
- [ ] 1.2 Implement the two-stage newline hyphen processing: preservation of compositional hyphens followed by joining of word splits.
- [ ] 1.3 Update the intra-line hyphen joining logic to use lookbehind for word context and lookahead for conjunction exclusion.

## 2. Verification and Testing

- [ ] 2.1 Verify that same-line compositional hyphens (e.g., `Luft- und`) are correctly preserved.
- [ ] 2.2 Verify that cross-line compositional hyphens (e.g., `Luft-\nund`) are correctly preserved as `Luft- und`.
- [ ] 2.3 Verify that standard word splits (e.g., `Hy-\nphenation`) are still correctly joined into a single word.
- [ ] 2.4 Verify that standalone dashes (e.g., `Value - Test`) are not accidentally joined.
