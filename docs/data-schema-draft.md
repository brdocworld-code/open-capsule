# Open Capsule Data Schema (Draft v0.1)

## Overview
This document defines the metadata structure for cultural artifacts stored in the Open Capsule. The schema is based on **JSON-LD** (JavaScript Object Notation for Linking Data) to ensure interoperability, semantic clarity, and long-term machine readability.

The goal is to capture not just the *data*, but the *context* necessary for a future civilization (or AI) to understand, interpret, and utilize the information.

## Core Principles
1.  **Self-Describing:** Every field should be clear without external documentation.
2.  **Language Agnostic:** Supports any language, with explicit language tagging.
3.  **Redundant:** Critical info is repeated in human-readable and machine-readable forms.
4.  **Extensible:** New fields can be added without breaking old parsers.

## The Schema Structure (JSON-LD)

```json
{
  "@context": "https://open-capsule.org/context/v1",
  "@type": "CulturalArtifact",
  "@id": "urn:uuid:550e8400-e29b-41d4-a716-446655440000",
  
  "metadata": {
    "created": "2026-08-13T14:30:00Z",
    "modified": "2026-08-13T14:30:00Z",
    "version": "1.0",
    "ingestor": "University of Example - Digital Archiving Dept.",
    "license": "CC0-1.0"
  },

  "artifact": {
    "title": {
      "en": "Global Climate Accord 2026",
      "es": "Acuerdo Climático Global 2026",
      "pt": "Acordo Climático Global 2026"
    },
    "description": {
      "en": "International treaty signed to reduce carbon emissions by 50% before 2040.",
      "pt": "Tratado internacional assinado para reduzir emissões de carbono em 50% até 2040."
    },
    "type": "LegalDocument", 
    "format": "PDF/A-3",
    "language": ["en", "es", "pt"],
    "size_bytes": 2450000,
    "hash_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  },

  "context": {
    "temporal": {
      "date": "2026-08-13",
      "era": "Post-Industrial",
      "significance": "Marked the first global binding agreement on carbon tax."
    },
    "spatial": {
      "location_name": "Geneva, Switzerland",
      "coordinates": { "lat": 46.2044, "lon": 6.1432 },
      "scope": "Global"
    },
    "cultural": {
      "creator": "United Nations Framework Convention on Climate Change",
      "contributors": ["195 Member States"],
      "keywords": ["climate change", "treaty", "carbon tax", "sustainability"],
      "related_events": ["2025 Heatwave Crisis", "2026 UN General Assembly"]
    }
  },

  "technical": {
    "storage_medium": "Project Silica Glass",
    "encryption": "None (Plain Text/Open Standard)",
    "compression": "None",
    "error_correction": "Reed-Solomon Code Level 3",
    "required_hardware": "Optical Reader v2.0+",
    "software_dependencies": ["PDF Reader (ISO 19005-3)", "UTF-8 Decoder"]
  },

  "preservation": {
    "migration_history": [],
    "integrity_check": {
      "algorithm": "SHA-256",
      "last_checked": "2026-08-13",
      "status": "VALID"
    },
    "recommended_refresh_cycle": "100 years"
  }
}

---

Field Definitions

Root Level
@context: URI pointing to the JSON-LD context definition (ensures semantic mapping).
@type: Always CulturalArtifact for top-level objects.
@id: A globally unique identifier (URN or UUID) for the artifact.

Metadata
created: ISO 8601 timestamp of ingestion.
ingestor: Institution or entity responsible for adding this record.
license: SPDX license identifier (e.g., CC0-1.0, MIT, CC-BY-SA-4.0).

Artifact
title/description: Multilingual objects (key = language code).
type: Controlled vocabulary (e.g., LegalDocument, NewsArticle, MusicTrack, ScientificPaper, TechnicalManual, Image, Video).
format: File extension or MIME type (preferably archival standards like PDF/A, FLAC, TXT).
hash_sha256: Checksum for integrity verification.

Context (Crucial for Future Interpretation)
temporal: When it happened and why it matters at that time.
spatial: Where it happened. Coordinates help future geolocation.
cultural: Who made it, keywords, and related events. This builds the "knowledge graph" of the era.

Technical
Describes how to read the data. Essential if file formats become obscure.
encryption: Must be None for core cultural data. Encryption keys can be lost; knowledge should not be locked.

Preservation
Tracks integrity checks and migration history (if the file format is ever converted).

Controlled Vocabularies (Suggested)
To ensure consistency, use these terms for artifact.type:

Text: NewsArticle, Book, LegalDocument, PersonalLetter, ScientificPaper, BlogPost
Media: MusicTrack, Podcast, VideoRecording, Photograph, DigitalArt
Data: Dataset, Map, SoftwareSourceCode, DatabaseSchema
Instruction: TechnicalManual, MedicalGuide, AgriculturalGuide, FirstAid

Example: Simple News Article
---
{
  "@context": "https://open-capsule.org/context/v1",
  "@type": "CulturalArtifact",
  "@id": "urn:uuid:12345678-1234-1234-1234-1234567890ab",
  "metadata": { "created": "2026-08-13T10:00:00Z", "ingestor": "Local University Archive", "license": "CC-BY-4.0" },
  "artifact": {
    "title": { "en": "City Council Approves New Water Recycling Plant" },
    "type": "NewsArticle",
    "format": "PDF/A-3",
    "language": ["en"],
    "hash_sha256": "abc123..."
  },
  "context": {
    "temporal": { "date": "2026-08-13", "significance": "Critical infrastructure response to regional drought." },
    "spatial": { "location_name": "Austin, Texas, USA", "scope": "Local" },
    "cultural": { "creator": "Austin Daily News", "keywords": ["water", "infrastructure", "drought", "city council"] }
  }
}
---

Next Steps for Collaboration
Information Scientists: Review and refine the controlled vocabularies.
Linguists: Propose standards for handling extinct or evolving languages.
Engineers: Validate the technical section for hardware readability constraints.
Legal Experts: Advise on license compatibility for global archival.

---

This is a living document. Propose changes via a Pull Request.
