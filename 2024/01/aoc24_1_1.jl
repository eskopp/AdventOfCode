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
