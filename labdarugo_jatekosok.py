"""
Olvasd be a labdarugok.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány játékos szerepel a fájlban?
2. Melyik játékos szerezte a legkevesebb gólt?
3. Melyik játékos szerzett a legtöbb gólt?
4. Ki játszott a legtöbb mérkőzést?
5. Átlagosan hány gólt szerzett egy játékos?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerzett a legtöbb gólt? (feltételezve, hogy egy játékos csak egy csapatban játszott)


A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""

# Fájl beolvasása
labdarugok = []
with open('beolvasando_adatok/labdarugok.txt', 'r', encoding='utf-8') as f:
    next(f)
    for sor in f:
        adatok = sor.strip().split(';')
        labdarugo = {'nev': adatok[0], 'csapat': adatok[1], 'gol': int(adatok[2]), 'merkozesek': int(adatok[3])}
        labdarugok.append(labdarugo)

# Kiválogató függvények --> csak hogy ne kelljen 4-szer leírni ugyanazt :D
def legtobb(adat: str):
    vizsgalando = labdarugok[0]
    for labdarugo in labdarugok:
        if labdarugo[adat] > vizsgalando[adat]:
            vizsgalando = labdarugo
    return vizsgalando["nev"]

def legkevesebb(adat: str):
    vizsgalando = labdarugok[0]
    for labdarugo in labdarugok:
        if labdarugo[adat] < vizsgalando[adat]:
            vizsgalando = labdarugo
    return vizsgalando["nev"]



# 1. feladat
osszes_jatekos = len(labdarugok)

# 2. feladat
legkevesebb_gol = legkevesebb("gol")

# 3. feladat
legtobb_gol = legtobb("gol")

# 4. feladat
legtobb_merkozes = legtobb("merkozesek")

# 5. feladat
osszes_gol = 0
for labdarugo in labdarugok:
    osszes_gol += labdarugo["gol"]

atlag_gol = osszes_gol / osszes_jatekos


# Létrehozzuk a mappát, ha még nem létezik.
from pathlib import Path
Path("kiirt_adatok").mkdir(exist_ok=True)

with open('kiirt_adatok/statisztika.txt', 'w', encoding='utf-8') as c:
    c.write(f"A beolvasott fájlban összesen {osszes_jatekos} játékos szerepel.\n")
    c.write(f"A legkevesebb gólt szerző játékos: {legkevesebb_gol}\n")
    c.write(f"A legtöbb gólt szerző játékos: {legtobb_gol}\n")
    c.write(f"A legtöbb mérkőzést játszó játékos: {legtobb_merkozes}\n")
    c.write(f"Az átlagos gólszám: {atlag_gol:.2f}")

if Path("kiirt_adatok/statisztika.txt").exists:
    print("A statisztika.txt fájl létrejött, a program kilép.")
else:
    print("A fájl nem jött létre. A program kilép.")