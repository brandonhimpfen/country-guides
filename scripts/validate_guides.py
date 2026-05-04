#!/usr/bin/env python3
"""Validate country-guides Markdown files.

This script intentionally avoids third-party dependencies so it can run in
simple CI environments and local editorial workflows.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COUNTRY_DIR = ROOT / "guides" / "countries"
CITY_DIR = ROOT / "guides" / "cities"

REQUIRED_FRONT_MATTER_KEYS = [
    "title",
    "last_reviewed",
    "status",
]

COUNTRY_REQUIRED_HEADINGS = [
    "# Country Guide:",
    "## Overview",
    "## Quick Facts",
    "## Entry and Visas",
    "## Safety and Risk Context",
    "## Transportation",
    "## Money and Payments",
    "## Connectivity and Remote Work",
    "## Health and Accessibility",
    "## Culture and Etiquette",
    "## Seasonal Planning",
    "## Solo Travel Notes",
    "## Digital Nomad Notes",
    "## Suggested Cities and Regions",
    "## Common Planning Mistakes",
    "## Useful Official Sources",
    "## Maintenance Notes",
]

CITY_REQUIRED_HEADINGS = [
    "# City Guide:",
    "## Overview",
    "## Quick Facts",
    "## Arrival and Orientation",
    "## Neighborhoods and Areas",
    "## Local Transportation",
    "## Accommodation Strategy",
    "## Food and Daily Life",
    "## Work-Friendly Notes",
    "## Solo Travel Notes",
    "## Accessibility Notes",
    "## Budget Notes",
    "## Day Trips and Nearby Places",
    "## Common Planning Mistakes",
    "## Useful Official Sources",
    "## Maintenance Notes",
]

DATE_RE = re.compile(r"last_reviewed:\s*[\"']?\d{4}-\d{2}-\d{2}[\"']?")
STATUS_RE = re.compile(r"status:\s*[\"']?(draft|reviewed|needs-update|archived)[\"']?")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def has_front_matter(text: str) -> bool:
    return text.startswith("---\n") and "\n---\n" in text[4:]


def validate_file(path: Path, required_headings: list[str]) -> list[str]:
    errors: list[str] = []
    text = read_text(path)

    if not has_front_matter(text):
        errors.append("missing YAML-style front matter")

    for key in REQUIRED_FRONT_MATTER_KEYS:
        if f"{key}:" not in text:
            errors.append(f"missing front matter key: {key}")

    if not DATE_RE.search(text):
        errors.append("last_reviewed must use YYYY-MM-DD format")

    if not STATUS_RE.search(text):
        errors.append("status must be one of: draft, reviewed, needs-update, archived")

    for heading in required_headings:
        if heading not in text:
            errors.append(f"missing required heading: {heading}")

    if "# " not in text:
        errors.append("missing H1 title")

    if len(text.strip()) < 1200:
        errors.append("guide appears too short for a production guide")

    return errors


def collect_markdown(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(directory.glob("*.md"))


def main() -> int:
    failures: dict[Path, list[str]] = {}

    country_files = collect_markdown(COUNTRY_DIR)
    city_files = collect_markdown(CITY_DIR)

    if not country_files:
        failures[COUNTRY_DIR] = ["no country guide files found"]

    if not city_files:
        failures[CITY_DIR] = ["no city guide files found"]

    for path in country_files:
        errors = validate_file(path, COUNTRY_REQUIRED_HEADINGS)
        if errors:
            failures[path] = errors

    for path in city_files:
        errors = validate_file(path, CITY_REQUIRED_HEADINGS)
        if errors:
            failures[path] = errors

    if failures:
        print("Guide validation failed.\n")
        for path, errors in failures.items():
            rel = path.relative_to(ROOT) if path.is_absolute() and ROOT in path.parents else path
            print(f"{rel}:")
            for error in errors:
                print(f"  - {error}")
            print()
        return 1

    print(f"Guide validation passed for {len(country_files)} country guides and {len(city_files)} city guides.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
