import random
bekertszam = 1
proba = "próba"

def beker_szam():
    global bekertszam

    szam = int(input("Adj meg egy számot!"))
    if szam > 30 or szam < 5:
        print("Hiba!")
    while szam > 30 or szam < 5:
        szam = int(input("Kérlek 5-30 közötti számot adj meg!"))

    print(f"A számod: {szam}.")

    bekertszam = szam


def nevkiiras():

    keresztnev = str(input("Add meg a keresztneved! "))
    teljes = str(input("Add meg a teljes neved (szóközzel elválasztva)!"))
    vezeteknev = ""

    i = 0
    while teljes[i] != " ":
        i += 1
    if i < len(teljes):
        vezeteknev = teljes[0:i]

    print(f"A vezetékneved: {vezeteknev}, keresztneved: {keresztnev}")


def beker_harombetus_szo():
    szo = str(input("Adj meg egy szót!"))

    while len(szo) < 3:
        szo = str(input("Kérlek legalább hárombetűs szót adj meg!"))

    hossz = len(szo)-1

    if szo[0] == szo[hossz]:
        print(f"Az első({szo[0]}) és utolsó({szo[hossz]}) betű megegyezik")
    else:
        print(f"Az első({szo[0]}) és utolsó({szo[hossz]}) betű nem egyezik meg")

    if szo[1] == szo[hossz]:
        print(f"A második({szo[1]}) és utolsó({szo[hossz]}) betű megegyezik")
    else:
        print(f"A második({szo[1]}) és utolsó({szo[hossz]}) betű nem egyezik meg")

    if szo[0] == szo[0].upper():
        print("Az első betű nagybetű")
    else:
        print("Az első betű nem nagy betű")


def veletlenszam():
    szamok = ""
    i = 0
    while i < 5:
        vel = int(random.random() * - 5) + 10
        if i == 4:
            szamok += str(vel)
        else:
            szamok += str(vel) + ", "
        i += 1
    print(szamok)


def lista_abc():

    lista = [3, -5, 7]

    i = 0
    while i < len(lista):

        print(chr(ord("a") + i), f"{i+1:>3}. elem: {lista[i]:>2}")
        i += 1


def veletlenlistaban():
    szamok = []

    i = 0
    while i < 5:
        vel = int(random.random() * 5) + 10
        szamok.append(vel)
        i += 1
    print(szamok)

    osztas_eredmenye = bekertszam / szamok[-1]
    print(f"{bekertszam} / {szamok[-1]} = {osztas_eredmenye:.2f}")


"""16.	Generáljunk 5 db véletlenszámot [5; 15] intervallumban, 
egy listába rakva jelenítsük meg őket

17.	A 3. feladat bekért számát osszuk el a generált lista utolsó elemével,
írjuk ki 2 tizedes pontossággal az eredményt

18.	A 14. feladat 1. elemét(3) osszuk el a generált lista (16. feladat) középső elemével,
írjuk ki 4 tizedes pontossággal az eredményt

19.	Mennyi a generált lista (16. feladat) elemeinek összege?
20.	Mennyi a generált lista (16. feladat) elemeinek átlaga?
21.	Hány darab hárommal osztható szám van benne?
22.	Melyik helyen van a legnagyobb és a legkisebb szám?
23.	Van benne 13? Ha megvan a válasz, akkor álljon le a vizsgálat!
24.	Minden elem nagyobb 10? Amint kiderül, hogy nem, álljon le a vizsgálat!
25.	Van benne / hány darab tökéletes számot tartalmaz a lista?
26.	Van benne / hány darab prímszámot tartalmaz a lista?
A feladatok készüljenek el metódusokba szervezve is, 
a meglévőt kell kiszervezni eljárásokba! 
A metódusoknak ne legyen paramétere, a több eljárásban is használt
változókat szervezzük ki az osztály szintjén elérhetőre!
Az utolsó kettő feladatot függvényekkel oldjuk meg!
"""