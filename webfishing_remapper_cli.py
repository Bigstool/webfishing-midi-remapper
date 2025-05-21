import mido

# Function to fold notes into 40–80 range
def remap_note(note):
    while note < 40:
        note += 12
    while note > 80:
        note -= 12
    return note


def main():
    # List MIDI ports
    print("Available MIDI input ports:")
    for i, name in enumerate(mido.get_input_names()):
        print(f"{i}: {name}")

    input_index = int(input("Select input port number: "))
    input_name = mido.get_input_names()[input_index]

    print("\nAvailable MIDI output ports:")
    for i, name in enumerate(mido.get_output_names()):
        print(f"{i}: {name}")

    output_index = int(input("Select output port number: "))
    output_name = mido.get_output_names()[output_index]

    # Open ports
    with mido.open_input(input_name) as inport, mido.open_output(output_name) as outport:
        print(f"\n🔁 Remapping MIDI from '{input_name}' to '{output_name}'...")
        print("🎶 Play your keyboard!\n")
        for msg in inport:
            if msg.type in ('note_on', 'note_off'):
                original = msg.note
                remapped = remap_note(msg.note)
                new_msg = msg.copy(note=remapped)
                outport.send(new_msg)
                print(f"{msg.type.upper()} {original} → {remapped}")
            else:
                outport.send(msg)  # Pass through other MIDI messages


if __name__ == "__main__":
    main()
