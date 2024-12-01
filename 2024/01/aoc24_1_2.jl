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
