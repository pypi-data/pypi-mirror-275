from typing import Literal

# インスタンスclass
from .src.cui import cui
from .src.create import create

#from scripts.database import database

from .models.statisticModel import St_Input
from .models.pitchclassModel import Pc_Input
from .utils.calculation import *

class EchoAssigner:
    '''
    ## params
    ### [need]
    * `input_path`: path of input midi file
    * `distmethod`: method of distance calculation
            * `0` :Euclidean
            * `1` :Chebyshev
            * `2` :Manhattan
            * `3` :Minkowski
            * `4` :Cosine

    ### [optional]
    * `logs`: whether to output logs at runtime (default: `True`)
    * `model`: model selection
            * `pitchclass`: model with pitch class as feature
            * `statistic`: model with 5 features
                * first pitch 
                * average pitch
                * variance of pitch
                * average change in pitch
                * note density as features

    * `division`: section of extracted features
            * `0.5` :1/2 measure
            * `1` :1 measure
            * `2` :2 measure
    '''
    def __init__(self,  input_path: str, 
                        distmethod: Literal[0,1,2,3,4],
                        logs: bool = True,
                        model: Literal["pitchclass", "statistic"] = "statistic", 
                        division: float | int = 2):
        
        # distmethod: 距離計算手法
        # 0=Euclidean, 1=Chebyshev, 2=Manhattan, 3=Minkowski, 4=Cosine
        assert distmethod in [0,1,2,3,4], "[Error] Invalid distance method."
        self.distmethod = distmethod

        # logs: 実行時にログの出力をするかどうか
        self.logs = logs

        # model: モデルの選択
        assert model in ["pitchclass", "statistic"], "[Error] Invalid model."
        
        # 最初の音高・音高の平均・音高の分散・音高の変化量の平均・音符密度を特徴量としたモデル
        if model == "statistic":
            self.model = St_Input(input_path, division)

        # ピッチクラスを特徴量としたモデル
        elif model == "pitchclass":
            self.model = Pc_Input(input_path, division)
            #self.vectors, self.labels, self.scales = pitchclassDB().reference(division)

        assert division == 0.5 or division >= 1, "[Error] Division is 0.5 or more than 1"
        self.division = division



        self.cui = cui(self.model, self.distmethod, self.division)
        # cui: CUIのインスタンス
        '''
        * `show_params()`: show settings params
        * `show_assigned_part()`: show information of assigned part
                * `method`:
                    * `text`: show as text in terminal
                    * `png`: save score as png & musicxml file
                    * `midi`: save score as midi file
                * `dirpath`: directly path to save score (default: `None`)
        * `show_similar_melody()`: show information of melody of high similarity
                * `method`:
                    * `text`: show as text in terminal
                    * `png`: save score as png & musicxml file
                    * `midi`: save score as midi file
                * `dirpath`: directly path to save score (default: `None`)
        * `show_melody_vector()`: show melody vector of similarity of input and knowledge base
        * `accuracy()`: show accuracy of similarity of input melody and knowledge base melody
        '''



        self.create = create(self.model, self.distmethod, self.logs, self.division)
        # create: createのインスタンス
        '''
        * `score()`: Returns similarity numbers and knowledge base part labels
        * `give_measures()`: Return scale for each measure and note from part label
        * `setup_part()`: Construct and return stream.Part from the scale of each measure and note
        * `shift_notes()`: Shift stream.Part configured in setup_part to the input scale
        * `fit_stream()`: Configure stream.Stream
        '''



        #self.database = database(self.model, )
        # todo: database: 知識ベースのインスタンス
        '''
        '''
        