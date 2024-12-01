use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    // Pfad zur Eingabedatei
    let file_path = Path::new("2024/01/input.in");

    // Datei öffnen
    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);

    // Unsortierte Listen für linke und rechte Spalten
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();

    // Daten einlesen und in Spalten aufteilen
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

    // Betragsdifferenzen berechnen und aufsummieren
    let result: i32 = left
        .iter()
        .zip(right.iter())
        .map(|(l, r)| (l - r).abs())
        .sum();

    // Ergebnis ausgeben
    println!("Ergebnis: {}", result);

    Ok(())
}
