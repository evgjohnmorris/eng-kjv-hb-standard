# Changelog

All notable changes to the `eng-kjv-hb-standard` repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to strict **Data Parity** rather than Semantic Versioning, though major structural releases are tagged.

## [Unreleased]

### Added
- Comprehensive logging infrastructure (`scripts/update_manager.py`).
- GitHub Actions CI/CD workflows for integrity checks and automated synchronization (`.github/workflows/`).
- Master `FORMATS.md` definitions file cataloging all 110+ archive types and use-cases.

### Changed
- Refactored `README.md` and `CONTRIBUTING.md` to reflect the industrial-grade omni-format archive paradigm.

## [1.0.0] - Initial Archive Finalization
- Established base SQLite database (`ENG-KJV-HB-STANDARD.db`) with exactly 31,102 verses.
- Generated and synchronized 115 distinct programmatic formats of the 1769 KJV text.
