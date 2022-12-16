import random

lista = []
osztando = []


def fel():

    szam = int(input("Adj meg egy számot"))

    while szam < 5 or szam > 30:
        print("Hiba")
        szam = int(input("[5, 30] intervallumból válassz egy számot]"))
    osztando.append(szam)

    keresztnev = input("Add meg a keresztneved")
    teljesnev = input("Add meg a teljes neved")
    nev = teljesnev.split(" ")
    print(nev[0])
    print(keresztnev)

    szo = "as"

    while len(szo) < 3:
        szo = input("Írj egy hosszú szót")

    utolso = len(szo)-1

    if szo[0].upper() == szo[utolso].upper():
        print("Az első és utolsó betű EGYEZIK")
    else:
        print("Az első és utolsó NEM betű egyezik")

    if szo[1].upper() == szo[utolso].upper():
        print("A második és utolsó betű EGYEZIK")
    else:
        print("Az második és utolsó NEM betű egyezik")

    if szo[0] == szo[0].upper():
        print("Az első betű NAGYBETŰ")
    else:
        print("Az első betű NEM nagybetűs")


def fel2():
    i = 0
    szamok = ""
    while i < 5:
        vel = int(random.random()*21)-5
        szamok += f"{str(vel):>4},"
        i += 1
    print(szamok)


def fel3():
    szamok = [3, -5, 7]

    i = 97
    x = 1
    while i < 100:
        abc = str(chr(i))
        sor = abc + ",   " + str(x) + ". elem: " + str(szamok[x-1])
        print(sor)
        i += 1
        x += 1
    return szamok[0]


def otdbveletlen():
    osszeg = 0
    db = 0
    kicsi = 1000
    nagy = 0
    kicsihely = 0
    nagyhely = 0

    while len(lista) < 5:
        vel = int(random.random()*11)+5
        lista.append(vel)
        osszeg += vel

    i = 0
    while i < len(lista):
        if lista[i] % 3 == 0:
            db += 1
        if lista[i] < kicsi:
            kicsi = lista[i]
            kicsihely = i+1
        elif lista[i] > nagy:
            nagy = lista[i]
            nagyhely = i+1
        i += 1

    print(lista)
    atlag = osszeg / len(lista)
    print("összege:", osszeg)
    print("átlaga:", atlag)
    print(db, "db 3-mal osztható szám van benne")
    print("legkisebb helye / értéke:", kicsihely, "/", kicsi)
    print("legnagyobb helye / értéke:", nagyhely, "/", nagy)


def osztas():
    eredmeny = osztando[0] / lista[len(lista)-1]
    print(f"{osztando[0]} / {lista[len(lista)-1]} = {eredmeny:.2f}")

    osztani = fel3()
    eredmeny2 = osztani / lista[2]
    print(f"3 / {lista[2]} = {eredmeny2:.4f}")


def tizenharom():
    i = 0
    while i < len(lista) and lista[i] != 13:
        i += 1
    if i < len(lista):
        print(f"van benne 13-mas a {i+1}. helyen")
    else:
        print("nincs benne 13-mas")


def nagyobbtiznel():
    i = 0

    while i < len(lista) and lista[i] > 10:
        i += 1
    if i < len(lista):
        print("nem minden elem nagyobb, mint tíz")
    else:
        print("minden elem nagyobb, mint tíz")
