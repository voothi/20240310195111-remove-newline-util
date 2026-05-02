# intelligent-hyphen-handling Specification

## Purpose
TBD - created by archiving change 20260503003457-fix-german-hyphen-joining. Update Purpose after archive.
## Requirements
### Requirement: Context-Aware Same-Line Hyphen Joining
The system SHALL only join hyphenated words on the same line if the hyphen is immediately preceded by a non-whitespace character and is NOT followed by a common German conjunction (`und`, `oder`, `sowie`, `bzw`, `bis`).

#### Scenario: Join standard OCR split
- **WHEN** the text contains `hy- phenation` (hyphen followed by space)
- **THEN** the system SHALL remove both the hyphen and the space to produce `hyphenation`

#### Scenario: Preserve German compositional hyphen
- **WHEN** the text contains `Luft- und See`
- **THEN** the system SHALL preserve the hyphen and the space

#### Scenario: Preserve standalone dash
- **WHEN** the text contains `Value - Test` (space before hyphen)
- **THEN** the system SHALL preserve the hyphen and the space

### Requirement: Intelligent Newline Hyphen Handling
The system SHALL distinguish between word splits and compositional hyphens at the end of a line. If a hyphenated word break is followed by a common German conjunction, the system SHALL preserve the hyphen and replace the newline with a single space. Otherwise, it SHALL join the parts by removing both the hyphen and the newline.

#### Scenario: Preserve cross-line compositional hyphen
- **WHEN** the text contains `See-, Luft-\nund Landtransport`
- **THEN** the system SHALL replace the newline with a space resulting in `See-, Luft- und Landtransport`

#### Scenario: Join cross-line word split
- **WHEN** the text contains `Hy-\nphenation`
- **THEN** the system SHALL remove both the hyphen and the newline resulting in `Hyphenation`

