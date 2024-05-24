import music21 as m21
from typing import Literal

# from scripts.config import *
from ..utils.calculation import distfunction, accuraryfunction
from ..database.statistic import statisticDB
from ..models.statisticModel import St_Input
from ..models.pitchclassModel import Pc_Input
from ..src.create import create
from ..config import *

class cui:
    def __init__(self, model: St_Input | Pc_Input, distmethod: Literal[0,1,2,3,4], division: float | int = 2):
        self.model = model
        self.distmethod = distmethod
        self.division = division
    
    
    def show_params(self) -> None: # パラメータの表示
        print('\033[35m' +  f"---[Params]---"  + '\033[0m')
        print("[Model]:" + self.model.name)
        print("[Division]:" + str(self.division))
        print("[Distance Method]:" + distfunction([0], [0], self.distmethod)[1])
        print('\033[35m' +  f"--------------"  + '\033[0m')


    def show_assigned_part(self, method: Literal['text', 'png', 'midi'], dirpath: str = None) -> None: # 割り当てられたパートの表示
        assert method in ['text', 'png', 'midi'], "[Error] Invalid method."
        if method in ['png', 'midi'] and dirpath is None:
            raise Exception("[Error] If method is png or mid, need dirpath.")
        
        distance, label_info = create(self.model, self.distmethod, False, self.division).score()
        midiNums , measureNums = label_info[0], label_info[1]

        for i in range(len(distance)):
            print(  '\033[35m' +  f"[{int(midiNums[i])}.mid-{measureNums[i]} measure]"  + '\033[0m' 
                    + " - " + '\033[34m' + f"distance: {min(distance[i])}" + '\033[0m')
            
            accompaniment = m21.converter.parse(f"{DATABASE_PATH}/{int(midiNums[i])}.mid")[2] # 伴奏stream
            
            if method == 'text': ## テキスト表示
                if self.division >= 1:
                    for d in range(self.division):
                        accompaniment[int(measureNums[i]+d)].notes.show('text')
                        print('\033[36m' +  f"-----measureNumber: {measureNums[i]+d}-----"  + '\033[0m')
                elif self.division == 0.5:
                    for notes in accompaniment[int(measureNums[i])].flatten().notes:
                        if notes.offset >= 2.0 and (measureNums[i] / 0.5) % 2 == 1: # .5小節目の場合
                            print("{" + str(notes.offset) + "} " + str(notes))
                        elif notes.offset < 2.0 and (measureNums[i] / 0.5) % 2 == 0: # .0小節目の場合
                            print("{" + str(notes.offset) + "} " + str(notes))
            
            else: ## xmlかmidとして保存
                if self.division >= 1:
                    save_part = m21.stream.Part()
                    for d in range(self.division):
                        save_part.append(m21.stream.Measure(accompaniment[int(measureNums[i]+d)].flatten().notes))
                    
                    if method == "png":
                        save_part.write("musicxml.png", fp=f"{dirpath}/{int(midiNums[i])}mid - {measureNums[i]}measure.png")
                        print('\033[36m' +  f"[Saved] {int(midiNums[i])}mid - {measureNums[i]}measure.png and music xml"  + '\033[0m')

                    elif method == "midi":
                        save_part.write("midi", fp=f"{dirpath}/{int(midiNums[i])}mid - {measureNums[i]}measure.mid")
                        print('\033[36m' +  f"[Saved] {int(midiNums[i])}mid - {measureNums[i]}measure.mid"  + '\033[0m')
                
                elif self.division == 0.5:
                    save_measure = m21.stream.Measure()
                    for notes in accompaniment[int(measureNums[i])].flatten().notes:
                        if notes.offset >= 2.0 and (measureNums[i] / 0.5) % 2 == 1: # .5小節目の場合
                            save_measure.append(notes)
                        elif notes.offset < 2.0 and (measureNums[i] / 0.5) % 2 == 0: # .0小節目の場合
                            save_measure.append(notes)
                    
                    if method == "png":
                        save_measure.write("musicxml.png", fp=f"{dirpath}/{int(midiNums[i])}mid - {measureNums[i]}measure.png")
                        print('\033[36m' +  f"[Saved] {int(midiNums[i])}mid - {measureNums[i]}measure.png and music xml"  + '\033[0m')
                    elif method == "midi":
                        save_measure.write("midi", fp=f"{dirpath}/{int(midiNums[i])}mid - {measureNums[i]}measure.mid")
                        print('\033[36m' +  f"[Saved] {int(midiNums[i])}mid - {measureNums[i]}measure.mid"  + '\033[0m')



    def show_similar_melody(self, method: Literal['text', 'png', 'midi'], dirpath: str = None) -> None: # 距離計算されたメロディの表示
        assert method in ['text', 'png', 'midi'], "[Error] Invalid method."
        if method in ['png', 'midi'] and dirpath is None:
            raise Exception("[Error] If method is png or mid, need dirpath.")
        

        distance, label_info = create(self.model, self.distmethod, False, self.division).score()
        midiNums , measureNums = label_info[0], label_info[1]

        for i in range(len(distance)):
            print(  '\033[35m' +  f"[{int(midiNums[i])}.mid-{measureNums[i]} measure]"  + '\033[0m' 
                    + " - " + '\033[34m' + f"distance: {min(distance[i])}" + '\033[0m')
            
            accompaniment = m21.converter.parse(f"{DATABASE_PATH}/{int(midiNums[i])}.mid")[1] # メロディstream
            
            if method == 'text': ## テキスト表示
                if self.division >= 1:
                    for d in range(self.division):
                        accompaniment[int(measureNums[i]+d)].notes.show('text')
                        print('\033[36m' +  f"-----measureNumber: {measureNums[i]+d}-----"  + '\033[0m')
                elif self.division == 0.5:
                    for notes in accompaniment[int(measureNums[i])].flatten().notes:
                        if notes.offset >= 2.0 and (measureNums[i] / 0.5) % 2 == 1: # .5小節目の場合
                            print("{" + str(notes.offset) + "} " + str(notes))
                        elif notes.offset < 2.0 and (measureNums[i] / 0.5) % 2 == 0: # .0小節目の場合
                            print("{" + str(notes.offset) + "} " + str(notes))
            
            else: ## xmlかmidとして保存
                if self.division >= 1:
                    save_part = m21.stream.Part()
                    for d in range(self.division):
                        save_part.append(m21.stream.Measure(accompaniment[int(measureNums[i]+d)].flatten().notes))
                    
                    if method == "png":
                        save_part.write("musicxml.png", fp=f"{dirpath}/{int(midiNums[i])}mid - {measureNums[i]}measure.png")
                        print('\033[36m' +  f"[Saved] {int(midiNums[i])}mid - {measureNums[i]}measure.png and music xml"  + '\033[0m')

                    elif method == "midi":
                        save_part.write("midi", fp=f"{dirpath}/{int(midiNums[i])}mid - {measureNums[i]}measure.mid")
                        print('\033[36m' +  f"[Saved] {int(midiNums[i])}mid - {measureNums[i]}measure.mid"  + '\033[0m')
                
                elif self.division == 0.5:
                    save_measure = m21.stream.Measure()
                    for notes in accompaniment[int(measureNums[i])].flatten().notes:
                        if notes.offset >= 2.0 and (measureNums[i] / 0.5) % 2 == 1: # .5小節目の場合
                            save_measure.append(notes)
                        elif notes.offset < 2.0 and (measureNums[i] / 0.5) % 2 == 0: # .0小節目の場合
                            save_measure.append(notes)
                    
                    if method == "png":
                        save_measure.write("musicxml.png", fp=f"{dirpath}/{int(midiNums[i])}mid - {measureNums[i]}measure.png")
                        print('\033[36m' +  f"[Saved] {int(midiNums[i])}mid - {measureNums[i]}measure.png and music xml"  + '\033[0m')
                    elif method == "midi":
                        save_measure.write("midi", fp=f"{dirpath}/{int(midiNums[i])}mid - {measureNums[i]}measure.mid")
                        print('\033[36m' +  f"[Saved] {int(midiNums[i])}mid - {measureNums[i]}measure.mid"  + '\033[0m')
    

    def show_melody_vector(self) -> None:
        distance, label_info, vector_info = create(self.model, self.distmethod, False, self.division).score(return_vector=True)
        midiNums , measureNums = label_info[0], label_info[1]

        for i in range(len(distance)):
            print(  '\033[35m' +  f"[{int(midiNums[i])}.mid-{measureNums[i]} measure]"  + '\033[0m' 
                    + " - " + '\033[34m' + f"distance: {min(distance[i])}" + '\033[0m')
            print(  '\033[36m' + "input    melody" + '\033[0m' + \
                    " -> " + '\033[32m' +  str(self.model.vector[i])  + '\033[0m')
            print(  '\033[36m' + "selected melody" + '\033[0m' + \
                    " -> " + '\033[32m' +  str(vector_info[i])  + '\033[0m')
            
    
    def accuracy(self) -> None:
        distance, label_info = create(self.model, self.distmethod, False, self.division).score()
        midiNums , measureNums = label_info[0], label_info[1]

        accuraries = []
        for i in range(len(distance)):
            selected_melody = statisticDB().get_figure_array(self.division, midiNums[i], measureNums[i])
            accurary = accuraryfunction(selected_melody, self.model.figureArray[i])
            
            accuraries.append(accurary)

            print(  '\033[35m' +  f"[{int(midiNums[i])}.mid-{measureNums[i]} measure]"  + '\033[0m' 
                    + " - " + '\033[34m' + f"distance: {min(distance[i])}" + '\033[0m')
            print(  '\033[32m' + "Accurary Score" + \
                    " : " +  str(accurary)  + '\033[0m')
        
        print("------")
        print(  '\033[33m' + "Average Accurary Score" + \
                " : " +  str(sum(accuraries) / len(accuraries))  + '\033[0m' )


