from dataclasses import dataclass
from mido import MidiFile
import pretty_midi
import ezdxf
from ezdxf import units
import os
import glob
import sys

# Process all midi files in the same directory as executable

#all units in mm, must be float values
distance_between_beats = 10.0 #distance at 120bpm
bottom_padding = 5.6 #distance between bottom of strip and lowest note
vertical_distance_between_notes = 2.00 #distance between each note on the strip vertically
strip_height = 70.0 #height of the strip entering music box
paper_lead = 150.0 #distance between start of strip and start of music
hole_radius = 1.0

paper_max_width = 13.7*25.4 #max horizontal width of paper being cut
paper_max_height = 10.9*25.4 #max vertical height of paper being cut

#list of notes currently available on music box
note_names_available = ['F3','G3','C4','D4','E4','F4','G4','A4','A#4','B4','C5','C#5','D5','D#5','E5','F5','F#5','G5','G#5','A5','A#5','B5','C6','C#6','D6','D#6','E6','F6','G6','A6']

# -----------------------------------------END OF GLOBALS----------------------------------------------------------

def process_midi_file(docName, exe_dir):
    global distance_between_beats
    mid = MidiFile(docName)

    # #all midi note on and off events
    note_positions_unclean = []

    @dataclass
    class note:
        note_name: int
        x: float #vertical position of note on reel (corresponds with note name)
        y: float #horizontal position of note on reel (corresponds with time)
        msg_type: str
        velocity: int

    first_tempo_received = False
    current_tempo = 0.0
    total_time = 0.0
    for msg in mid:
        # print("msg type:", msg.type, "msg time:" , msg.time)
        
        if msg.type == 'set_tempo':
            if not first_tempo_received:
                first_tempo_received = True
            
            current_tempo = msg.tempo

        if first_tempo_received:
            total_time += msg.time * (current_tempo/500000)
        else:
            total_time += msg.time
        

        if msg.type == 'note_on' or msg.type == 'note_off':
            x = -1
            if pretty_midi.note_number_to_name(msg.note) in note_names_available:
                x = (note_names_available.index(pretty_midi.note_number_to_name(msg.note))*vertical_distance_between_notes)+bottom_padding
            else:
                print("Note unavailable:", pretty_midi.note_number_to_name(msg.note))
             
            note_positions_unclean.append(note(msg.note,x,total_time*distance_between_beats*2.0,msg.type,msg.velocity))
            
        
        
        

    
    note_positions = list(filter(lambda item: item.velocity != 0 and item.x != -1 and item.msg_type != 'note_off', note_positions_unclean)) #remove midi notes represent the end of notes or don't exist in note_names_available

    # Calculate the maximum width needed based on the last note position
    if note_positions:
        max_note_position = max(note.y for note in note_positions)
        # Add paper_lead at the beginning and 20mm margin at the end
        calculated_width = max_note_position + paper_lead + 20.0
        print(f"Calculated width needed: {calculated_width:.1f}mm (last note at {max_note_position:.1f}mm)")
    else:
        calculated_width = paper_lead + 20.0
        print("No valid notes found, using minimum width")

    print(f"Processing {docName}: {len(note_positions)} notes")
    
    # Create a single DXF document for all notes
    doc = ezdxf.new()
    doc.units = units.MM
    mspLines = doc.modelspace()
    mspCircles = doc.modelspace()
    doc.layers.add(name="Numbers", color=1)

    heightOffset = 0
    strip_number = 0

    # Calculate how many strips fit in the paper height
    max_strips = int(paper_max_height // strip_height)
    
    # Add note holes
    for i, note_pos in enumerate(note_positions):
        # All notes go on strip 0 since we're making one long strip
        y_position = note_pos.y + paper_lead
        mspCircles.add_circle((y_position, note_pos.x), hole_radius).rgb = (255, 0, 0)

    # Draw single strip boundary
    # Add strip number to bottom corner
    number = mspLines.add_text("0").set_placement((2, 3))
    number.dxf.layer = "Numbers"

    # Left diagonal for first strip
    mspLines.add_line((0, 0), (0, strip_height/2.5)).rgb = (255, 0, 0)
    mspLines.add_line((0, strip_height/2.5), (10, strip_height)).rgb = (255, 0, 0)
    
    # Bottom line
    mspLines.add_line((0, 0), (calculated_width, 0)).rgb = (255, 0, 0)
    
    # Right line
    mspLines.add_line((calculated_width, 0), (calculated_width, strip_height)).rgb = (255, 0, 0)
    
    # Top line
    mspLines.add_line((10, strip_height), (calculated_width, strip_height)).rgb = (255, 0, 0)

    print(f"Single strip, Single DXF file, Width: {calculated_width:.1f}mm")

    # Create output directory if it doesn't exist
    output_dir = os.path.join(exe_dir, 'output')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    
    # Get base filename without path and extension
    base_filename = os.path.splitext(os.path.basename(docName))[0]
    
    # Save single DXF file
    output_filename = os.path.join(output_dir, f"{base_filename}.dxf")
    doc.saveas(output_filename)
    print(f"Saved: {output_filename}")

def main():
    # Get the directory where the executable is located
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        exe_dir = os.path.dirname(sys.executable)
    else:
        # Running as script
        exe_dir = os.path.dirname(os.path.abspath(__file__))
    
    print(f"Looking for MIDI files in: {exe_dir}")
    
    # Find all midi files in the same directory as the executable
    midi_files = []
    for ext in ["*.mid", "*.MID", "*.midi", "*.MIDI"]:
        midi_files.extend(glob.glob(os.path.join(exe_dir, ext)))
    
    # Remove duplicates
    midi_files = list(set(midi_files))
    
    if not midi_files:
        print("No MIDI files found in the executable directory!")
        print("Please place MIDI files in the same folder as the executable.")
        input("Press Enter to exit...")
        return
    
    print(f"Found {len(midi_files)} MIDI file(s) to process:")
    for file in midi_files:
        print(f"  - {os.path.basename(file)}")
    
    # Process each midi file
    for midi_file in midi_files:
        try:
            print(f"\n--- Processing {os.path.basename(midi_file)} ---")
            process_midi_file(midi_file, exe_dir)
        except Exception as e:
            print(f"Error processing {os.path.basename(midi_file)}: {e}")
    
    print("\nAll files processed!")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

