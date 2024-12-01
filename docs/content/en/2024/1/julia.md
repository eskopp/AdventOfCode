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

```go {linenos=table,linenostart=1}
// AoC 2024 - Day 1 - Task 1
// https://erik-skopp.de/AdventofCode/2024/1/
// https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_1.go
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
```


## Part 2 

```go {linenos=table,linenostart=1}
// AoC 2024 - Day 1 - Task 2
// https://erik-skopp.de/AdventofCode/2024/1/
// https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_2.go
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

```