import tkinter as tk
from tkinter import ttk, messagebox
import threading
import mido
import time


# Remapping function
def remap_note(note):
    while note < 40:
        note += 12
    while note > 80:
        note -= 12
    return note


# MIDI handling class
class MidiMapper:
    def __init__(self, input_name, output_name, log_callback):
        self.input_name = input_name
        self.output_name = output_name
        self.log_callback = log_callback
        self.running = False
        self.thread = None
        self.inport = None
        self.outport = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        # Close ports if open
        if self.inport:
            self.inport.close()
            self.inport = None
        if self.outport:
            self.outport.close()
            self.outport = None

    def run(self):
        try:
            self.inport = mido.open_input(self.input_name)
            self.outport = mido.open_output(self.output_name)
            self.log_callback(f"Remapping started from '{self.input_name}' to '{self.output_name}'...\n")
            for msg in self.inport:
                if not self.running:
                    break
                if msg.type in ('note_on', 'note_off'):
                    new_note = remap_note(msg.note)
                    new_msg = msg.copy(note=new_note)
                    self.outport.send(new_msg)
                    self.log_callback(f"{msg.type.upper()} {msg.note} → {new_note}")
                else:
                    self.outport.send(msg)
        except Exception as e:
            self.log_callback(f"Error: {e}")
        finally:
            # Extra safety on exit
            self.stop()


# GUI class
class MidiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WEBFISHING MIDI Note Remapper 🎣🎹")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.mapper = None

        # Input Dropdown
        tk.Label(root, text="Input Device:").grid(row=0, column=0, sticky="w")
        self.input_var = tk.StringVar()
        self.input_combo = ttk.Combobox(root, textvariable=self.input_var, width=40, state='readonly')
        self.input_combo['values'] = mido.get_input_names()
        self.input_combo.grid(row=0, column=1)

        # Output Dropdown
        tk.Label(root, text="Output Device:").grid(row=1, column=0, sticky="w")
        self.output_var = tk.StringVar()
        self.output_combo = ttk.Combobox(root, textvariable=self.output_var, width=40, state='readonly')
        self.output_combo['values'] = mido.get_output_names()
        self.output_combo.grid(row=1, column=1)

        # Start/Stop Button
        self.toggle_btn = tk.Button(root, text="Start Remapping", command=self.toggle_mapping, width=20)
        self.toggle_btn.grid(row=2, column=0, columnspan=2, pady=10)

        # Log Display
        self.log_text = tk.Text(root, height=10, width=60, state='disabled', bg='#f0f0f0')
        self.log_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def log(self, message):
        self.log_text.config(state='normal')
        self.log_text.insert('end', message + '\n')
        self.log_text.see('end')
        self.log_text.config(state='disabled')

    def toggle_mapping(self):
        if self.mapper and self.mapper.running:
            # Stop mapping
            self.mapper.stop()
            self.toggle_btn.config(text="Start Remapping")
            self.log("Stopped remapping.\n")

            # Re-enable and refresh dropdowns
            self.input_combo['state'] = 'readonly'
            self.output_combo['state'] = 'readonly'
            self.input_combo['values'] = mido.get_input_names()
            self.output_combo['values'] = mido.get_output_names()

        else:
            input_name = self.input_var.get()
            output_name = self.output_var.get()
            if not input_name or not output_name:
                messagebox.showwarning("Missing selection", "Please select both input and output devices.")
                return

            # Disable dropdowns during mapping
            self.input_combo['state'] = 'disabled'
            self.output_combo['state'] = 'disabled'

            # Start mapping
            self.mapper = MidiMapper(input_name, output_name, self.log)
            self.mapper.start()
            self.toggle_btn.config(text="Stop Remapping")

    def on_close(self):
        if self.mapper and self.mapper.running:
            self.mapper.stop()
            time.sleep(0.1)  # give time to release ports
        self.root.destroy()


def main():
    root = tk.Tk()
    MidiApp(root)
    root.mainloop()


# Run the app
if __name__ == '__main__':
    main()
