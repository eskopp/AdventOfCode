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

# Function to check if a list is safe
def is_safe(levels):
    # Check if the list is sorted either ascending or descending
    if levels == sorted(levels) or levels == sorted(levels, reverse=True):
        # Check the differences between adjacent numbers
        differences = [abs(levels[i] - levels[i+1]) for i in range(len(levels)-1)]
        return all(1 <= diff <= 3 for diff in differences)
    return False

# Count the safe reports
safe_count = sum(1 for report in data if is_safe(report))

# Print the result
print(f"Number of safe reports: {safe_count}")
