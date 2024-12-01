// AoC 2024 - Day 1 - Task 2
// https://erik-skopp.de/AdventofCode/2024/1/
// https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_2.py
//
// Day 1 - Historian Hysteria
// result: 20373490

package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

func main() {

	// Change the working directory
	err := os.Chdir(filepath.Join("2024", "01"))
	if err != nil {
		fmt.Printf("Error changing directory: %v\n", err)
		return
	}

	// Lists for unique and target values
	var uniqueValues []string
	var targetValues []string

	// Read the file and split data into columns
	file, err := os.Open("input.in")
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		columns := strings.Split(line, "   ")
		if len(columns) == 2 {
			uniqueValues = append(uniqueValues, columns[0])
			targetValues = append(targetValues, columns[1])
		}
	}
	if err := scanner.Err(); err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}

	// Count how often values from `uniqueValues` appear in `targetValues`
	counts := make(map[string]int)
	for _, value := range uniqueValues {
		counts[value] = 0
		for _, target := range targetValues {
			if target == value {
				counts[value]++
			}
		}
	}

	// Calculate the weighted sum
	totalSum := 0
	for value, count := range counts {
		if count != 0 {
			parsedValue, err := strconv.Atoi(value)
			if err != nil {
				fmt.Printf("Error parsing value '%s': %v\n", value, err)
				return
			}
			totalSum += parsedValue * count
		}
	}

	// Output the result
	fmt.Println(totalSum)
}
