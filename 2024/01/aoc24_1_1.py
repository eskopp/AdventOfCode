# https://erik-skopp.de/AdventofCode/2024/1/
# https://github.com/eskopp/AdventOfCode
#
# Day 1 - Part 1 - Historian Hysteria
# result: 1722302

import os

# Arbeitsverzeichnis setzen
os.chdir(os.path.join("2024", "01"))

# Initialisierung der Variablen
result = 0

# Daten direkt verarbeiten
with open("input.in", "r") as file:
    for line in file:
        left, right = map(int, line.strip().split("   "))
        result += abs(left - right)

# Ausgabe des Ergebnisses
print(result)
del result
