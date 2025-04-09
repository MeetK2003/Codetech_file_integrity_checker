# codetech_ task to create file_integrity_checker

# 🔐 File Integrity Checker

This is a simple Python project created for **Internship Task - 1** to help monitor changes in files by calculating and comparing their hash values.

---

## 📌 Task Objective

- Build a tool to **detect changes** in files.
- Use **hashing** to check file integrity.
- Deliver a **Python script** using the `hashlib` library.

---

## 🚀 How It Works

1. The script reads a file.
2. It generates a **SHA-256 hash** (like a fingerprint).
3. It saves that hash.
4. Later, it checks if the file has changed by **comparing** the old hash with the new one.

---

## 🧰 Tools & Libraries

- Python 3
- `hashlib`
- `os` (built-in Python module)

---

## 🧪 How to Use

1. Clone this repository or download the files.
2. Place your target file (like `example.txt`) in the same folder.
3. Run the Python script:

```bash
python file_integrity_checker.py
