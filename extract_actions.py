import re
import sys
from pathlib import Path

ACTION_PATTERN = re.compile(r"^\s*(?:todo|action)\s*[:\-]?\s*(.+)$", re.IGNORECASE)

def extract_from_file(path: Path):
    items = []
    for line in path.read_text().splitlines():
        match = ACTION_PATTERN.match(line.strip())
        if match:
            text = match.group(1).strip()
            if text:
                items.append(text)
    return items

def main(folder: str):
    folder_path = Path(folder)
    note_files = sorted(folder_path.glob("*.txt"))

    if not note_files:
        print(f"No .txt files found in {folder_path}")
        return

    report = []
    total_lines_scanned = 0

    for note_file in note_files:
        total_lines_scanned += len(note_file.read_text().splitlines())
        items = extract_from_file(note_file)
        for item in items:
            report.append((note_file.name, item))

    print("=" * 60)
    print("ACTION ITEM REPORT")
    print("=" * 60)
    print(f"Files scanned: {len(note_files)}")
    print(f"Lines scanned: {total_lines_scanned}")
    print(f"Action items found: {len(report)}")
    print("-" * 60)
    for source, item in report:
        print(f"[{source}] -> {item}")
    print("=" * 60)

if __name__ == "__main__":
    folder_arg = sys.argv[1] if len(sys.argv) > 1 else "sample_notes"
    main(folder_arg)
