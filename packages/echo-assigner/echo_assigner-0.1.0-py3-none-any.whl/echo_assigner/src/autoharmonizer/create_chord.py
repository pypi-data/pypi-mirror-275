import os, warnings, pickle
import numpy as np
from ...src.autoharmonizer.config import *
from music21 import *
from samplings import gamma_sampling
from tensorflow.python.keras.utils.np_utils import to_categorical

# use cpu
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
warnings.filterwarnings("ignore")

# Load chord types
with open(os.path.dirname(__file__)+"/bin/chord_types.bin", "rb") as filepath:
    chord_types = pickle.load(filepath)


def generate_chord( chord_model, melody_data, beat_data, key_data, 
                    segment_length=SEGMENT_LENGTH, rhythm_gamma=RHYTHM_DENSITY, chord_per_bar=CHORD_PER_BAR):

    # Process each melody sequence in the corpus
    # Load the corresponding beat sequence
    song_chord = segment_length*[0]

    song_melody = segment_length*[0] + melody_data + segment_length*[0]
    song_beat = segment_length*[0] + beat_data + segment_length*[0]
    song_key = segment_length*[0] + key_data + segment_length*[0]
    
    # Predict each pair
    for idx in range(segment_length, len(song_melody)-segment_length):
        
        # Create input data
        melody_left = song_melody[idx-segment_length:idx]
        melody_right = song_melody[idx:idx+segment_length][::-1]
        beat_left = song_beat[idx-segment_length:idx]
        beat_right = song_beat[idx:idx+segment_length][::-1]
        key_left = song_key[idx-segment_length:idx]
        key_right = song_key[idx:idx+segment_length][::-1]
        chord_left = song_chord[idx-segment_length:idx]
        
        # One-hot vectorization
        melody_left = to_categorical(melody_left, num_classes=128)
        melody_right = to_categorical(melody_right, num_classes=128)
        beat_left = to_categorical(beat_left, num_classes=5)
        beat_right = to_categorical(beat_right, num_classes=5)
        key_left = to_categorical(key_left, num_classes=16)
        key_right = to_categorical(key_right, num_classes=16)
        condition_left = np.concatenate((beat_left, key_left), axis=-1)
        condition_right = np.concatenate((beat_right, key_right), axis=-1)
        chord_left = to_categorical(chord_left, num_classes=len(chord_types))

        # expand dimension
        melody_left = np.expand_dims(melody_left, axis=0)
        melody_right = np.expand_dims(melody_right, axis=0)
        condition_left = np.expand_dims(condition_left, axis=0)
        condition_right = np.expand_dims(condition_right, axis=0)
        chord_left = np.expand_dims(chord_left, axis=0)
        
        # Predict the next chord
        prediction = chord_model.predict(x=[melody_left, melody_right, condition_left, condition_right, chord_left], verbose=0)[0]

        if song_melody[idx]!=0 and song_beat[idx]==4:
            prediction = gamma_sampling(prediction, [[0]], [1], return_probs=True)

        # Tuning rhythm density
        if chord_per_bar:
            if song_beat[idx]==4 and (song_melody[idx]!=song_melody[idx-1] or song_beat[idx]!=song_beat[idx-1]) and not (idx==segment_length and song_melody[idx]==0):
                prediction = gamma_sampling(prediction, [[song_chord[-1]]], [1], return_probs=True)
            
            else:
                prediction = gamma_sampling(prediction, [[song_chord[-1]]], [0], return_probs=True)

        else:
            prediction = gamma_sampling(prediction, [[song_chord[-1]]], [rhythm_gamma], return_probs=True)

        cho_idx = np.argmax(prediction, axis=-1)
        song_chord.append(cho_idx)
    
    # Remove the leading padding
    chord_data = song_chord[segment_length:]

    # Convert to music
    chord_info = []
    offset = 0.0

    song_chord = [chord_types[int(cho_idx)] for cho_idx in chord_data]
    song_beat = beat_data
    pre_chord = None
        
    for t_idx, cho in enumerate(song_chord):
        cho = cho.replace('N.C.', 'R')
        cho = cho.replace('bpedal', '-pedal')
        if cho != 'R' and (pre_chord != cho or (chord_info and t_idx!=0 and song_beat[t_idx]==4 and song_beat[t_idx-1]!=4)):
            chord_symbol= harmony.ChordSymbol(cho)
            chord_symbol = chord_symbol
            chord_symbol.offset = offset
            chord_info.append(chord_symbol)
        offset += 0.25
        pre_chord = cho

    return chord_info

