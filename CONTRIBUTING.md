# Contributing

Contributions are welcome.

This repository is designed to remain lightweight, practical, and consistent. Before submitting a new guide or update, please review the editorial standards in `docs/editorial-standards.md`.

## What makes a strong contribution

A strong contribution should:

- Improve clarity, accuracy, or usefulness
- Avoid promotional language
- Use neutral and respectful wording
- Distinguish stable information from information that changes frequently
- Prefer official sources where possible
- Keep guide structure consistent
- Avoid overloading guides with personal opinion

## Adding a country guide

1. Copy `templates/country-guide-template.md`.
2. Save it under `guides/countries/` using a lowercase hyphenated filename.
3. Complete the required sections.
4. Add official sources where appropriate.
5. Run the validation script.

Example:

```bash
cp templates/country-guide-template.md guides/countries/portugal.md
python scripts/validate_guides.py
```

## Adding a city guide

1. Copy `templates/city-guide-template.md`.
2. Save it under `guides/cities/` using the format `city-country.md`.
3. Complete the required sections.
4. Run the validation script.

Example:

```bash
cp templates/city-guide-template.md guides/cities/lisbon-portugal.md
python scripts/validate_guides.py
```

## Source expectations

Use official sources for:

- Entry rules
- Visa and immigration information
- Public health information
- Travel advisories
- Public transportation agencies
- Currency and government services

Use non-official sources carefully for context, local insight, or practical travel planning. Do not present forum comments, outdated blog posts, or commercial pages as authoritative.

## Pull request checklist

Before opening a pull request, confirm that:

- The guide follows the correct template
- The guide is written in a neutral tone
- Critical claims are source-aware
- The validation script passes
- The content does not include affiliate links or promotional placement
- The guide remains useful without requiring the reader to visit a commercial service
