import os
import pickle
import numpy as np
from music21 import *
from ...src.autoharmonizer.config import *

def quant_score(score):
    
    for element in score.flat:
        onset = np.ceil(element.offset/0.25)*0.25

        if isinstance(element, note.Note) or isinstance(element, note.Rest) or isinstance(element, chord.Chord):
            offset = np.ceil((element.offset+element.quarterLength)/0.25)*0.25
            element.quarterLength = offset - onset

        element.offset = onset

    return score


def melody_reader(score):

    melody_txt = []
    beat_txt = []
    key_txt = []
    sharps = 0

    for element in score.flat:

        if isinstance(element, note.Note):
            # midi pitch as note onset
            token = element.pitch.midi

        elif isinstance(element, note.Rest):
            # 0 as rest onset
            token = 0
            
        elif isinstance(element, chord.Chord) and not isinstance(element, harmony.ChordSymbol):
            notes = [n.pitch.midi for n in element.notes]
            notes.sort()
            token = notes[-1]
        
        elif isinstance(element, key.Key) or isinstance(element, key.KeySignature):
            sharps = element.sharps+8
            continue
            
        else:
            continue
        
        melody_txt += [token]*int(element.quarterLength*4)
        beat_txt += [int(element.beatStrength*4)]*int(element.quarterLength*4)
        key_txt += [sharps]*int(element.quarterLength*4)

    return melody_txt, beat_txt, key_txt


# fromDataset = Falseがデフォルト
# Trueに関する補足が必要
def to_corpus(score: stream.Part, fromDataset=False):
    try:
        song_data = []

        score = quant_score(score)
        melody_txt, beat_txt, key_txt = melody_reader(score)

        if fromDataset:
            if len(melody_txt)==len(beat_txt) and len(beat_txt)==len(key_txt):
                song_data.append((melody_txt, beat_txt, key_txt))
            
            else:
                raise Exception

        else:
            if len(melody_txt)!=len(beat_txt) or len(melody_txt)!=len(key_txt):
                min_len = min(len(melody_txt), len(beat_txt))
                melody_txt = melody_txt[:min_len]
                beat_txt = beat_txt[:min_len]
                key_txt = key_txt[:min_len]
        
        if not fromDataset:
            data_corpus = (melody_txt, beat_txt, key_txt)
        
        elif len(song_data)>0:
            data_corpus = (song_data)

    except Exception as e:
        raise e

    if fromDataset:
        chord_types = [song[3] for songs in data_corpus for song in songs]
        chord_types = [item for sublist in chord_types for item in sublist]
        chord_types = list(set(chord_types))
        chord_types.remove('R')
        chord_types = ['R']+chord_types

        with open(os.path.dirname(__file__)+"/bin/chord_types.bin", "wb") as filepath:
            pickle.dump(chord_types, filepath)

        with open(os.path.dirname(__file__)+"/bin/data_corpus.bin", "wb") as filepath:
            pickle.dump(data_corpus, filepath)
    
    else:
        return data_corpus