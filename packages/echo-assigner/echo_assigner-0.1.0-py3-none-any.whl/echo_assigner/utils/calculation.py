import numpy as np
from typing import Literal
from scipy.spatial import distance

# Cメジャーとの距離計算
def keyC_dif(key: int) -> int:
    if 66 <= key <= 71:
        key -= 12
    key_dif = key - 60
    return key_dif

# さまざまな距離計算手法を定義
def distfunction(a: np.array, b: np.array, distmethod: Literal[0,1,2,3,4]) -> distance: 
    # 欠損値を平均値で埋める (model=pitchclassのときしか使わない)
    if None in a:
        none_mean = np.mean([v for v in a if v is not None])
        a = [none_mean if v is None else v for v in a]
    if None in b:
        none_mean = np.mean([v for v in b if v is not None])
        b = [none_mean if v is None else v for v in b]

    # 以下距離計算
    if distmethod==0: # ユークリッド距離
        dist =  distance.euclidean(a, b)
        method = "Euclidean"
    
    elif distmethod==1: # チェビシェフ距離
        dist = distance.chebyshev(a, b)
        method = "Chebyshev"
    
    elif distmethod==2: # マンハッタン距離
        dist = distance.cityblock(a, b)
        method = "Manhattan"
    
    elif distmethod==3: # ミンコフスキー距離
        dist = distance.minkowski(a, b)
        method = "Minkowski"
    
    elif distmethod==4: # コサイン類似度
        a = a / np.linalg.norm(a) # 正規化
        b = b / np.linalg.norm(b)
        dist = distance.cosine(a, b)
        method = "Cosine"

    return dist, method


# 配列の各要素の次のインデックスに0を挿入
def insert_zeros(array: list, exec_num: int) -> list:
    for _ in range(exec_num):
        array = sum([[item, 0] for item in array],[])
    return array


# 正解率を計算する
def accuraryfunction(selected: list, input: list) -> float:
    if len(selected) > len(input):
        input = insert_zeros(input, int(np.log2(len(selected)-np.log2(len(input)))))
    elif len(selected) < len(input):
        selected = insert_zeros(selected, int(np.log2(len(input)-np.log2(len(selected)))))

    return sum(1 for s, i in zip(selected, input) if s == i) / len(input)