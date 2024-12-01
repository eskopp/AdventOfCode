---
title: Day 1 - Rust
toc: false
type: docs
---
{{< callout type="info" >}}
I have never worked in Rust. My main programming language is Python. I am trying to learn a modern compiler language and C++ as part of the Advent of Codes 2024. Rust is quite handy. Unfortunately, most legacy programs are still written in C++. So unfortunately you have to work with it to find work. 
{{< /callout >}}

## Download

{{< cards >}}
{{< card title="Example" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/example.in" icon="user" tag="Github">}}
{{< card title="Input" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/input.in" icon="user" tag="Github">}}
{{< card title="Source Code Part 1" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_1.rs" icon="user" tag="Github">}}
{{< card title="Source Code Part 2" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_2.rs" icon="user" tag="Github">}}
{{< /cards >}}

## Part 1

```rust {linenos=table,linenostart=1}
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

```

## Part 2

```rust {linenos=table,linenostart=1}
// AoC 2024 - Day 1 - Task 2
// https://erik-skopp.de/AdventofCode/2024/1/
// https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_2.rs
//
// Day 1 - Historian Hysteria
// result: 20373490

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    // Set the working directory
    let file_path = Path::new("input.in"); 

    // Vectors for unique and target values
    let mut unique_values: Vec<String> = Vec::new();
    let mut target_values: Vec<String> = Vec::new();

    // Open the file
    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);

    // Read the file and split data into columns
    for line in reader.lines() {
        let line = line?;
        let columns: Vec<&str> = line.trim().split("   ").collect();
        if columns.len() == 2 {
            unique_values.push(columns[0].to_string());
            target_values.push(columns[1].to_string());
        }
    }

    // Count how often values from `unique_values` appear in `target_values`
    let mut weighted_counts: Vec<i32> = Vec::new();
    for value in &unique_values {
        let count = target_values.iter().filter(|&x| x == value).count() as i32;
        if count != 0 {
            weighted_counts.push(value.parse::<i32>().unwrap_or(0) * count);
        }
    }

    // Calculate the total sum of weighted counts
    let total_sum: i32 = weighted_counts.iter().sum();

    // Output the result
    println!("Total Sum: {}", total_sum);

    Ok(())
}

```
