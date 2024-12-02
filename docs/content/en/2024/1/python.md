---
title: Day 1 - Python
toc: true
type: docs
weight: 1
---

{{< callout type="info" >}}
The entire implementation could have been done more elegantly using maps. However, efficiency and speed are not the focus here, so it’s not a priority. What truly matters to me is the readability and simplicity of the code.
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
frequency_tuples = {value: target_values.count(value) for value in unique_values}.items()

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

```
