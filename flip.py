#!/usr/bin/python3

import sys

def main():
    print("Flip")

    # Argumentumok ellenőrzése
    if len(sys.argv) != 7:
    # Azért 7, mert a 0. indexű elemben a most futó fájl neve található, így 6 + 1 = 7
        print("Nem megfelelő számú argumentumot adtál meg!")
        return

    # Argumentumok változókhoz rendelése
    elolap   = sys.argv[1]
    hatlap   = sys.argv[2]
    cellap   = sys.argv[3]
    sor      = sys.argv[4]
    oszlop   = sys.argv[5]
    ini_fajl = sys.argv[6]

    # Előfeltétel vizsgálat
    if cellap != elolap and cellap != hatlap:
        print("None")
        return

if __name__ == "__main__":
    main()
