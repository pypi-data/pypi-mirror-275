import music21 as m21
import numpy as np

from ..utils.calculation import *
from ..config import *
from ..models.statisticModel import St_Input
from ..models.pitchclassModel import Pc_Input
from ..database.statistic import statisticDB

class create:
    def __init__(self, model: St_Input | Pc_Input, distmethod: Literal[0,1,2,3,4], logs: bool, division: float | int):
        self.model = model
        self.model_vector = model.vector
        self.distmethod = distmethod
        self.division = division
        self.logs = logs


    def score(self, return_vector: bool = False) -> list: # 類似度計算
        if isinstance(self.model, St_Input):
            self.vectors, self.labels = statisticDB().reference(self.division)
        elif isinstance(self.model, Pc_Input):
            pass
            #self.vectors, self.labels = pitchclassDB().reference(division)
        
        dist = np.array([[distfunction(d,i,self.distmethod)[0] # 距離計算
                        for d in self.vectors] # dataset midi
                        for i in self.model_vector]) # intput midi

        if self.distmethod == 4:  # コサインのときはargmaxにする必要がある
            label_info = np.array([ self.labels[i]
                                    for i in [np.argmax(d) 
                                    for d in dist]]).T.tolist()
        else:
            label_info = np.array([ self.labels[i]
                                    for i in [np.argmin(d) 
                                    for d in dist]]).T.tolist()
            
        if return_vector:
            if self.distmethod == 4: # コサインのときはargmaxにする必要がある
                vector_info = np.array([ self.vectors[i]
                                        for i in [np.argmax(d) 
                                        for d in dist]])
            else:
                vector_info = np.array([ self.vectors[i]
                                        for i in [np.argmin(d) 
                                        for d in dist]])
            
            return dist, label_info, vector_info

        else:
            return dist, label_info


    def give_measures(self) -> list: # [measure, measure, ...]と、全notesのスケールのリストを作成
        part_contents = [] # partの中身
        notes_scales = [] # notesごとのスケール(figure)
        ct, measure = 0, m21.stream.Measure() # 半小節のときだけしか使わない
        label_info = self.score()[1]
        
        for midiNum, measureNum in zip(label_info[0], label_info[1]):
            accompaniment = m21.converter.parse(f"{DATABASE_PATH}/{int(midiNum)}.mid")[2]# 伴奏stream
            print('\033[34m' +  f"[{int(midiNum)}-{measureNum}]"  + '\033[0m' +
                    '\033[36m' +  " fetching..." + '\033[0m') if self.logs else None
            
            notes_scales += statisticDB().get_scales(self.division, int(midiNum), measureNum) # midiとmeasureからscalesを取得
            
            if self.division >= 1: # 1小節以上の場合
                for n in range(int(measureNum), int(measureNum + self.division)): # 小節の数だけ伴奏を追加
                    measure = m21.stream.Measure() # measureNum = 4, division = 2のとき、4,5小節目をコピー
                    for item in accompaniment[n].flatten():
                        if isinstance(item, (m21.note.Note, m21.chord.Chord, m21.note.Rest, m21.stream.Voice)):
                            measure.insert(item.offset, item)
                    part_contents.append(measure)

            elif self.division == 0.5: # 半小節の場合
                for item in accompaniment[int(measureNum)].flatten():
                    if measureNum - int(measureNum) == 0.5: # .5のとき (offset:0.5以降をappend)
                        if isinstance(item, (m21.note.Note, m21.chord.Chord, m21.note.Rest, m21.stream.Voice)) \
                            and item.offset >= 2.0:
                            if ct == 0: # offset0からappendする場合
                                if len(measure)==0 and item.offset != 2.0: # 最初の音符が0からはじまらない場合
                                    measure.insert(0, m21.note.Rest(quarterLength=item.offset-2.0))
                                
                                measure.insert(item.offset-2.0, item)
                            else:
                                measure.insert(item.offset, item)

                    else: # 整数のとき(offset:0以降をappend)
                        if isinstance(item, (m21.note.Note, m21.chord.Chord, m21.note.Rest, m21.stream.Voice)) \
                            and item.offset < 2.0:
                            if ct == 1: # offset0.5からappendする場合
                                measure.insert(item.offset+2.0, item)
                            else:
                                measure.insert(item.offset, item)
                
                ct+=1
                if ct==2: # measureが埋まった時にpart_contentsへappend
                    part_contents.append(measure)
                    measure = m21.stream.Measure()
                    ct = 0
        
        if len(m21.stream.Part(part_contents[:self.model.length]).flatten().notes) < len(notes_scales):
            notes_scales = notes_scales[:len(m21.stream.Part(part_contents[:self.model.length]).flatten().notes)]

        return part_contents[:self.model.length], notes_scales


    def setup_part(self) -> m21.stream.Part: # partの初期設定
        part_measures, original_scales = self.give_measures()

        part = m21.stream.Part(part_measures) # partの作成

        partInfo = [m21.clef.BassClef(), # ヘ音記号
                    m21.meter.TimeSignature(f'{self.model.beat}/4'), # 拍子
                    m21.tempo.MetronomeMark(number=self.model.bpm), # テンポ
                    m21.instrument.Piano(), # 楽器
                    m21.key.KeySignature(0)] # 調符
        for i in partInfo:
            i.offset = 0
            part[0].insert(0, i) # partの最初にinfoを追加
        part[-1].append(m21.bar.Barline('final')) # 最後に小節線を追加

        for i,m in enumerate(part): # 小節にoffsetとnumberを追加
            m.offset = i * self.model.beat
            m.number = i+1
        
        key_dif = keyC_dif(self.model.key)
        part.transpose(key_dif, inPlace=True) # もとのキーに戻す
        
        transposed_scales = []
        for scale in original_scales:
            now_scale = m21.harmony.ChordSymbol(scale)
            now_scale.transpose(key_dif, inPlace=True)
            transposed_scales.append(now_scale.figure)


        print('\033[33m' +  "[Done]"  + '\033[0m' +
                '\033[32m' +  " AcPart Created." + '\033[0m') if self.logs else None
        
        return part, transposed_scales


    def shift_notes(self): # noteのスケールをoriginal -> newに変換
        created_part, original_scales = self.setup_part()
        new_scales = self.model.harmonizer.get_scale_note(created_part)["scale"]
        
        remove_notes_of_recurse = []

        assert  len(original_scales) == len(new_scales) == len(created_part.flatten().notes), \
                f"[Error] The number of notes is different. ({len(original_scales)}, {len(new_scales)}, {len(created_part.flatten().notes)})"
        
        for note_num in range(len(original_scales)):
            root = m21.harmony.ChordSymbol(original_scales[note_num]).root().name

            if "m" in original_scales[note_num]:
                original_scale = m21.scale.HarmonicMinorScale(root)
            else:
                original_scale = m21.scale.MajorScale(root)

            if "m" in new_scales[note_num]:
                new_scale = m21.scale.HarmonicMinorScale(root)
            else:
                new_scale = m21.scale.MajorScale(root)
            
            note = created_part.flat.notes[note_num]

            if isinstance(note, m21.note.Note):
                scaleDegree = original_scale.getScaleDegreeFromPitch(note)
                if scaleDegree:
                    octave = note.octave
                    note.pitch = m21.pitch.Pitch(new_scale.getPitches()[scaleDegree-1], octave=octave)
                else:
                    remove_notes_of_recurse.append(note)
                
            elif isinstance(note, m21.chord.Chord):
                for chord_note in note:
                    scaleDegree = original_scale.getScaleDegreeFromPitch(chord_note)
                    if scaleDegree:
                        octave = chord_note.octave
                        chord_note.pitch = m21.pitch.Pitch(new_scale.getPitches()[scaleDegree-1], octave=octave)
                    else:
                        note.remove(chord_note)
        
        #print(remove_notes_of_recurse) # todo:どうremoveするかを考える

        return created_part


    def fit_stream(self) -> m21.stream.Stream: # partをstreamに適応
        created_part = self.shift_notes()

        for measures in created_part:
            for note in measures.flatten().notes:
                note.volume.velocity = self.model.velocity
        
        self.model.stream.append(created_part)

        print('\033[33m' +  "[Complete!]"  + '\033[0m' +
            '\033[32m' +  " Stream Converted." + '\033[0m') if self.logs else None
        
        return self.model.stream