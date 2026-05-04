# country-guides

Lightweight country and city guide markdowns for travelers, solo travelers, digital nomads, researchers, and open knowledge projects.

`country-guides` is a Markdown-first repository for practical, structured, maintainable travel reference guides. It is designed to be easy to read, easy to fork, easy to cite, and easy to reuse across websites, newsletters, knowledge bases, datasets, and travel planning tools.

## Purpose

Travel information often becomes scattered across blog posts, government websites, forums, review platforms, and commercial booking pages. This repository offers a simple alternative: concise, consistent, source-aware Markdown guides that can be reviewed, improved, and reused over time.

The goal is not to replace official travel advice, local expertise, or current safety notices. The goal is to create a dependable editorial layer that helps readers understand a destination before they make more specific decisions.

## What is included

- Country guide templates
- City guide templates
- Production-grade sample country guides
- Production-grade sample city guides
- Editorial standards
- Source and maintenance guidance
- Validation script for guide structure
- Contribution guidelines
- GitHub Actions workflow for validation

## Repository structure

```text
country-guides/
├── guides/
│   ├── countries/
│   │   ├── canada.md
│   │   ├── france.md
│   │   └── japan.md
│   └── cities/
│       ├── toronto-canada.md
│       ├── paris-france.md
│       └── tokyo-japan.md
├── templates/
│   ├── country-guide-template.md
│   └── city-guide-template.md
├── docs/
│   ├── data-sources.md
│   ├── editorial-standards.md
│   ├── maintenance.md
│   └── publishing.md
├── scripts/
│   └── validate_guides.py
├── .github/
│   └── workflows/
│       └── validate.yml
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── CHANGELOG.md
```

## Guide philosophy

Each guide should be:

- Practical without pretending to be exhaustive
- Clear without being simplistic
- Neutral without being generic
- Useful to first-time visitors and repeat travelers
- Respectful of local communities and cultures
- Easy to update as conditions change

## Guide categories

Country guides cover broad destination context, including entry considerations, transportation, safety, money, connectivity, accessibility, health, etiquette, seasonal planning, and useful official sources.

City guides focus on arrival logistics, neighborhoods, local transport, solo travel considerations, work-friendly infrastructure, day trips, food culture, accessibility, and practical planning notes.

## Validation

Run the validation script from the repository root:

```bash
python scripts/validate_guides.py
```

The script checks that each guide contains the expected front matter and required headings.

## Suggested use cases

- Travel knowledge bases
- Country and city reference pages
- Static websites
- Open data and open knowledge projects
- Solo travel planning resources
- Digital nomad destination research
- Newsletter research notes
- Lightweight internal editorial systems

## Disclaimer

These guides are informational and should not be treated as legal, medical, immigration, tax, safety, or financial advice. Travelers should verify critical details with official sources before making decisions.

## License

This project is licensed under Creative Commons Zero v1.0 Universal. See `LICENSE` for details.
