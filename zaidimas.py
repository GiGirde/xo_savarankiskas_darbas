import time

x_žaidėjas = ""
o_žaidėjas = ""


def žaisti1():
    global lenta_sk, x_žaidėjas, o_žaidėjas
    print("Sveiki! Čia yra žaidimas XO!")
    print("--------------------------------")
    time.sleep(2)
    x_žaidėjas = input("Žaidėjas X - Prisistatykite: ")
    o_žaidėjas = input("Žaidėjas O - Prisistatykite: ")

    print("--------------------------------")
    print(f"Malonu, {x_žaidėjas} ir {o_žaidėjas} susipažinti")
    time.sleep(1)
    print("--------------------------------")

    sutikimas = input("Ar norite pradėti žaidimą? pasirinkite 'taip' arba 'ne'")
    print("************************************")

    if sutikimas.lower() == "taip":
        time.sleep(1)
        print("ŽAIDIMASD PRASIDEDA")
        print("************************************")
        time.sleep(1)
        žaisti()
        pakartoti_žaidimą()
    else:
        print("Labai gaila, galbūt kitą kartą!")


lenta_sk = ["1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"]


def lenta():
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

    if lenta_sk[0] == lenta_sk[1] == lenta_sk[2] or \
            lenta_sk[3] == lenta_sk[4] == lenta_sk[5] or \
            lenta_sk[6] == lenta_sk[7] == lenta_sk[8] or \
            lenta_sk[0] == lenta_sk[3] == lenta_sk[6] or \
            lenta_sk[1] == lenta_sk[4] == lenta_sk[7] or \
            lenta_sk[2] == lenta_sk[5] == lenta_sk[8] or \
            lenta_sk[0] == lenta_sk[4] == lenta_sk[8] or \
            lenta_sk[2] == lenta_sk[4] == lenta_sk[6]:
        laimėtojas = dabar_žaidžia
        žaidimas_tęsesi = False
    elif all(langelis == "X" or langelis == "O" for langelis in lenta_sk):
        laimėtojas = "Lygiosios"
        žaidimas_tęsesi = False


laimėjimų_skaicius = {'X': 0, 'O': 0}


def skelbti_laimėtoją():
    global laimėtojas, x_žaidėjas, o_žaidėjas
    if laimėtojas == "X":
        print("")
        print(f"Laimėjo žaidėjas X ({x_žaidėjas})!")
        print("")
        laimėjimų_skaicius['X'] += 1
    elif laimėtojas == "O":
        print("")
        print(f"Laimėjo žaidėjas O ({o_žaidėjas})!")
        print("")
        laimėjimų_skaicius['O'] += 1
    else:
        print("")
        print("Lygiosios!")
        print("")


def žaisti():
    global dabar_žaidžia, x_žaidėjas, o_žaidėjas
    while žaidimas_tęsesi:
        lenta()
        pasirinkti_vieta()
        ar_laimėjo()
        dabar_žaidžia = "X" if dabar_žaidžia == "O" else "O"
    lenta()
    skelbti_laimėtoją()


def pakartoti_žaidimą():
    while True:
        pasirinkimas = input("Ar norite žaisti iš naujo? (taip/ne): ")
        if pasirinkimas.lower() == "taip":
            time.sleep(1)
            global lenta_sk, laimėtojas, žaidimas_tęsesi
            lenta_sk = ["1", "2", "3",
                        "4", "5", "6",
                        "7", "8", "9"]
            laimėtojas = None
            žaidimas_tęsesi = True
            žaisti()
        elif pasirinkimas.lower() == "ne":
            time.sleep(1)
            print("")
            print(f"Ačiū,{x_žaidėjas} ir {o_žaidėjas}, kad žaidėte!\nIki kitų kartų!")
            print("--------------------------------")
            print("Jūsų rezultatas yra:")
            for žaidėjas, laimėjimai in laimėjimų_skaicius.items():
                print(f"{žaidėjas}: {laimėjimai} laimėjimai")

            break
        else:
            print("Netinkamas pasirinkimas. Pasirinkite 'taip' arba 'ne'.")


def pasirinkti_vieta():
    global laimėtojas
    while True:
        pasirinkta_vieta = input(f"Žaidėjas {dabar_žaidžia}, pasirinkite langelį (1-9): ")
        if pasirinkta_vieta.isdigit() and 1 <= int(pasirinkta_vieta) <= 9:
            pasirinkta_vieta = int(pasirinkta_vieta) - 1
            if lenta_sk[pasirinkta_vieta] == "X" or lenta_sk[pasirinkta_vieta] == "O":
                print("Šis langelis jau užimtas. Bandykite dar kartą.")
            else:
                lenta_sk[pasirinkta_vieta] = dabar_žaidžia
                ar_laimėjo()
            break
        else:
            print("Jūsų pasirinkimas yra netinkamas. Pasirinkite laisvą skaičių nuo 1 iki 9.")
            print("...................")


if __name__ == "__main__":
    žaisti1()
