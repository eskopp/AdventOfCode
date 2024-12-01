# AoC 2024 - Day 1 - Part 1
# https://erik-skopp.de/AdventofCode/2024/1/
#
# Day 1 - Historian Hysteria
import os

# Die Pfade können je nach Ort abweichen
os.chdir(os.path.join("2024", "01"))

# unsortiere Listen
left = []
right = []
liste = []

# Trennen der Daten in die verschiedenen Spalten
with open("input.in", "r") as file:
    for line in file:
        line = line.strip().split("   ")
        left.append(line[0])
        right.append(line[1])


# Sortieren der Listen
left_sort = sorted(left)
right_sort = sorted(right)

# Löschen von Altlasten
del left
del right

# Berechnen der Paarungen
index = []
for runner in range(len(left_sort)):
    value = int(left_sort[runner]) - int(right_sort[runner])
    # Betragsfunktion
    if value < 0:
        value *= -1
    index.append(value)
    del value

# Ermittle das Ergebniss
result = 0
for runner in index:
    result += runner

# Test Ausgabe
print(result)
