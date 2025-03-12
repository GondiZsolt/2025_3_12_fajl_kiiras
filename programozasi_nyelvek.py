"""1. Feladat
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát, és másold át azt egy fájlba úgy, hogy abba már csak a nyelv és az évszám kerüljön!"""

with open("Timeline_of_programming_languages.txt", "r", encoding="utf-8") as f, \
    open("Timeline_of_programming_languages_copy.txt", "w", encoding="utf-8") as celfajl:

    for sor in f:
        adatok = sor.strip().split(";")
        year = adatok[0]
        language = adatok[1]

        print(year, language, file=celfajl)