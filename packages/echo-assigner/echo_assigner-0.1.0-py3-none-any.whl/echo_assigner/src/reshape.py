import music21 as m21
from ..utils.preprocessing import *


class Reshape:
    def __init__(self, stream: m21.stream.Stream, melody_part: int, accomp_part: int):
        self.stream: m21.stream.Stream = stream
        self.melody_part: m21.stream.Part = stream[melody_part+1]
        self.accomp_part: m21.stream.Part = stream[accomp_part+1]


    # 4拍子以外の小節を削除
    def remove_nquarter(self) -> None:
        for part in self.stream.parts:
            for measure in part:
                if isinstance(measure, m21.stream.Measure) \
                    and measure.duration.quarterLength != 4.0:
                    part.remove(measure, shiftOffsets=True)
        
        for part in self.stream.parts:
            for n, measure in enumerate(part):
                if isinstance(measure, m21.stream.Measure):
                    measure.number = n+1


    # 全休符の小節を削除
    def remove_allrest(self) -> None:
        pass


    # テンポ=60の調整
    def set_bpm60(self) -> None:
        for part in self.stream.parts:
            for measure in part:
                if isinstance(measure, m21.stream.Measure):
                    for item in measure.flat:
                        if isinstance(item, m21.tempo.MetronomeMark):
                            measure.remove(item)
            part[0].insert(0, m21.tempo.MetronomeMark(number=60))


    # コードは最高の音を取る
    def remove_chord(self) -> None:
        for measure in self.stream[1]:
            if isinstance(measure, m21.stream.Measure):
                for item in measure.flat.notes:
                    if isinstance(item, m21.chord.Chord):
                        highest_note = item[-1]
                        highest_note.offset = item.offset
                        highest_note.quarterLength = item.quarterLength
                        measure.flat.replace(item, highest_note)
