#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Pál Polonkai
"""

import sys
import csv
import search

tabla = []
cel_tabla = []

# Táblainicializálása és a céltábla elkészítése
def tabla_ini(sor, oszlop, cellap, ini_fajl):
    with open(ini_fajl, 'r') as f:
        r = csv.reader(f)
        for s in r:
            tabla.append(s)
    for i in range(sor):
        cel_tabla.append([cellap for j in range(oszlop)])

# Cseréhez segédfüggvény - mindig a másikat adja vissza:
def masikat(x, a, b):
    if x == a:
        return b
    elif x == b:
        return a
    return x

# Csere implementálása
def csere(tabla, sor, oszlop, i, j, elolap, hatlap):
    # Önmaga cserélése
    tabla[i][j] = masikat(tabla[i][j], elolap, hatlap)

    # Felette levő cserélése (ha van)
    if i - 1 >= 0:
        tabla[i - 1][j] = masikat(tabla[i - 1][j], elolap, hatlap)

    # Jobbra levő cserélése (ha van)
    if j + 1 < oszlop:
        tabla[i][j + 1] = masikat(tabla[i][j + 1], elolap, hatlap)

    # Alatta levő cserélése (ha van)
    if (i + 1) < sor:
        tabla[i + 1][j] = masikat(tabla[i + 1][j], elolap, hatlap)

    # Balra levő cserélése (ha van)
    if j - 1 >= 0:
        tabla[i][j - 1] = masikat(tabla[i][j - 1], elolap, hatlap)

def main():
    print("Flip")

    # Argumentumok ellenőrzése
    if len(sys.argv) != 7:
    # Azért 7, mert a 0. indexű elemben a most futó fájl neve található, így 6 + 1 = 7
        print("Nem megfelelő számú argumentumot adtál meg!")
        return

    # Argumentumok változókhoz rendelése
    sor      = int(sys.argv[1])
    oszlop   = int(sys.argv[2])
    elolap   = sys.argv[3]
    hatlap   = sys.argv[4]
    cellap   = sys.argv[5]
    ini_fajl = sys.argv[6]

    # Előfeltétel vizsgálat
    if cellap != elolap and cellap != hatlap:
        print("None")
        return

    # Tábla inicializálása
    tabla_ini(sor, oszlop, cellap, ini_fajl)

if __name__ == "__main__":
    main()
