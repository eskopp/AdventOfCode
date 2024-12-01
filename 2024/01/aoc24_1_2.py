# AoC 2024 - Day 1 - Task 2
# https://erik-skopp.de/AdventofCode/2024/1/
# https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_2.py
#
# Day 1 - Historian Hysteria
# result:

import os

# Arbeitsverzeichnis setzen
os.chdir(os.path.join("2024", "01"))

# Listen für linke und rechte Werte
left = []
right = []

# Datei einlesen und Daten in Spalten aufteilen
with open("input.in", "r") as file:
    for line in file:
        line = line.strip().split("   ")
        if len(line) == 2:
            left.append(line[0])
            right.append(line[1])

# Zählen, wie oft Werte aus `left` in `right` vorkommen
result = {value: right.count(value) for value in left}

# Ausgabe des Ergebnisses
print(result)
