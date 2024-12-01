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
