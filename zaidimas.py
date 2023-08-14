# žaidimo lenta.
from bendravimas_su_zaidejais import *

lenta_sk = ["1","2","3",
            "4","5","6",
            "7","8","9"]

def lenta ():
    print((lenta_sk[0] + "|" + lenta_sk[1] + "|" + lenta_sk[2]))
    print((lenta_sk[3] + "|" + lenta_sk[4] + "|" + lenta_sk[5]))
    print((lenta_sk[6] + "|" + lenta_sk[7] + "|" + lenta_sk[8]))

# lenta()

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
    laimėtojas = dabar_žaidžia
    žaidimas_tęsesi = False


def žaisti():
    # dabar_žaidžia keičia žaidėjų eiliškumą
    global dabar_žaidžia
    #  prasideda begalinis ciklas (loop), kuris vykdomas tol, kol žaidimas_tęsesi yra True.
    while žaidimas_tęsesi:
        # spausdina lenta su esamais įrašais.
        lenta()
        # pasirinkti_vieta(): Ši eilutė iškviečia funkciją pasirinkti_vieta(), kuri leidžia dabar einančiam žaidėjui pasirinkti vietą (langelį) ant lentos.
        pasirinkti_vieta()
        # ar_laimėjo(): Ši eilutė iškviečia funkciją ar_laimėjo()
        ar_laimėjo()
        # Jei dabar_žaidžia yra "X", tai pakeičiama į "O", o jei ne, tai pakeičiama į "X"
        dabar_žaidžia = "X" if dabar_žaidžia == "X" else "O"

def pasirinkti_vieta():
    #  Ši eilutė nurodo, kad funkcija gali pakeisti laimėtojas kintamojo reikšmę, jei bus laimėtojas.
    global laimėtojas
    # Ši eilutė įkelia žaidėjo pasirinkimą - numerį nuo 1 iki 9 - į pasirinkta_vieta
    pasirinkta_vieta = input(f"Žaidėjas {dabar_žaidžia}, pasirinkite langelį (1-9): ")
    # patikrina, ar įvestas žaidėjo pasirinkimas yra skaičius ir ar jis yra tarp 1 ir 9
    if pasirinkta_vieta.isdigit() and 1 <= int(pasirinkta_vieta) <= 9:
        # ši eilutė konvertuoja jį į sveikąjį skaičių ir sumažina vienetu, nes žaidimo lentos indeksai pradedami nuo 0.
        pasirinkta_vieta = int(pasirinkta_vieta) - 1
        #  tikrina, ar pasirinktas langelis ant lentos jau užimtas
        if lenta_sk[pasirinkta_vieta] == "X" or lenta_sk[pasirinkta_vieta] == "O":
            #
            print("Šis langelis jau užimtas. Bandykite dar kartą.")
        else:
            # Ši eilutė įrašo dabar einančio žaidėjo simbolį ("X" arba "O") į pasirinktą langelį ant žaidimo lentos.
            lenta_sk[pasirinkta_vieta] = dabar_žaidžia
            ar_laimėjo()
    else:
        # Jei įvestas pasirinkimas nėra tinkamas skaičius tarp 1 ir 9.
        print("Netinkamas pasirinkimas. Pasirinkite skaičių nuo 1 iki 9.")
    lenta()

if __name__ == "__main__":
    žaisti1()