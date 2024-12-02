# AoC 2024 - Day 2 - Task 2
# https://erik-skopp.de/AdventofCode/2024/2/
# https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_2_2.py
#
# Day 2 - Red-Nosed Reports
# result: 


from os import chdir
from os.path import join

# Change the working directory
chdir(join("2024", "02"))

# Load the file and convert the data into integers
data = []
with open("example.in", "r") as file:
    for line in file:
        # Remove line breaks and convert the line into a list of integers
        data.append(list(map(int, line.strip().split(" "))))

print(data)