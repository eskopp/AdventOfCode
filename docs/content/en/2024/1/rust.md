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

```

## Part 2

```rust {linenos=table,linenostart=1}

```
