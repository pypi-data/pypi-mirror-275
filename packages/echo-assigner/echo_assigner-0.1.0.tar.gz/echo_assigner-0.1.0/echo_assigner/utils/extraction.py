import music21 as m21
import numpy as np
from typing import Literal
from ..src.autoharmonizer.harmonizer import AutoHarmonizer

def notes(stream: m21.stream, division: float | int) -> list: # [区間内音階]*分割小節数　のリストを作成
    note = []
    div, div2 = [], []

    for i, measures in enumerate(stream[1]):
        for notes in measures:
            if isinstance(notes, m21.note.Note):
                if division == 0.5 and \
                   notes.offset < measures.quarterLength/2: # 前半(0.5)
                    div.append(notes.pitch.ps)
                elif division == 0.5 and \
                     notes.offset >= measures.quarterLength/2: # 後半(0.5)
                    div2.append(notes.pitch.ps)
                else:
                    div.append(notes.pitch.ps)
            
        if division >= 1 and i % division == division-1: # n小節ごとに分割(整数 >= 1)
            note.append(div)
            div = []
        
        elif division == 0.5: # 1小節を2分割(0.5)
            if len(div) == 0:
                div = [None]
            elif len(div2) == 0:
                div2 = [None]
            
            note.append(div)
            note.append(div2)
            div, div2 = [], []

    if len(div) > 0:
        note.append(div)
    elif len(div2) > 0:
        note.append(div2)

    return note


def mean_or_var(note: list, opt: Literal["mean", "var"]) -> list: # np.mean, np.varを使う
    assert opt in ["mean", "var"], "opt is mean or var"
    result = []

    for n in note:
        try:
            if opt == "mean":
                result.append(np.mean(n))
            elif opt == "var":
                result.append(np.var(n))
        except TypeError:
            result.append(None)
    return result


def mean_notesdif(notes: list) -> list: # 音階の変化量の平均
    notes_flatten = sum(notes, [])
    notes_shift = np.append(0, np.delete(notes_flatten, -1))
    notesdif_flatten = []

    for f,s in zip(notes_flatten, notes_shift):
        try:
            notesdif_flatten.append(f-s)
        except TypeError:
            notesdif_flatten.append(None)

    notesdif_flatten = notesdif_flatten[1:]
    
    notes_figure = [len(measure) for measure in notes]
    notes_dif , e = [], 0 # eは底数
    for f in notes_figure:
        try:
            slice = notesdif_flatten[e:e+f]
            if slice == []:
                notes_dif.append(0)
            else:
                notes_dif.append(np.mean(slice))
        except TypeError:
            notes_dif.append(0)
        finally:
            e += f

    return notes_dif


def pitch_class(stream: m21.stream, division: float | int) -> list: # pitchClassごとの音の長さの合計を計算
    pitchClass = []
    div, div2 = [0 for i in range(12)], [0 for i in range(12)]

    for i,measures in enumerate(stream[1]):
        for notes in measures:
            if isinstance(notes, m21.note.Note):
                if division == 0.5 and \
                    notes.offset < measures.quarterLength/2: # 前半(0.5)
                    div[notes.pitch.pitchClass] += notes.quarterLength
                elif division == 0.5 and \
                    notes.offset >= measures.quarterLength/2: # 後半(0.5)
                    div2[notes.pitch.pitchClass] += notes.quarterLength
                else:
                    div[notes.pitch.pitchClass] += notes.quarterLength

        if division >= 1 and i % division == division-1: # n小節ごとに分割(整数 >= 1)
            pitchClass.append(div)
            div = [0 for i in range(12)]

        elif division == 0.5: # 1小節を2分割(0.5)
            pitchClass.append(div)
            pitchClass.append(div2)
            div, div2 = [0 for i in range(12)], [0 for i in range(12)]
        
    if div != [0 for i in range(12)]:
        pitchClass.append(div)
    elif div2 != [0 for i in range(12)]:
        pitchClass.append(div2)

    return np.array(pitchClass).T


