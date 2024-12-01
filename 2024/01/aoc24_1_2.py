# AoC 2024 - Day 1 - Task 2
# https://erik-skopp.de/AdventofCode/2024/1/
# https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_2.py
#
# Day 1 - Historian Hysteria
# result: 20373490

import os

# Set the working directory
os.chdir(os.path.join("2024", "01"))

# Lists for unique and target values
unique_values = []
target_values = []

# Read the file and split data into columns
with open("input.in", "r") as file:
    for line in file:
        line = line.strip().split("   ")
        if len(line) == 2:
            unique_values.append(line[0])
            target_values.append(line[1])

# Count how often values from `unique_values` appear in `target_values`
# The dictionary is converted to a List[Tuple] for further processing
frequency_tuples = {
    value: target_values.count(value) for value in unique_values
}.items()

# Create a list of weighted counts
weighted_counts = []
for value, count in frequency_tuples:
    # Skip entries with a count of zero
    if count != 0:
        weighted_counts.append(int(value) * count)
del frequency_tuples

# Calculate the total sum of weighted counts
total_sum = sum(weighted_counts)

# Output the result
print(total_sum)
