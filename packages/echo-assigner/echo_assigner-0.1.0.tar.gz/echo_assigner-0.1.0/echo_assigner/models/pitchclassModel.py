import numpy as np
from .baseModel import stBase
from ..utils.extraction import *
from ..utils.preprocessing import *


class Pc_Data(stBase):
    def __init__(self, midi_path: str, midi_number: int, division: float | int):
        super().__init__(midi_path)

        ### EXTRACTION ###
        self.pitchclass = pitch_class(self.stream, division) # pitchClassごとの音の長さの合計を計算
        self.scales = presume_chord(self.stream.parts[1], division) # コード推定

        self.vector = np.array([
                        [midi_number for _ in np.arange(0, self.length, division)], # midi番号
                        np.arange(0, self.length, division), # 小節番号
                        *self.pitchclass, # pitchclass
                        self.scales # 音符ごとのコードネーム
                        ]).T # 転置&ベクトル化
        
        
class Pc_Input(stBase):
    def __init__(self, midi_path: str, division: float | int):
        super().__init__(midi_path)
        self.streamC = ignore_rest(trasnpose_toC(self.stream)) # 休符を埋めて、Cメジャーへ移調
        self.scales = presume_chord(self.stream.parts[0]) # コード推定
        self.name = "pitchclass"

        ### EXTRACTION ###
        self.vector = pitch_class(self.streamC, division).T # pitchClassごとの音の長さの合計を計算




if __name__ == "__main__":
    pc = Pc_Input("/Users/pam/create-future-pj/database/sample/input10.mid")
    print(pc.vector)