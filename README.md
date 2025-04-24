# EXR Tools

**EXR Tools** is a growing collection of utilities designed to simplify workflows involving `.exr` files, especially in 3D rendering pipelines.

This repository aims to provide tools that assist in **validation**, **inspection**, and **automation** of processes with EXR sequences.

## 🔧 Tool 1: EXR Validator (`exr_validator.py`)

The **EXR Validator** is the first tool in this collection. It helps identify:

- **Corrupted EXR files** (files that cannot be opened/read)
- **Suspicious EXR files** (whose file size deviates significantly from their neighbors)

This is useful for detecting rendering issues in long EXR sequences without manual visual checks.

### ⚙️ How it works

- Scans a selected folder containing `.exr` files  
- Attempts to open each file using the `OpenEXR` module  
- Compares the size of each file with its 20 nearest neighbors  
- Flags:
  - Unreadable files as **invalid**
  - Files differing more than **20%** from the local average as **suspicious**

### 📦 Requirements

- Python 3.x  
- Modules listed in `requirements.txt`:
  - `openexr`
  - `tqdm`
  - `colorama`

To install all dependencies:

```bash
pip install -r requirements.txt
```

### ▶️ Usage

1. Run the script:

```bash
python exr_validator.py
```

2. Enter the path to the folder containing your `.exr` files when prompted.

3. The script will:
   - Show a **progress bar** while analyzing files
   - Print:
     - Total number of files
     - Count of valid, invalid, and suspicious files
     - Filenames of flagged files
     - Average file size in a human-readable format

---

🚀 **More tools coming soon. Contributions and suggestions are welcome!**
