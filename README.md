# WEBFISHING MIDI Remapper 🎣🎹

A lightweight Windows GUI tool that remaps MIDI notes from your MIDI keyboard to the range of the in-game guitar. Out-of-range notes are *rounded to the closest octave* within the range, so you never lose a note again. 🎶

## 🧰 Features

- 🎹 Supports any MIDI input/output device on your system
- 📈 Remaps notes to the range of the in-game guitar (40–80)
- 🔁 Rounds out-of-range notes to the closest octave within that range
- 🪟 Simple, modern GUI using Tkinter

## 🔧 Develop it

### Dependencies

- Python 3.8+
- mido
- python-rtmidi

Install them with:

```bash
pip install mido python-rtmidi
```

## 📦 Bundle it

Install `PyInstaller`:

```bash
pip install pyinstaller
```

Build the `.exe`:

```bash
pyinstaller --onefile --windowed --hidden-import=mido.backends.rtmidi --icon=res/icon.ico webfishing_remapper.py
```







