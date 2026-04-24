# Class Teacher Skills

This folder contains two complementary teacher-facing skills:

- `class-assistant/` — operational homeroom-teacher workflow skill
- `class-teacher-market-scan/` — background scan of local skill coverage, market landscape, and memtensor validation notes

## Why split them?

Because mixing market notes, infrastructure verification, and actual classroom workflows into one skill is messy.

- `class-assistant` is the thing you actually use.
- `class-teacher-market-scan` explains what exists, what doesn't, and what has already been validated locally.

## GitHub hygiene

Before publishing:

- keep tokens, passwords, session keys, and personal identifiers out of the repo
- avoid committing real student data
- prefer templates and sanitized examples over production records
- document local-only assumptions in each skill's `SKILL.md`
