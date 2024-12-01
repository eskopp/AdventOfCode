---
title: Day 1 - Julia 
toc: false
type: docs
weight: 4
---

{{< callout type="info" >}}
I don't have much experience with Julia, but I'm curious to explore the language. I'm using the LTS version v1.10.7. Julia is a high-performance language designed specifically for scientific computing. However, it is only used in 0.54% of all projects. While Julia serves an important niche, its focus limits its appeal to a relatively small audience. 

These facts make Julia a genuinely intriguing language. I don't plan to use it for the entirety of Advent of Code, but I enjoy exploring different languages from time to time, and Julia is definitely worth a closer look.
{{< /callout >}}

## Download 
{{< cards >}}
{{< card title="Example" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/example.in" icon="user" tag="Github">}}
{{< card title="Input" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/input.in" icon="user" tag="Github">}}
{{< card title="Source Code Part 1" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_1.jl" icon="user" tag="Github">}}
{{< card title="Source Code Part 2" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_2.jl" icon="user" tag="Github">}}
{{< /cards >}}


## Part 1

```julia {linenos=table,linenostart=1}
# AoC 2024 - Day 1 - Task 1
# https://erik-skopp.de/AdventofCode/2024/1/
# https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_1.jl
#
# Day 1 - Historian Hysteria
# result: 1722302

# Change the working directory to the specified path
cd("2024/01")

# Unsorted arrays for left and right column values
left_column = []
right_column = []

# Read the file and split data into columns
open("input.in", "r") do file
    for line in eachline(file)
        columns = split(strip(line), "   ") # Split columns based on triple spaces
        push!(left_column, columns[1])
        push!(right_column, columns[2])
    end
end

# Sort the left and right columns
sorted_left = sort(parse.(Int, left_column))
sorted_right = sort(parse.(Int, right_column))

# Calculate absolute differences between paired values
differences = [abs(sorted_left[i] - sorted_right[i]) for i in 1:length(sorted_left)]

# Compute the total sum of the differences
total_difference = sum(differences)

# Output the result
println(total_difference)

```


## Part 2 

```julia {linenos=table,linenostart=1}
# AoC 2024 - Day 1 - Task 2
# https://erik-skopp.de/AdventofCode/2024/1/
# https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_2.jl
#
# Day 1 - Historian Hysteria
# result: 20373490

# Change the working directory to the specified path
cd("2024/01")

# Arrays for unique and target values
unique_values = String[]
target_values = String[]

# Read the file and split data into columns
open("input.in", "r") do file
    for line in eachline(file)
        columns = split(strip(line), "   ") # Split columns based on triple spaces
        if length(columns) == 2
            push!(unique_values, columns[1])
            push!(target_values, columns[2])
        end
    end
end

# Count how often values from `unique_values` appear in `target_values`
frequency_map = Dict(value => count(==(value), target_values) for value in unique_values)

# Create a list of weighted counts
weighted_counts = Int[]
for (value, count) in frequency_map
    if count != 0
        push!(weighted_counts, parse(Int, value) * count)
    end
end

# Calculate the total sum of weighted counts
total_sum = sum(weighted_counts)

# Output the result
println(total_sum)


```