import music21 as m21
from ...src.autoharmonizer.model import build_model
from ...src.autoharmonizer.create_chord import generate_chord
from ...src.autoharmonizer.loader import to_corpus
from ...src.autoharmonizer.config import *

class AutoHarmonizer:
    def __init__(self, part: m21.stream.Part):
        self.part = part
        self.model = build_model(SEGMENT_LENGTH, RNN_SIZE, NUM_LAYERS, DROPOUT, training=False)
        self.melody_data, self.beat_data, self.key_data = to_corpus(part)
    
    # autoharmonizerの出力を {chord: start: end: } の形式で返す
    def get_chord_info(self):
        print(  '\033[35m' +  "[Autoharmonizer]"  + '\033[0m' +
            '\033[32m' +  " Chord Generating..." + '\033[0m')
        
        chord_data = generate_chord(self.model, self.melody_data, self.beat_data, self.key_data)

        chord_info = []
        for i in range(len(chord_data)):
            try:
                if i == 0 and chord_data[i].offset != 0:
                    chord_info.append({ "chord": chord_data[i].figure,
                                        "start": 0,
                                        "end": chord_data[i].offset})
                else:
                    chord_info.append({ "chord": chord_data[i].figure,
                                        "start": chord_data[i].offset,
                                        "end": chord_data[i+1].offset})
            except IndexError:
                if self.part.duration.quarterLength > chord_data[i].offset:
                    chord_info.append({ "chord": chord_data[i].figure,
                                        "start": chord_data[i].offset,
                                        "end": self.part.duration.quarterLength})
            
        return chord_info # -> {chord: start: end: }
    
    # part内の各noteについて、{note: scale: } の形式で返す
    def get_scale_note(self, other_part: m21.stream.Part = None):
        chord_info = self.get_chord_info()

        if other_part:
            give_notes = other_part.flatten().notes
        else:
            give_notes = self.part.flatten().notes

        notes = []
        scales = []
        for note in give_notes:
            notes.append(note.fullName)
            for chord in chord_info:
                if chord["start"] <= note.getOffsetInHierarchy(give_notes) < chord["end"]:
                    scales.append(chord["chord"])
        
        return { "note": notes, "scale": scales }
