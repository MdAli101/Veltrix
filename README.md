## Veltrix 🔍📋

**Veltrix** is a lightweight utility that automatically extracts phone numbers and email addresses from any text currently stored in your clipboard. Designed for speed and simplicity, Veltrix helps you quickly pull out important contact information without the need to manually scan through content.

### ✨ Features

* 📋 **Clipboard Integration** – Reads directly from your system clipboard
* 📞 **Phone Number Extraction** – Supports various phone number formats
* 📧 **Email Extraction** – Detects standard email patterns accurately
* ⚡ **Fast & Lightweight** – Minimal dependencies, quick execution
* 🖥️ **Command-line Interface** – Easy to run from terminal or integrate into scripts

### 🛠️ Usage

Simply copy any text containing contact information, then run:

```bash
python veltrix.py
```

And Veltrix will output the extracted phone numbers and emails.

### 📦 Requirements

* Python 3.x
* `pyperclip` (for clipboard access)
* `re` (standard regex module)
* `phonenumbers` (to identify region)
* `colorama` (for title)
* `pyfiglet` (for rich text)

### 📈 Ideal For

* Journalists, researchers, data miners
* Developers parsing user data
* Anyone needing to extract contact info in bulk