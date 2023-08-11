# žaidimo lenta.
from bendravimas_su_zaidejais import *
lenta_sk = ["1","2","3",
            "4","5","6",
            "7","8","9"]

def lenta ():
    print((lenta_sk[0] + "|" + lenta_sk[1]+"|" + lenta_sk[2]))
    print((lenta_sk[3] + "|" + lenta_sk[4] + "|" + lenta_sk[5]))
    print((lenta_sk[6] + "|" + lenta_sk[7] + "|" + lenta_sk[8]))

lenta()

dabar_žaidžia = "x"
laimėtojas = None
žaidimas_tęsesi = True

def ar_laimėjo():
    global laimėtojas
    global žaidimas_tęsesi

if lenta_sk[0] == lenta_sk[2] == lenta_sk[3] or\
    lenta_sk[0] == lenta_sk[4] == lenta_sk[8] or\
    lenta_sk[3] == lenta_sk[4] == lenta_sk[5] or\
    lenta_sk[6] == lenta_sk[7] == lenta_sk[8] or\
    lenta_sk[2] == lenta_sk[4] == lenta_sk[8] or\
    lenta_sk[0] == lenta_sk[3] == lenta_sk[6] or\
    lenta_sk[1] == lenta_sk[4] == lenta_sk[7] or\
    lenta_sk[2] == lenta_sk[5] == lenta_sk[8]:
    laimėtojas = dabar_zaidzia
    žaidimas_tęsesi = False
