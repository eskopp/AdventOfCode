// AoC 2024 - Day 1 - Task 1
// https://erik-skopp.de/AdventofCode/2024/1/
// https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_1.rs
//
// Day 1 - Historian Hysteria
// result: 1722302

package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
)

func main() {
	// Change the working directory to the specified path
	err := os.Chdir(filepath.Join("2024", "01"))
	if err != nil {
		fmt.Printf("Error changing directory: %v\n", err)
		return
	}

	// Unsorted slices for left and right column values
	var leftColumn []int
	var rightColumn []int

	// Open the input file
	file, err := os.Open("input.in")
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return
	}
	defer file.Close()

	// Read the file and split data into columns
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		columns := strings.Split(line, "   ")
		if len(columns) == 2 {
			leftValue, err := strconv.Atoi(columns[0])
			if err != nil {
				fmt.Printf("Error parsing left value: %v\n", err)
				return
			}
			rightValue, err := strconv.Atoi(columns[1])
			if err != nil {
				fmt.Printf("Error parsing right value: %v\n", err)
				return
			}
			leftColumn = append(leftColumn, leftValue)
			rightColumn = append(rightColumn, rightValue)
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}

	// Sort the left and right columns
	sort.Ints(leftColumn)
	sort.Ints(rightColumn)

	// Calculate absolute differences between paired values
	var totalDifference int
	for i := 0; i < len(leftColumn); i++ {
		difference := leftColumn[i] - rightColumn[i]
		if difference < 0 {
			difference = -difference
		}
		totalDifference += difference
	}

	// Output the result
	fmt.Println(totalDifference)
}
