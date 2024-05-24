import sqlite3, os
import numpy as np

from ..models.pitchclassModel import Pc_Data
from ..config import *

class pitchclassDB:
    def __init__(self, database_path :str = f"{DATABASE_PATH}/sample", maxdivision:int = 2):
        self.database_path = database_path
        self.midis = os.listdir(database_path)
        self.divisions = [0.5, *list(range(1, maxdivision+1))]

        self.con = sqlite3.connect(f"{DATABASE_PATH}/pitchClassData.sqlite")
        self.cur = self.con.cursor()

    def reload(self) -> None: # DB 更新
        for d in self.divisions:
            self.cur.execute(f'DROP TABLE IF EXISTS "pitchclass-{d}";')
            self.cur.execute(f'CREATE TABLE "pitchclass-{d}"(\
                            midi INT NOT NULL, \
                            measure FLOAT NOT NULL, \
                            C FLOAT, \
                            Cis FLOAT, \
                            D FLOAT, \
                            Dis FLOAT, \
                            E FLOAT, \
                            F FLOAT, \
                            Fis FLOAT, \
                            G FLOAT, \
                            Gis FLOAT, \
                            A FLOAT, \
                            Ais FLOAT, \
                            B FLOAT);')

            for midiname in self.midis:
                if midiname.endswith(".mid"):
                    stream = Pc_Data(self.database_path + "/" + midiname, int(midiname.split(".")[0]), d)
                    vectors = [tuple(s) for s in stream.vector]
                    self.cur.executemany(f'INSERT INTO "pitchclass-{d}" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);', vectors)
                    self.con.commit()

        print('\033[33m' +  "[Complete!]"  + '\033[0m' +
              '\033[36m' +  " Database reloaded." + '\033[0m')
        

    def reference(self, division: float | int) -> list: # DB 参照
        self.cur.execute(f'SELECT midi, measure FROM "pitchclass-{division}";')
        labels =  [list(s) for s in self.cur.fetchall()] # DBラベル

        self.cur.execute(f'SELECT C, Cis, D, Dis, E, F, Fis, G, Gis, A, Ais, B \
                          FROM "pitchclass-{division}";')
        vectors = np.array([list(s) for s in self.cur.fetchall()]) # DBベクトル
        return vectors, labels



if __name__=="__main__":
    db = pitchclassDB()
    db.reload()