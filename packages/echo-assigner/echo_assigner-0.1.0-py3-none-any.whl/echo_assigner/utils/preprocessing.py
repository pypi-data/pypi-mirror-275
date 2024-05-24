import music21 as m21
from ..utils.calculation import keyC_dif

def trasnpose_toC(stream: m21.stream.Stream) -> m21.stream.Stream:
    key = stream.analyze('key')
    if key.mode == "minor": # マイナーは受け付けない
        raise Exception("midi key must be major")
    
    if len(stream) == 2 or len(stream) == 3:
        key_dif = keyC_dif(m21.note.Note(key.tonicPitchNameWithCase).pitch.ps)
        stream.transpose(key_dif*(-1), inPlace=True)

    else:
        raise Exception("midi must have 2 or 3 parts")
    
    return stream


def ignore_rest(stream: m21.stream.Stream) -> m21.stream.Stream:
    for measure in stream[1]:
        rests = []
        if isinstance(measure,m21.stream.Measure):
            for i,item in enumerate(measure):
                if isinstance(item,m21.note.Rest):
                    rest = item.quarterLength
                    rests.append(item)
                    note = measure[i-1]
                    if isinstance(note,m21.note.Note):
                        note.quarterLength += rest
            measure.remove(rests)
    return stream