def presume_chord(part: m21.stream.Part, division: float | int) -> list: # division区間ごとにコードを推定
    chord_scales = []
    div, div2 = [], []

    for i, measures in enumerate(part):
        presume_obj = m21.stream.Measure()
        for notes in measures.flatten().notes:
            if division == 0.5 and \
                notes.offset < measures.quarterLength/2: # 前半(0.5)
                div.append(notes) # noteの集まりを形成 div -> measure
            elif division == 0.5 and \
                notes.offset >= measures.quarterLength/2: # 後半(0.5)
                notes.offset -= measures.quarterLength/2
                div2.append(notes) # noteの集まりを形成 div -> measure
            else:
                presume_obj.append(notes) # noteの集まりを形成
        if len(presume_obj):
            div.append(presume_obj) # measureの集まりを形成 div -> part

        if division >= 1 and i % division == division-1: # n小節ごとに分割(整数 >= 1)
            div_scales = AutoHarmonizer(m21.stream.Part(div)).get_scale_note()
            chord_scales.append(div_scales)
            div = []

        elif division == 0.5: # 1小節を2分割(0.5)
            div_scales = AutoHarmonizer(m21.stream.Part(m21.stream.Measure(div))).get_scale_note()
            div2_scales = AutoHarmonizer(m21.stream.Part(m21.stream.Measure(div2))).get_scale_note()
            
            # {'note': [note, note], 'scale': []} の状態
            if len(div2_scales["note"]) and len(div2_scales["scale"]) == 0:
                div2_scales["scale"] = [div_scales["scale"][-1] for _ in range(len(div2_scales["note"]))]

            chord_scales.append(div_scales)
            chord_scales.append(div2_scales)
            
            div, div2 = [], []

    # append残しがあった場合
    if len(div):
        div_scales = AutoHarmonizer(m21.stream.Part(div)).get_scale_note()
        chord_scales.append(div_scales)
    
    return chord_scales


def insert_zeros(array: list, exec_num: int) -> list: # 配列の各要素の次のインデックスに0を挿入
    for _ in range(exec_num):
        array = sum([[item, 0] for item in array],[])
    return array


def convert_array(stream: m21.stream, division: float | int) -> list: # 正解率を計算するための配列に変換
    
    # 1小説ごとに配列を構成
    per_measure_array = []

    for measure in stream[1]:
        # 1小節の中で最も細かいquarterlengthを取得
        lengths = []
        for n in measure.flat.notes:
            if n.quarterLength - int(n.quarterLength) == 0:
                lengths.append(n.quarterLength)
            else:
                after_dot = len(str(n.quarterLength).split(".")[1])
                # .x   -> 0.5   = 1/2
                # .xx  -> 0.25  = 1/4
                # .xxx -> 0.125 = 1/8
                
                if after_dot <= 5:
                    lengths.append(1/2**after_dot)
                else:
                    print(f"[WARNING] Note quarterLength is too small ;{n.quarterLength}")


        min_quarterlength = min(lengths)
        # min     -> array length -> index bias
        # 1       -> 4            -> 1
        # 0.5     -> 8            -> 2
        # 0.25    -> 16           -> 4

        measure_array = [0 for _ in range(int(4/min_quarterlength))]
        index_bias = 1 / min_quarterlength
        for n in measure.flat.notes:
            if isinstance(n, m21.note.Note):
                measure_array[int(n.offset * index_bias)] = n.pitch.midi
        
        per_measure_array.append(measure_array)

    # divisionで分割
    stream_array = []

    if division == 2:
        for n in range(0,len(per_measure_array),2):
            try:
                first_measure = per_measure_array[n]
                second_measure = per_measure_array[n+1]
            except IndexError:
                stream_array.append(per_measure_array[n])
            else:
                if len(first_measure) > len(second_measure):
                    insert_num = int(np.log2(len(first_measure)) - np.log2(len(second_measure)))
                    second_measure = insert_zeros(second_measure, insert_num)
                elif len(first_measure) < len(second_measure):
                    insert_num = int(np.log2(len(second_measure)) - np.log2(len(first_measure)))
                    first_measure = insert_zeros(first_measure, insert_num)
                
                if len(first_measure) != len(second_measure):
                    raise IndexError(f"[Error] Array conversion failed ({len(first_measure)},{len(second_measure)})")
                else:
                    stream_array.append([*first_measure, *second_measure])


    elif division == 1:
        stream_array = per_measure_array

    elif division == 0.5:
        for measure in per_measure_array:
            stream_array.append(measure[:int(len(measure)/2)])
            stream_array.append(measure[int(len(measure)/2):])
    
    return stream_array

