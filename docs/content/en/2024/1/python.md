---
title: Day 1 - Python
toc: false
type: docs
---


## Download
{{< cards >}}
{{< card title="Example" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/example.in" icon="user" tag="Github">}}
{{< card title="Input" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/input.in" icon="user" tag="Github">}}
{{< /cards >}}




## Part 1
```python {linenos=table,linenostart=1}
# https://erik-skopp.de/AdventofCode/2024/1/
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
```
See: [https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_1.py](https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_1.py)