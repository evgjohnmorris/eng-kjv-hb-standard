# Contributing to ENG-KJV-HB-STANDARD

First and foremost, thank you for considering contributing to the `eng-kjv-hb-standard` archive. This repository acts as the central, industrial-grade distribution layer for the English King James Version Bible.

Given the omni-format nature of this repository, our contributing guidelines are highly rigorous to ensure that out of the 110+ formats supported, none fall out of sync, truncate data, or suffer from schema degradation.

## 1. System Philosophy: Absolute Parity

The core operating principle of this repository is **Absolute Data Parity**. 

Because this repository provides the Bible in everything from `sqlite3` and `json` to `COBOL`, `Zarr`, and `DICOM` (for theoretical testing), a single typo fix in the master text requires regeneration of the *entire* archive. 
- You MUST NOT edit a single leaf file manually (e.g., do not submit a PR changing `GEN 1:1` in `json/ENG-KJV-HB-STANDARD.json` only).
- All fixes must target the Master Data Generator script (maintained externally) or point out systemic schema flaws so the entire suite can be recompiled deterministically.

## 2. Reporting Issues

If you find a data anomaly, please submit an Issue with the following technical details:

1. **Affected Format(s)**: Which extension(s) did you find the issue in?
2. **Canonical Index**: Provide the Book, Chapter, and Verse (e.g., `JHN 3:16`).
3. **Encoding Issue vs. Schema Issue**: Specify if the issue is a text encoding error (e.g., a broken UTF-8 byte) or a structural schema error (e.g., missing primary key `id`).
4. **Environment**: If a database format (like `.db` or `.arrow`) failed to load, provide your driver, library version, and OS.

## 3. Proposing New Formats

We currently support over 110 distinct file extensions, including legacy mainframe data types, markup languages, scientific analytical arrays, and strict relational dumps. 

If you wish to propose a new format to be added to the suite:
- Provide a technical specification of the proposed format.
- Explain the specific industrial, scientific, or software engineering use case.
- Note any schema limitations (e.g., "Format X does not support integers larger than 16-bit, so absolute IDs over 32,000 will overflow").

## 4. Submitting Pull Requests

If you are modifying the dataset directly or submitting scripts for the generation pipeline:

1. **Fork the repository** and create a branch.
2. **Prefix Rules**: All root dataset files and major folders MUST carry the `ENG-KJV-HB-STANDARD` naming prefix.
3. **No Schema Pollution**: Ensure that integer fields (chapter, verse, absolute ID) remain strictly integers and do not get cast to strings, as this breaks downstream static typing in compiled languages like Go, Rust, and C#.
4. **Validating Edits**: If you contribute a script to correct data across all formats, you must write a deterministic test that asserts the exact verse count (`31102`) across all generated tables and files.

## 5. Theological & Textual Integrity

We treat the source text as an immutable dataset. We strictly follow the 1769 Oxford standard text of the KJV. Pull Requests attempting to alter the translation base, "modernize" the English, or insert commentary will be rejected. This repository is purely structural and architectural.

Thank you for contributing to the preservation and technical proliferation of the Scripture.
