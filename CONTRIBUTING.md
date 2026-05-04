# Contributing to ENG-KJV-HB-STANDARD

First off, thank you for considering contributing to the `eng-kjv-hb-standard` project. It's people like you that make this industrial-grade archive a powerful tool for developers, theologians, and researchers everywhere.

## How to Contribute

### 1. Reporting Issues
If you find a missing verse, a character encoding error, or an inconsistency in the database schemas, please open an issue! Be sure to include:
- The file type and exact path (e.g., `json/ENG-KJV-HB-STANDARD.openapi.json`).
- The specific Book, Chapter, and Verse where the anomaly was found.
- The behavior you expected.

### 2. Suggesting New Formats
Have an idea for a new data format? We currently support over 100 extensions, but we are always looking to expand. Open an issue proposing the format, its standard use case, and how it benefits the wider community.

### 3. Submitting Pull Requests
If you are contributing code (e.g., Python scripts for parsing, new data dumps):
1. **Fork the repository** and create your branch from `main`.
2. **Adhere to the naming conventions:** Any new dataset must be prefixed with `ENG-KJV-HB-STANDARD`.
3. **Validate your data:** Ensure that no verses have been dropped and that text encoding strictly adheres to UTF-8.
4. **Update Documentation:** If you add a new subfolder or format, please add a brief note to the `README.md`.
5. Open a Pull Request with a clear description of the problem you've solved.

## Our Philosophy
We treat scripture as an immutable, sacred dataset. Our goal is to prevent "type pollution", data gaps, and format decay. Every PR should prioritize data integrity, deterministic outputs, and high-quality standardization.

Thank you for helping us preserve and distribute the Word!
