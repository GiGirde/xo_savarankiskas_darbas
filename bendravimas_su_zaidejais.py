# čia yra bendravimas su žaidėju
from zaidimas import lenta

print("Sveiki! Čia yra žaidimas XO!")
print("--------------------------------")

x_žaidėjas = (input("Žaidėjas X - Prisistatykite: "))
o_žaidėjas = (input("Žaidėjas O - Prisistatykite: "))
print("--------------------------------")
print("Malonu, " + x_žaidėjas, "ir " + o_žaidėjas, "susipažinti")
print("--------------------------------")
sutikimas= input("Ar norite pradėti žaidimą? pasirinkite 'taip' arba 'ne'")
print("************************************")

if sutikimas.lower() == "taip":
    print("ŽAIDIMASD PRASIDEDA")
    print("************************************")

    lenta()
else:
    print("labai gaila")
