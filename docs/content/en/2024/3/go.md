---
title: Day 2 - Go 
toc: true
type: docs
weight: 2
---

## Download 
{{< cards >}}
{{< card title="Example" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/03/example.in" icon="user" tag="Github">}}
{{< card title="Input" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/03/input.in" icon="user" tag="Github">}}
{{< card title="Source Code Part 1" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/03/aoc24_3_1.go" icon="user" tag="Github">}}
{{< card title="Source Code Part 2" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/03/aoc24_3_2.go" icon="user" tag="Github">}}
{{< /cards >}}


## Part 1

```go {linenos=table,linenostart=1}
// AoC 2024 - Day 2 - Task 1
// https://erik-skopp.de/AdventofCode/2024/2/
// https://github.com/eskopp/AdventOfCode/blob/main/2024/03/aoc24_2_1.go
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

```


## Part 2 

```go {linenos=table,linenostart=1}
// AoC 2024 - Day 2 - Task 2
// https://erik-skopp.de/AdventofCode/2024/2/
// https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_2_2.go
//
// Day 2 - Red-Nosed Reports
// result: 366

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Function to check if a list of levels is safe
func isSafe(levels []int) bool {
	ascending := true
	descending := true

	// Check if the list is sorted either ascending or descending
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

	return ascending || descending
}

// Function to check if a list can be made safe by removing one level
func canBeMadeSafe(levels []int) bool {
	for i := range levels {
		// Create a new list with one level removed
		modifiedLevels := append([]int{}, levels[:i]...)
		modifiedLevels = append(modifiedLevels, levels[i+1:]...)

		if isSafe(modifiedLevels) {
			return true
		}
	}
	return false
}

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

	// Count the number of safe reports
	safeCount := 0
	for _, report := range data {
		if isSafe(report) || canBeMadeSafe(report) {
			safeCount++
		}
	}

	// Print the result
	fmt.Printf("Number of safe reports with Problem Dampener: %d\n", safeCount)
}
```