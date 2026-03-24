# 🚀 Startup Automation Script

This project automatically opens your favorite apps and websites with one click.

---

## 📌 What This Script Does

* Opens selected applications (WhatsApp, VS Code, Notepad, etc.)
* Opens useful websites (YouTube, Calendar, ChatGPT, etc.)
* Adds small delays to avoid system lag
* Runs everything in sequence smoothly

---

## 🧰 Requirements

Before running the script, make sure you have:

1. **Python installed (version 3.8 or higher)**
2. Required Python library:

   ```
   pip install AppOpener
   ```

---

## 📁 Project Files

* `atonce.py` → Main script (you can edit this)
* `atonce.exe` → Ready-to-run executable (optional)

---

## ▶️ How to Run the Script

### Option 1: Run using Python

1. Open Command Prompt
2. Navigate to the script folder:

   ```
   cd path\to\your\folder
   ```
3. Run:

   ```
   python atonce.py
   ```

---

### Option 2: Run using EXE

1. Go to the `dist` folder
2. Double-click:

   ```
   atonce.exe
   ```

---

## ⚙️ How to Customize

### ✏️ Edit Apps

Open `atonce.py` and modify:

```python
apps = [
    "File Explorer",
    "notepad"
]
```

---

### 🌐 Edit Websites

```python
urls = [
    "https://www.youtube.com",
]
```

---

### ⏱️ Adjust Delay

```python
APP_DELAY = 2   # seconds between apps
URL_DELAY = 3   # seconds between websites
```

---

## 🔍 Finding Correct App Names

If an app does not open:

```python
from AppOpener import open

open("appname", match_closest=True, output=True)
```

This helps you find the correct system name.

---

## 🔄 Rebuilding the EXE (after editing)

If you change the script, rebuild the `.exe`:

```
pyinstaller --onefile --noconsole atonce.py
```

New file will be in:

```
dist/atonce.exe
```

---

## ⌨️ Assign a Hotkey to Run the EXE

You can launch the script using a keyboard shortcut:

### Steps:

1. Right-click `atonce.exe` → **Create shortcut**
2. Right-click the shortcut → **Properties**
3. Find **Shortcut key**
4. Press your desired keys (e.g. `Ctrl + Alt + S`)
5. Click **Apply → OK**

---

### 📌 Important:

* The shortcut must be placed on:

  * Desktop **OR**
  * Start Menu folder

To open Start Menu folder:

```
Win + R → shell:programs
```

* Hotkeys must include `Ctrl` or `Alt`
* Do not delete the shortcut (hotkey depends on it)

---

## 🚀 Auto Run on Startup (Optional)

1. Press `Win + R`
2. Type:

   ```
   shell:startup
   ```
3. Paste `atonce.exe` into that folder

---

## ⚠️ Troubleshooting

* Apps not opening → Check app names
* EXE not working → Run from Command Prompt to see errors
* Slow startup → Increase delay values

---

## 💡 Notes

* Keep `atonce.py` safe — you need it for editing
* EXE file cannot be edited directly
* First EXE run may be slower (normal behavior)

---

## 🎯 Use Cases

* Daily work setup
* Study environment launcher
* One-click productivity boost
You now have a fully automated startup system 🚀

