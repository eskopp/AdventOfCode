// AoC 2024 - Day 2 - Task 1
// https://erik-skopp.de/AdventofCode/2024/2/
// https://github.com/eskopp/AdventOfCode/blob/main/2024/02/aoc24_2_1.go
//
// Day 2 - Red-Nosed Reports
// result: 306

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// Open the input file
	file, err := os.Open("example.in")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var data [][]int

	// Read the file line by line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		// Split the line into strings and convert to integers
		levels := strings.Fields(line)
		intLevels := make([]int, len(levels))
		for i, str := range levels {
			intLevels[i], _ = strconv.Atoi(str)
		}
		data = append(data, intLevels)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Function to check if a report is safe
	isSafe := func(levels []int) bool {
		ascending := true
		descending := true

		// Check if the list is sorted
		for i := 0; i < len(levels)-1; i++ {
			diff := levels[i+1] - levels[i]
			if diff > 3 || diff < -3 {
				return false
			}
			if diff < 0 {
				ascending = false
			}
			if diff > 0 {
				descending = false
			}
		}
		// A report is safe if it's either strictly ascending or strictly descending
		return ascending || descending
	}

	// Count the number of safe reports
	safeCount := 0
	for _, report := range data {
		if isSafe(report) {
			safeCount++
		}
	}

	// Print the result
	fmt.Printf("Number of safe reports: %d\n", safeCount)
}
