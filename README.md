<div align="center">

# 🛡️ ThreatGuardian

**A signature-based antivirus for Windows, built in Python.**
Scans files by SHA-256 hash against a ~40,000-signature malware database.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square&logo=windows&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-2E8B57?style=flat-square)
![Status](https://img.shields.io/badge/Status-Educational%20Project-orange?style=flat-square)

</div>

---

## Overview

ThreatGuardian is a desktop antivirus application I built to understand how
signature-based detection engines actually work under the hood — hashing files,
matching them against a signature database, and reporting hits. It ships with a
CustomTkinter GUI, a real signature database of ~40,000 known malware hashes, and
a handful of system-utility features.

> **Concept inspired by** an existing open-source antivirus project
> (<!-- FILL: link the repo you took the idea from, e.g. HarshscGithub/Atarbals-Modern-Antivirus -->).
> The engine and application code here are written from scratch.

---

## Features

- 🔍 **Signature-based detection** — computes the **SHA-256** hash of each file and
  matches it against a database of ~40,000 known malware hashes.
- 📁 **Directory scanning** — recursively walks a folder (`os.walk`) and flags any
  file whose hash is in the database, with the malware family name.
- 🖥️ **CustomTkinter GUI** — splash screen + main dashboard (Quick Scan, utilities).
- ⏱️ **Real-time protection module** — background watcher started at launch.
- 🧹 **Junk file cleaner** — clears Windows `Temp` and `Prefetch` directories.
- ⚡ **System boost** — terminates a preset list of background processes to free RAM.

---

## How Detection Works

1. **Load signatures** — `engine.py` reads `virusHash.unibit` (SHA-256 hashes) and
   `virusInfo.unibit` (matching malware names) into memory at startup.
2. **Hash the target** — each scanned file is read in binary and hashed with
   `hashlib.sha256`.
3. **Match** — the file's hash is compared against the signature list; a hit returns
   the malware family name (e.g. `Trojan-Ransom/Petya`).
4. **Report** — matches are collected and surfaced in the GUI.

This is **exact-hash signature matching**: it detects *known* samples whose hashes
are in the database. It does not detect modified, packed, or unknown malware — see
[Limitations](#limitations).

---

## Requirements

- **Windows** (uses `pywin32`, `os.startfile`, `.bat` launchers, and `C:\` paths)
- **Python 3.11+**

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
# Launch with the splash screen (recommended)
python splash.py

# ...or start the main window directly
python main.py
```

---

## Project Structure

```
ThreatGuardian/
├── splash.py               # Splash screen -> launches main.py
├── main.py                 # Main CustomTkinter GUI (dashboard)
├── engine.py               # Core: SHA-256 hashing, DB matching, utilities
├── virusscanner.py         # Standalone full-drive scanner
├── RealTime.py             # Real-time protection logic
├── realtimepro_checker.py  # Real-time protection state checker
├── virusHash.unibit        # Signature DB - ~40,000 SHA-256 malware hashes
├── virusInfo.unibit        # Malware family names (paired with hashes)
├── res/                    # GUI assets (icons, animations, buttons)
├── *.bat                   # Windows launchers for background scanners
├── requirements.txt
└── README.md
```

---

## Limitations

- **Educational project** - not a replacement for a production antivirus.
- **Exact-hash detection only** - catches known samples in the database. Changing a
  single byte of a malware file changes its hash and evades detection. No heuristic
  or behavioural analysis.
- **Windows-only** - depends on `pywin32`, batch scripts, and hardcoded system paths.
- **Detection != removal (yet)** - the scanner flags threats; automated removal is a
  work in progress.
- The junk cleaner clears `Temp`/`Prefetch` directly - run with care.

---

## Roadmap

- [ ] Replace the linear hash search with a `set`/`dict` lookup (O(n) -> O(1) per file)
- [ ] Pair hashes and names in a single dict (removes index-mismatch / `IndexError` risk)
- [ ] Implement working quarantine + removal
- [ ] Signature-database update mechanism
- [ ] Cross-platform support (Linux/macOS)

---

## License

<!-- FILL: add a LICENSE file. MIT is a good default for a portfolio project.
     (You took only the *idea* from another repo, not code, so you're free to
     choose your own license.) -->
Released under the MIT License - see [`LICENSE`](LICENSE).

---

<div align="center">

Built by **[Parth Koli](https://github.com/parthkoli04)** - M.S. Cybersecurity, RMIT Melbourne

</div>
