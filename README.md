# ENG-KJV-HB-STANDARD

> The Omni-Format Polyglot Archive of the English King James Version (KJV) Holy Bible

## Overview

The `eng-kjv-hb-standard` repository is an exhaustive, industrial-grade structured data archive of the 1769 Standard Text of the English King James Version (KJV) Bible. 

Unlike typical repositories that offer the Bible in a single file, this archive programmatically compiles the biblical corpus into the **three core foundational data formats**: Relational SQLite (`.db`), Delimited Tabular (`.csv`), and Plaintext (`.txt`). Our primary objective is providing maximum utility and structural integrity without unnecessary bloat. Whether you are ingesting the text into an enterprise database, analyzing it via data science workflows, or simply reading the text, this repository provides the exact canonical data structure.

Every file strictly adheres to the `ENG-KJV-HB-STANDARD` naming convention and maintains absolute data parity, ensuring no truncated chapters, missing verses, or corrupted character encodings across formats.

---

## Technical Schema Parity

At the core of the archive is a rigorously defined structural schema. Across all serialized and relational formats, the fundamental data unit representing a single verse is structured as follows:

```sql
CREATE TABLE verses (
    id INTEGER PRIMARY KEY,   -- Absolute canonical verse index (1 to 31102)
    book_code TEXT,           -- 3-Letter Book Identifier (e.g., 'GEN', 'EXO', 'REV')
    book_name TEXT,           -- Full Book String (e.g., 'Genesis', 'Revelation')
    chapter INTEGER,          -- Chapter Integer
    verse INTEGER,            -- Verse Integer
    text TEXT                 -- The raw text strictly normalized to UTF-8
);
CREATE INDEX idx_ref ON verses (book_code, chapter, verse);
```

---

## Exhaustive Format Index

This archive focuses entirely on three fundamental formats:

### 1. Relational Database (`db/`)
* **SQLite3 Database** with `-wal` and `-shm` enabled for high concurrency.
* Contains the absolute canonical representation of the text.

### 2. Tabular Data (`csv/`)
* **Comma-Separated Values** (`.csv`) for basic data science, spreadsheet ingestion, and statistical NLP tools.

### 3. Plaintext (`txt/`)
* **UTF-8 Encoded Plaintext** (`.txt`) for maximum compatibility, Unix text processing, and archival preservation.

---

## Production Use Cases

### Immediate App Bootstrapping
Rather than parsing raw text, a developer can immediately connect to the `ENG-KJV-HB-STANDARD.db` file to serve verses via an API or mobile app backend.

### Large Language Model (LLM) Fine-Tuning
Machine Learning engineers can bypass text extraction and load the `csv` formats into a dataset loader for foundation model training.

### Static Analysis
Researchers can run standard Unix `grep`/`awk` pipelines on the `txt` files for rapid pattern matching and corpus linguistics.

---

## Maintenance & Integrity Philosophy

1. **Zero Truncation**: No book, chapter, or verse is dropped due to special characters or length.
2. **Deterministic Output**: If a typo is found in the master index, all 3 formats must be regenerated via the CI/CD pipeline to ensure strict 1-to-1 data parity.
3. **No 'Type Pollution'**: The `verse` integer field is strictly typed as an integer. Edge cases (like omitted verses or split verses) are handled strictly to standard SQL and Schema paradigms.

## License

The King James Version text is in the public domain in most of the world (excluding UK Crown Copyright restrictions). All programmatic schemas, structured architectures, and data conversion outputs within this repository are released to the public domain and available for uninhibited open-source usage.
