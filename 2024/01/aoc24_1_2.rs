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
