// AoC 2024 - Day 1 - Task 1
// https://erik-skopp.de/AdventofCode/2024/1/
// https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_1_1.rs
//
// Day 1 - Historian Hysteria
// result: 1722302

use std::fs::File;
use std::io::{self, BufRead};

fn calculate_result(file_path: &str) -> io::Result<i32> {
    // Datei öffnen
    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);

    // Unsortierte Listen 
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();

    // split
    for line in reader.lines() {
        let line = line?;
        let columns: Vec<&str> = line.trim().split("   ").collect();
        if let [left_value, right_value] = columns[..] {
            left.push(left_value.parse::<i32>().unwrap());
            right.push(right_value.parse::<i32>().unwrap());
        }
    }

    // Listen sortieren
    left.sort();
    right.sort();

    // Betragsdifferenzen 
    let result: i32 = left
        .iter()
        .zip(right.iter())
        .map(|(l, r)| (l - r).abs())
        .sum();

    Ok(result)
}

fn main() -> io::Result<()> {
    // Pfad zur Eingabedatei
    let file_path = "input.in";

    // Funktion aufrufen und Ergebnis ausgeben
    match calculate_result(file_path) {
        Ok(result) => println!("Ergebnis: {}", result),
        Err(e) => eprintln!("Fehler: {}", e),
    }

    Ok(())
}
