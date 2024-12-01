# AoC 2024 - Day 1 - Task 1
# https://erik-skopp.de/AdventofCode/2024/1/
# https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_1.py
#
# Day 1 - Historian Hysteria
# result: 1722302


import os

# Change the working directory to the specified path
os.chdir(os.path.join("2024", "01"))

# Unsorted lists for left and right column values
left_column = []
right_column = []

# Read the file and split data into columns
with open("input.in", "r") as file:
    for line in file:
        line = line.strip().split("   ")  # Split columns based on triple spaces
        left_column.append(line[0])
        right_column.append(line[1])

# Sort the left and right columns
sorted_left = sorted(left_column)
sorted_right = sorted(right_column)

# Free up memory by deleting the original unsorted lists
del left_column
del right_column

# Calculate absolute differences between paired values
differences = []
for i in range(len(sorted_left)):
    difference = int(sorted_left[i]) - int(sorted_right[i])
    # Convert the difference to its absolute value
    if difference < 0:
        difference = -difference
    differences.append(difference)

# Compute the total sum of the differences
total_difference = sum(differences)

# Output the result
print(total_difference)
