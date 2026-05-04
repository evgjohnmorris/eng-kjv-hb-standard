# ENG-KJV-HB-STANDARD

**ENG-KJV-HB-STANDARD** is an open-source, industrial-grade digital archive of the 1769 Standard Text of the English King James Version (KJV) Bible. First established to address the fragmentation and technical inconsistencies found in modern digital biblical texts, the archive provides the complete corpus of the KJV in three foundational data formats: Relational SQLite, Delimited CSV, and UTF-8 Plaintext. 

The repository is widely noted for its strict adherence to absolute data parity, zero-truncation policies, and deterministic output, ensuring that the biblical text can be seamlessly integrated into modern computing environments, machine learning pipelines, and enterprise databases without data friction.

---

## Quick Facts

| Parameter | Detail |
| :--- | :--- |
| **Language** | Early Modern English (eng) |
| **Text Source** | 1769 Blayney Oxford Standard (King James Version) |
| **Total Verses** | 31,102 |
| **Primary Formats** | SQLite (`.db`), CSV (`.csv`), Plaintext (`.txt`) |
| **License** | Public Domain (outside UK Crown Copyright) |
| **Encoding** | UTF-8 |

---

## History and Background

The King James Version of the Bible was originally published in 1611, but the text underwent standardizations over the centuries. The 1769 edition, edited by Benjamin Blayney at Oxford, became the de facto standard text used by most publishers. 

In the digital age, biblical texts were frequently digitized in ad-hoc, inconsistent formats. Developers and data scientists often faced "data friction" when attempting to ingest biblical texts due to irregular character encodings, truncated verses, and inconsistent structural paradigms. The `eng-kjv-hb-standard` project was initiated to create a single, canonical repository that adhered to strict software engineering and data science principles, eliminating the need for secondary parsers or text cleaning.

## Architecture and Core Formats

To ensure maximum utility without unnecessary bloat, the archive was streamlined from a highly fragmented multi-format ecosystem into a core triplet of foundational data structures. This triad allows for maximum interoperability across all computational domains.

### Relational Database (`.db`)
The core of the archive is a highly concurrent SQLite3 database. The database is distributed with `-wal` (Write-Ahead Logging) and `-shm` (Shared Memory) files enabled, making it production-ready for immediate deployment in mobile applications or API backends. The schema features a canonical `verses` table mapped by absolute canonical verse index, book string, and chapter/verse integers.

### Tabular Data (`.csv`)
For data science, statistical Natural Language Processing (NLP), and spreadsheet ingestion, the archive maintains a Comma-Separated Values dataset. This format is heavily utilized by machine learning engineers for direct integration into foundation model training loaders.

### Plaintext (`.txt`)
A strictly normalized UTF-8 plaintext file serves as the archival backbone of the repository. It is designed for maximum compatibility with legacy systems, Unix text processing tools (like `grep` and `awk`), and long-term digital preservation.

## Maintenance and Integrity Philosophy

The repository is maintained under a philosophy of absolute data integrity, managed via Continuous Integration and Continuous Deployment (CI/CD) pipelines.

1. **Zero Truncation**: The project enforces a strict policy that no book, chapter, or verse is dropped, regardless of special characters, length, or formatting anomalies.
2. **Deterministic Parity**: The three formats are generated deterministically. If a typographical error is corrected in the master index, the CI/CD pipeline enforces an automated regeneration of the DB, CSV, and TXT formats simultaneously to prevent version drift.
3. **Strict Typing**: The `verse` field is strictly typed as an integer in the database schema. Complex edge cases, such as omitted or combined verses found in other translations, are standardized according to strict SQL and schema paradigms to prevent "Type Pollution."

## Production Use Cases

* **Software Development**: Front-end and back-end developers utilize the SQLite database for rapid application bootstrapping, allowing them to instantly query biblical texts without writing custom ingestion pipelines.
* **Artificial Intelligence**: The tabular formats are used to fine-tune Large Language Models (LLMs), bypassing standard text extraction friction.
* **Corpus Linguistics**: Researchers perform static analysis on the plaintext corpus for historical linguistic studies and pattern matching.

## See Also

* [King James Version](https://en.wikipedia.org/wiki/King_James_Version)
* [Biblical software](https://en.wikipedia.org/wiki/Bible_software)
* [Digital humanities](https://en.wikipedia.org/wiki/Digital_humanities)

## External Links

* [Official Repository Workflow (`.github/workflows`)](./.github/workflows)
* [Repository Changelog](./CHANGELOG.md)
