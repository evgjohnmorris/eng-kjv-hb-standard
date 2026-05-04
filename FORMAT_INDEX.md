# Comprehensive Format Index

The `ENG-KJV-HB-STANDARD` archive historically included over 100 specialized data formats to ensure maximum interoperability across any computational domain. While the core repository now strictly focuses on the "Foundational Triad" (SQLite, CSV, and Plaintext), this index serves as the encyclopedic record of all supported extensions, structural variants, and their specific engineering uses.

## 1. Core Foundational Formats (Active)
| Format | Extension | Primary Use Case |
| :--- | :--- | :--- |
| **Relational Database** | `.db`, `.db-shm`, `.db-wal` | High-concurrency mobile apps, API backends, and production SQL deployments. |
| **Tabular Data** | `.csv` | Data science, Pandas ingestion, statistical NLP, and spreadsheet analysis. |
| **UTF-8 Plaintext** | `.txt` | Unix text processing (`grep`, `awk`), corpus linguistics, and legacy compatibility. |

## 2. Specialized Software & Game Engines
| Format | Extension | Primary Use Case |
| :--- | :--- | :--- |
| **Unreal Engine** | `.unreal.csv` | Direct ingestion into Unreal Engine `UDataTable` for video game development. |
| **Godot Engine** | `.tscn` | Pre-configured Godot scene files containing the biblical corpus. |
| **Unity3D** | `.unity.asset` | Unity ScriptableObjects for immediate drag-and-drop game integration. |
| **PICO-8** | `.p8` | Fantasy console cartridge data for 8-bit game development. |

## 3. Bible & Worship Presentation Software
| Format | Extension | Primary Use Case |
| :--- | :--- | :--- |
| **OSIS XML** | `.osis.xml` | Open Scripture Information Standard; the definitive format for Bible software. |
| **Zefania XML** | `.zefania.xml` | Modular XML format used by popular desktop Bible readers. |
| **MyBible** | `.mybible` | SQLite-based format for the MyBible mobile application. |
| **OpenLP** | `.openlp.v3` | Worship presentation software database format for church projection. |
| **Quelea** | `.quelea.xml` | Church projection software XML schema. |
| **USFM** | `.usfm` | Unified Standard Format Markers for Bible translation and publishing. |

## 4. Machine Learning & Big Data
| Format | Extension | Primary Use Case |
| :--- | :--- | :--- |
| **Apache Arrow** | `.arrow` | High-performance columnar memory format for Big Data processing. |
| **Hugging Face JSONL** | `.hf.jsonl` | Instruction-tuning datasets for Large Language Models (LLMs). |
| **NumPy Archives** | `.npz` | Tokenized vector embeddings for PyTorch/TensorFlow ingestion. |
| **HDF5** | `.h5` | Hierarchical Data Format for massive scientific computing datasets. |

## 5. Web, API, and Networking
| Format | Extension | Primary Use Case |
| :--- | :--- | :--- |
| **GraphQL** | `.graphql.json` | Pre-computed JSON payloads for GraphQL endpoints. |
| **OpenAPI** | `.openapi.json` | Swagger/OpenAPI compliant REST specifications. |
| **Postman** | `.postman_collection.json` | Postman collections for rapid API endpoint testing. |
| **Protocol Buffers** | `.pb` | Highly compressed gRPC serialization payloads. |
| **MessagePack** | `.msgpack` | Efficient binary serialization format. |
| **Redis** | `.redis` | Bulk Redis cache ingestion commands (`redis-cli --pipe`). |

## 6. Document, Publishing, and Academic
| Format | Extension | Primary Use Case |
| :--- | :--- | :--- |
| **InDesign Tagged Text** | `.indesign.txt` | Automated typesetting for print publishing in Adobe InDesign. |
| **TeX / LaTeX** | `.tex` | Academic and mathematical typesetting. |
| **EPUB** | `.epub` | Standardized e-reader publication format. |
| **Docx / PDF** | `.docx`, `.pdf` | Standard consumer document formats. |
| **TEI XML** | `.tei.xml` | Text Encoding Initiative standard for digital humanities. |
| **BibTeX / RIS** | `.bib`, `.ris` | Academic citation management formats. |

## 7. Programming Languages & Code Assets
| Format | Extension | Primary Use Case |
| :--- | :--- | :--- |
| **Go** | `.go` | Pre-compiled Go slices/maps for static binary inclusion. |
| **Rust** | `.rs` | Rust vectors and arrays for zero-dependency execution. |
| **TypeScript/JS** | `.ts`, `.js` | TypeScript definitions and JSON exports for Node.js/React. |
| **Java** | `.java` | Java class strings for Android or enterprise development. |
| **C#** | `.cs` | C# constants for Unity or .NET applications. |
| **C / C++** | `.h` | Header files for embedded systems or low-level parsing. |
| **Swift** | `.swift` | Swift arrays for native iOS app development. |
| **Kotlin** | `.kt` | Kotlin data classes for Android development. |

## 8. Niche, Industrial, and Legacy
| Format | Extension | Primary Use Case |
| :--- | :--- | :--- |
| **EBCDIC / PETSCII** | `_ebcdic.txt`, `_petscii.txt` | Mainframe (IBM) and Commodore 64 legacy character encodings. |
| **Modbus** | `.modbus.csv` | Industrial control systems (SCADA/PLC) holding register maps. |
| **NMEA** | `.nmea` | GPS protocol sentence injection for maritime/aviation spoofing. |
| **G-Code** | `.gcode` | CNC machining and 3D printing toolpaths (engraving the text). |
| **MIDI / MusicXML** | `.mid`, `.musicxml` | Algorithmic musical sonification of the biblical text. |
| **DICOM / HL7** | `.dcm`, `.hl7` | Healthcare and medical imaging data container encapsulation. |
| **X12 / EDI** | `.x12`, `.edi` | Electronic Data Interchange for corporate logistics. |

---
*Note: Due to file-size limitations and repository cloning speeds, the master branch maintains only the Core Foundational Formats. The specialized extensions listed above can be procedurally generated from the core `.db` using the repository's build pipelines.*
