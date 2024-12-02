---
title: Day 2 - Python
toc: true
type: docs
weight: 1
---

## Download

{{< cards >}}
{{< card title="Example" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/02/example.in" icon="user" tag="Github">}}
{{< card title="Input" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/02/input.in" icon="user" tag="Github">}}
{{< card title="Source Code Part 1" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/02/aoc24_2_1.py" icon="user" tag="Github">}}
{{< card title="Source Code Part 2" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/02/aoc24_2_2.py" icon="user" tag="Github">}}
{{< /cards >}}

## Part 1

```python {linenos=table,linenostart=1}
# AoC 2024 - Day 2 - Task 1
# https://erik-skopp.de/AdventofCode/2024/2/
# https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_2_1.py
#
# Day 2 - Red-Nosed Reports
# result: 306


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
```

## Part 2

```python {linenos=table,linenostart=1}
# AoC 2024 - Day 2 - Task 2
# https://erik-skopp.de/AdventofCode/2024/2/
# https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_2_2.py
#
# Day 2 - Red-Nosed Reports
# result: 366


from os import chdir
from os.path import join

# Change the working directory
chdir(join("2024", "02"))

# Load the file and convert the data into integers
data = []
with open("input.in", "r") as file:
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

# Function to check if a report can be made safe by removing one level
def can_be_made_safe(levels):
    # Try removing each level and check if the remaining list is safe
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]  # Remove the i-th element
        if is_safe(modified_levels):
            return True
    return False

# Count the safe reports considering the Problem Dampener
safe_count = 0
for report in data:
    if is_safe(report) or can_be_made_safe(report):
        safe_count += 1

# Print the result
print(f"Number of safe reports with Problem Dampener: {safe_count}")

```
