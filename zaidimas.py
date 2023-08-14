# žaidimo lenta.
from bendravimas_su_zaidejais import *
x_žaidėjas = ""
o_žaidėjas = ""

lenta_sk = ["1","2","3",
            "4","5","6",
            "7","8","9"]

def lenta ():
    print((lenta_sk[0] + "|" + lenta_sk[1] + "|" + lenta_sk[2]))
    print((lenta_sk[3] + "|" + lenta_sk[4] + "|" + lenta_sk[5]))
    print((lenta_sk[6] + "|" + lenta_sk[7] + "|" + lenta_sk[8]))
    print("______")

dabar_žaidžia = "X"
laimėtojas = None
žaidimas_tęsesi = True

def ar_laimėjo():
    global laimėtojas
    global žaidimas_tęsesi

    if lenta_sk[0] == lenta_sk[1] == lenta_sk[2] or\
       lenta_sk[3] == lenta_sk[4] == lenta_sk[5] or\
       lenta_sk[6] == lenta_sk[7] == lenta_sk[8] or\
       lenta_sk[0] == lenta_sk[3] == lenta_sk[6] or\
       lenta_sk[1] == lenta_sk[4] == lenta_sk[7] or\
       lenta_sk[2] == lenta_sk[5] == lenta_sk[8] or\
       lenta_sk[0] == lenta_sk[4] == lenta_sk[8] or\
       lenta_sk[2] == lenta_sk[4] == lenta_sk[6]:
        laimėtojas = dabar_žaidžia
        žaidimas_tęsesi = False

def skelbti_laimėtoją():
    global laimėtojas, x_žaidėjas, o_žaidėjas
    if laimėtojas == "X":
        print(f"Laimėjo žaidėjas X ({x_žaidėjas})!")
    elif laimėtojas == "O":
        print(f"Laimėjo žaidėjas O ({o_žaidėjas})!")
    else:
        print("Lygiosios!")

def žaisti():
    global dabar_žaidžia, x_žaidėjas, o_žaidėjas
    while žaidimas_tęsesi:
        lenta()
        pasirinkti_vieta()
        ar_laimėjo()
        dabar_žaidžia = "X" if dabar_žaidžia == "O" else "O"
    lenta()
    skelbti_laimėtoją()

def pasirinkti_vieta():
    global laimėtojas
    while True:
        pasirinkta_vieta = input(f"Žaidėjas {dabar_žaidžia}, pasirinkite langelį (1-9): ")
        if pasirinkta_vieta.isdigit() and 1 <= int(pasirinkta_vieta) <= 9:
            pasirinkta_vieta = int(pasirinkta_vieta) - 1
        # else:
            # print("jūsų pasirinkimas būtinai turi būti laisvas skaičius nuo 1 iki 9, bandykite dar kartą!")
            if lenta_sk[pasirinkta_vieta] == "X" or lenta_sk[pasirinkta_vieta] == "O":
                print("Šis langelis jau užimtas. Bandykite dar kartą.")
            else:
                lenta_sk[pasirinkta_vieta] = dabar_žaidžia
                ar_laimėjo()
            break
    else:
        print("Netinkamas pasirinkimas. Pasirinkite skaičių nuo 1 iki 9.")


if __name__ == "__main__":
    žaisti1()
    # skelbti_laimėtoją()