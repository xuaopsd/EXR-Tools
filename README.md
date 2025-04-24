# EXR Tools

**EXR Tools** is a growing collection of utilities designed to simplify workflows involving `.exr` files, especially in 3D rendering pipelines.

This repository aims to offer tools that assist in validation, inspection, and automation of processes with EXR sequences.

## 🔍 Tool 1: EXR Validator (`exr_validator.py`)

The **EXR Validator** is the first tool in this collection. It helps identify:

- **Corrupted EXR files** (files that cannot be opened/read)
- **Suspicious EXR files** (files with a size that deviates significantly from their neighbors in the sequence)

This is useful for spotting rendering issues in long image sequences where visual inspection would be time-consuming.

### How it works

- Scans a folder with EXR files
- Tries to open each file with `OpenEXR`
- Compares each file’s size to its neighbors in the sequence
- Flags:
  - Files that can’t be opened as **invalid**
  - Files whose size differs more than 20% from the local average as **suspicious**

### 📦 Requirements

- Python 3.x
- `OpenEXR` module (from `openexr-python`)

Install with:

```bash
pip install openexr
```

### ▶️ Usage

1. Run the script:
   ```bash
   python exr_validator.py
   ```
2. Enter the path to the folder containing your EXR sequence when prompted.
3. The script will output:
   - Total files scanned
   - Count of valid, invalid, and suspicious files
   - List of invalid/suspicious filenames
   - Average EXR file size (for reference)

More tools coming soon. Contributions and suggestions are welcome!




