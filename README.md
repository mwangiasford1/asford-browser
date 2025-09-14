# Asford Browser

[![Release](https://img.shields.io/github/v/release/mwangiasford1/asford-browser)](https://github.com/mwangiasford1/asford-browser/releases)
[![Downloads](https://img.shields.io/github/downloads/mwangiasford1/asford-browser/total)](https://github.com/mwangiasford1/asford-browser/releases)

A modern web browser built with PyQt5 featuring a premium splash screen and custom branding.

## 📥 Download
**Latest Release**: [AsfordBrowser.exe v1.0.0](https://github.com/mwangiasford1/asford-browser/releases/latest)

## Features
- Custom splash screen with premium logo
- Web browsing functionality
- Modern UI design
- Standalone executable

## Installation
```bash
pip install PyQt5 PyQtWebEngine
```

## Usage
```bash
python main.py
```

## Build Executable
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=assets/icons/asford.ico --name=AsfordBrowser main.py
```

## How to Find AsfordBrowser.exe

### Run PyInstaller
Make sure you've executed:
```bash
pyinstaller --onefile --windowed --icon=assets/icons/asford.ico --name=AsfordBrowser main.py
```

### Navigate to the dist/ Folder
After the build completes, PyInstaller creates two folders:
- `build/` – temporary files
- `dist/` – your final executable

**Note**: The `dist/` folder is not included in the repository (excluded by .gitignore). You must build the executable locally.

Inside `dist/`, you'll see:
```
AsfordBrowser.exe
```

### Location on Your Machine
If your project is in `C:\Users\Asford\Projects\asford-browser`, then the executable will be in:
```
C:\Users\Asford\Projects\asford-browser\dist\AsfordBrowser.exe
```