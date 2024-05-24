import music21 as m21

class stBase:
    def __init__(self, midi_path: str):
        self.stream = m21.converter.parse(midi_path) #　stream変換

        ### BASIC ###
        self.key =  m21.note.Note(self.stream.analyze('key').tonicPitchNameWithCase).pitch.ps # キー抽出
        self.length = len(self.stream[1]) # stream長さ = measure数
        self.bpm = self.stream.metronomeMarkBoundaries()[0][2].number # bpm抽出
        self.beat = [signature.beatCount
                    for measure in self.stream[1] for signature in measure 
                    if isinstance(signature, m21.meter.TimeSignature)][0] # 拍数抽出
        self.velocity = min([note.volume.velocity for note in self.stream[1].flatten().notes]) # velocity抽出
