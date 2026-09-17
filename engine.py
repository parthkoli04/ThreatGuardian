import hashlib
import os
from tkinter import messagebox

# ------------------------------------------------------------------
# Signature database
# ------------------------------------------------------------------
# Loaded ONCE at import into a { sha256 : malware_name } dict.
# - dict lookup is O(1) per file instead of scanning 40k entries (O(n)).
# - zip() pairs hash<->name by index and safely stops at the shorter
#   list, so the 40,069 vs 32,470 length mismatch can no longer cause
#   an IndexError or a misaligned name.
# ------------------------------------------------------------------
def _load_database():
    try:
        with open("virusHash.unibit", "r") as f:
            hashes = f.read().splitlines()
        with open("virusInfo.unibit", "r") as f:
            names = f.read().splitlines()
    except FileNotFoundError:
        messagebox.showerror(
            "ThreatGuardian",
            "Signature database (virusHash.unibit / virusInfo.unibit) not found."
        )
        return {}
    return dict(zip(hashes, names))


malware_db = _load_database()

# Backwards-compatible aliases (kept in case main.py references them)
malware_hashes = list(malware_db.keys())
virusInfo = list(malware_db.values())


# ------------------------------------------------------------------
# Hash a single file
# ------------------------------------------------------------------
def sha256_hash(filename):
    try:
        with open(filename, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except (OSError, PermissionError):
        # Unreadable / locked / gone — treat as "cannot hash"
        return 0


# ------------------------------------------------------------------
# Check one file against the database  ->  malware name, or 0 if clean
# ------------------------------------------------------------------
def malware_checker(pathOfFile):
    file_hash = sha256_hash(pathOfFile)
    if file_hash == 0:
        return 0
    return malware_db.get(file_hash, 0)


# ------------------------------------------------------------------
# Scan a directory tree
# ------------------------------------------------------------------
virusName = []
virusPath = []


def virusScanner(path):
    # Reset results so repeated scans don't accumulate stale hits
    virusName.clear()
    virusPath.clear()

    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            result = malware_checker(full_path)   # hash + lookup once
            if result != 0:
                print(full_path)
                virusName.append(result + " :: File :: " + os.path.normpath(full_path))
                virusPath.append(full_path)       # now populated -> removal works

    return virusName


# ------------------------------------------------------------------
# Remove detected threats
# ------------------------------------------------------------------
def virusRemover(path):
    virusScanner(path)
    if not virusPath:
        return 0
    for p in virusPath:
        try:
            os.remove(p)
        except OSError:
            pass


# ------------------------------------------------------------------
# Junk / temp file cleaner  (unchanged from original)
# ------------------------------------------------------------------
def juckFileRemover():

    # Temp Files Remover
    temp_list = list()

    # Windows username
    username = os.environ.get('USERNAME').upper().split(" ")

    for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Temp"):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]

    for (dirpath, dirnames, filenames) in os.walk("C:\\Users\\{}~1\\AppData\\Local\\Temp".format(username[0])):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]

    for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Prefetch"):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]

    if temp_list:
        for i in temp_list:
            print(i)
            try:
                os.remove(i)
            except:
                pass
            try:
                os.rmdir(i)
            except:
                pass
        messagebox.showinfo(
            "Threat Guardian",
            "All Temporary Files Removed Successfully" + '\n' +
            "Total Files Removed : {}".format(len(temp_list))
        )
    else:
        return 0


# ------------------------------------------------------------------
# RAM booster  (unchanged from original)
# ------------------------------------------------------------------
def ramBooster():

    taskList = ["notepad.exe", "AnyDesk.exe", "TeamViewer_Service.exe", "msedge.exe", "IDMan.exe"]

    for i in taskList:
        os.system("taskkill /f /im  {}".format(i))

    messagebox.showinfo("Ram Booster", "Ram Boosted Successfully")
