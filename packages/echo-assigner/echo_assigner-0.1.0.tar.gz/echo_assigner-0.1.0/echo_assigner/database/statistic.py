import sqlite3
import numpy as np

from ..models.statisticModel import St_Data
from ..config import *

class statisticDB:
    def __init__(self, database_path :str = f"{DATABASE_PATH}/sample", maxdivision:int = 2):
        self.database_path = database_path
        self.midis = os.listdir(database_path)
        self.divisions = [0.5, *list(range(1, maxdivision+1))]

        self.con = sqlite3.connect(f"{DATABASE_PATH}/statisticData.sqlite")
        self.cur = self.con.cursor()

    def reload(self) -> None: # DB 更新
        for d in self.divisions:
            self.cur.execute(f'DROP TABLE IF EXISTS "statistic-{d}";')
            self.cur.execute(f'CREATE TABLE "statistic-{d}" (\
                            midi INT NOT NULL, \
                            measure FLOAT NOT NULL, \
                            first_note FLOAT, \
                            mean_notes FLOAT, \
                            var_notes FLOAT,\
                            mean_notesdif FLOAT, \
                            density FLOAT);')

            for midiname in self.midis:
                if midiname.endswith(".mid"):
                    stream = St_Data(self.database_path + "/" + midiname, int(midiname.split(".")[0]), d)
                    vectors = [tuple(s) for s in stream.vector if None not in s]
                    self.cur.executemany(f'INSERT INTO "statistic-{d}" VALUES (?,?,?,?,?,?,?);', vectors)
                    self.con.commit()

        print('\033[33m' +  "[Complete!]"  + '\033[0m' +
              '\033[36m' +  " Database reloaded." + '\033[0m')
        

    def reference(self, division: float | int) -> list: # DB 参照
        self.cur.execute(f'SELECT midi, measure FROM "statistic-{division}";')
        labels =  [list(s) for s in self.cur.fetchall()] # DBラベル

        self.cur.execute(f'SELECT first_note, mean_notes, var_notes, \
                         mean_notesdif, density FROM "statistic-{division}";')
        vectors = np.array([list(s) for s in self.cur.fetchall()]) # DBベクトル
        return vectors, labels



if __name__=="__main__":
    db = statisticDB()
    db.reload()
        
