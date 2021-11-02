#!/usr/bin/python3

import sys
import csv

tabla = []

def tabla_ini(ini_fajl):
    with open(ini_fajl, 'r') as f:
        r = csv.reader(f)
        for s in r:
            tabla.append(s)

def main():
    print("Flip")

    # Argumentumok ellenőrzése
    if len(sys.argv) != 7:
    # Azért 7, mert a 0. indexű elemben a most futó fájl neve található, így 6 + 1 = 7
        print("Nem megfelelő számú argumentumot adtál meg!")
        return

    # Argumentumok változókhoz rendelése
    sor      = sys.argv[1]
    oszlop   = sys.argv[2]
    elolap   = sys.argv[3]
    hatlap   = sys.argv[4]
    cellap   = sys.argv[5]
    ini_fajl = sys.argv[6]

    # Előfeltétel vizsgálat
    if cellap != elolap and cellap != hatlap:
        print("None")
        return

    # Tábla inicializálása
    tabla_ini(ini_fajl)

if __name__ == "__main__":
    main()
