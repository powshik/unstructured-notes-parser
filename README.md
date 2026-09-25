# Unstructured Notes Parser (Claude 101 Project)

A clean, template-agnostic Python utility designed to scan directories of mixed, messy meeting notes and instantly isolate actionable todo items into a unified, source-tracked console report. Built as a practical proof-of-concept application alongside the **Anthropic Claude 101** certification course.

## 🚀 The Core Problem
Meeting notes, logs, and rapid transcripts are naturally chaotic. Critical action items are frequently buried inside blocks of conversational text or unstructured formatting variations (`TODO`, `action:`, `Action -`). This project tackles the data normalization problem by parsing inconsistent layouts and generating high-integrity structured logs.

## ✨ Features
- **Regex Mapping:** Uses clean compiled regular expressions to match variant indicators natively without complex runtime overhead.
- **Source Attribute Mapping:** Scans across directory matrices, cleanly tracking the origin filename for every single isolated commitment.
- **Volumetric Tracking:** Live telemetry capturing the total files evaluated, absolute lines processed, and final action density metrics.

## 📦 Quick Start
1. Clone the repository:
   ```bash
   git clone https://github.com/powshik/unstructured-notes-parser.git
   cd unstructured-notes-parser

   
   ```
2. Run the pipeline against the baseline dataset:
   ```bash
   python3 extract_actions.py sample_notes
   ```
