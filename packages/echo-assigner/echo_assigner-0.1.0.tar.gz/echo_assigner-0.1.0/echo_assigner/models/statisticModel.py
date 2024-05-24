import numpy as np
from ..utils.extraction import *
from ..utils.preprocessing import *
from .baseModel import stBase


class St_Data(stBase):
    def __init__(self, midi_path: str, midi_number: int, division: float | int):
        super().__init__(midi_path)
        self.notes = notes(self.stream, division) # [小節内音階]*小節数　のリストを作成

        ### EXTRACTION ###
        self.first_note = [note[0] for note in self.notes] # 最初の音高
        self.mean_notes = mean_or_var(self.notes, 'mean') # 音高の平均
        self.var_notes = mean_or_var(self.notes, 'var') # 音高の分散
        self.mean_notesdif = mean_notesdif(self.notes) # 音高の変化量の平均
        self.density = [len(n) / (60 * self.beat / self.bpm) for n in self.notes] # 音符密度
        self.scales = presume_chord(self.stream.parts[1], division) # 音符ごとのコードとノートネーム
        self.figureArray = convert_array(self.stream, division) # 正解率算出用の配列

        
        self.vector = np.array([
                        [midi_number for _ in np.arange(0, self.length, division)], # midi番号
                        np.arange(0, self.length, division), # 小節番号
                        self.first_note, # 最初の音階
                        self.mean_notes, # 音階の平均
                        self.var_notes, # 音階の分散
                        self.mean_notesdif, # 音階の変化量の平均
                        self.density, # 音符密度
                        self.scales, # 音符ごとのコードネーム
                        [{"array": array} for array in self.figureArray] # 正解率算出用の配列
                        ]).T # 転置&ベクトル化



class St_Input(stBase):
    def __init__(self, midi_path: str, division: float | int):
        super().__init__(midi_path)
        self.name = "statistic"
        self.streamC = ignore_rest(trasnpose_toC(self.stream))
        self.figureArray = convert_array(self.streamC, division) # 正解率算出用の配列
        self.notes = notes(self.streamC, division) # [小節内音階]*小節数　のリストを作成
        self.harmonizer = AutoHarmonizer(self.stream[1])

        ### EXTRACTION ###
        self.first_note = [note[0] for note in self.notes] # 最初の音高
        self.mean_notes = mean_or_var(self.notes, 'mean') # 音高の平均
        self.var_notes = mean_or_var(self.notes, 'var') # 音高の分散
        self.mean_notesdif = mean_notesdif(self.notes) # 音高の変化量の平均
        self.density = [len(n) / (60 * self.beat / self.bpm) for n in self.notes] # 音符密度
        
        self.vector = np.array([
                        self.first_note, # 最初の音階
                        self.mean_notes, # 音階の平均
                        self.var_notes, # 音階の分散
                        self.mean_notesdif, # 音階の変化量の平均
                        self.density # 音符密度
                        ]).T # 転置&ベクトル化




if __name__ == '__main__':
    st = St_Input("/Users/pam/create-future-pj/database/sample/input10.mid")
    print(st.vector)
