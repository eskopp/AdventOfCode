---
title: Day 1 - Python
toc: false
type: docs
---

{{< callout type="info" >}}
The whole thing could have been done more elegantly via maps. However, efficiency and speed are not important here. So this is not so important. What matters to me here is the legibility and simplicity of the code.
{{< /callout >}}

## Download

{{< cards >}}
{{< card title="Example" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/example.in" icon="user" tag="Github">}}
{{< card title="Input" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/input.in" icon="user" tag="Github">}}
{{< card title="Source Code Part 1" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_1.py" icon="user" tag="Github">}}
{{< card title="Source Code Part 2" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_2.py" icon="user" tag="Github">}}
{{< /cards >}}

## Part 1

```python {linenos=table,linenostart=1}
# AoC 2024 - Day 1 - Task 1
# https://erik-skopp.de/AdventofCode/2024/1/
# https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_1.py
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


# Sortieren der Listena
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
```

## Part 2

```python {linenos=table,linenostart=1}
# AoC 2024 - Day 1 - Task 2
# https://erik-skopp.de/AdventofCode/2024/1/
# https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_2.py
#
# Day 1 - Historian Hysteria
# result: 20373490

import os

# Set the working directory
os.chdir(os.path.join("2024", "01"))

# Lists for left and right values
left = []
right = []

# Read the file and split data into columns
with open("input.in", "r") as file:
    for line in file:
        line = line.strip().split("   ")
        if len(line) == 2:
            left.append(line[0])
            right.append(line[1])

# Count how often values from `left` appear in `right`
# Using a dict here is not ideal for further processing, so it is converted to a List[Tuple]
list_tuples = {value: right.count(value) for value in left}.items()

# Create a list in `index` that aggregates the counts
# Example: dict_items([('16435', 0), ...]) is processed
index = []
for dummy in list_tuples:
    # Skip empty elements to avoid creating a long list of zeros
    if dummy[1] != 0:
        index.append(int(dummy[0]) * dummy[1])
del list_tuples

# Sum up the individual values
result = 0
for dummy in index:
    result += dummy

# Output the result
print(result)

```
