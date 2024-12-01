use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::env;

fn main() -> io::Result<()> {
    match env::current_dir() {
        Ok(path) => println!("Aktueller Pfad: {}", path.display()),
        Err(e) => eprintln!("Fehler beim Abrufen des Pfads: {}", e),
    }
    
    let path = Path::new("input.in");

    
    let file = File::open(&path)?;
    let reader = io::BufReader::new(file);

    let mut result = 0;
    
    for line in reader.lines() {
        let line = line?;
        let values: Vec<i32> = line
            .split("   ") 
            .filter_map(|s| s.trim().parse::<i32>().ok()) // i32
            .collect();
        if let [left, right] = values[..] {
            result += (left - right).abs(); 
        }
    }

    println!("{}", result);

    Ok(())
}
