# WEBFISHING MIDI Remapper 🎣🎹

A lightweight Windows GUI tool that remaps MIDI notes from your MIDI keyboard to the range of the in-game guitar. Out-of-range notes are *rounded to the closest octave* within the range, so you never lose a note again. 🎶

## 🧰 Features

- 🎹 Supports any MIDI input/output device on your system
- 📈 Remaps notes to the range of the in-game guitar (40–80)
- 🔁 Rounds out-of-range notes to the closest octave within that range
- 🪟 Simple, modern GUI using Tkinter

## 🚀 Use it

- Install a mod that allows you to play the in-game guitar with MIDI devices in WEBFISHING, e.g., [MIDI Strummer](https://github.com/puppy-girl/MidiStrummer).
- Download WEBFISHING MIDI Remapper (`webfishing_remapper.exe`) from [Releases](https://github.com/Bigstool/webfishing-midi-remapper/releases).
- Create a virtual loopback MIDI port using software like [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html).
- Connect your MIDI instrument to your computer.
- Launch WEBFISHING MIDI Remapper.
- For the input device, select your MIDI instrument.
- For the output device, select the virtual loopback MIDI port you've created.
- Click "Start Remapping". Try to play a few notes on your MIDI instrument. If you see note events appearing below the "Start Remapping" as you play, you're all set!
- Launch the game and voilà.

If you are looking to connect your MIDI instrument via Bluetooth, I recommend trying [MIDIberry](https://apps.microsoft.com/detail/9n39720h2m05). Notice that you will need to create one more virtual loopback MIDI port in this case. Select it as the output device in MIDIberry (with your Bluetooth MIDI instrument as the input device). Then, in WEBFISHING MIDI Remapper, select it (instead of your MIDI instrument) as the input device.

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

