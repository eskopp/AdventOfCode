package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func main() {
	// Datei öffnen
	file, err := os.Open("e:/git/AdventOfCode/2023/01/input.txt")
	if err != nil {
		fmt.Println("Fehler beim Öffnen der Datei:", err)
		return
	}
	defer file.Close()

	var totalSum int
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		var firstDigit, lastDigit rune

		// Find the first and last digits in the line
		for _, char := range line {
			if unicode.IsDigit(char) {
				firstDigit = char
				break
			}
		}

		for i := len(line) - 1; i >= 0; i-- {
			if unicode.IsDigit(rune(line[i])) {
				lastDigit = rune(line[i])
				break
			}
		}

		// Combine the digits to form a two-digit number and add to the total
		if firstDigit != 0 && lastDigit != 0 {
			calibrationValue := int(firstDigit-'0')*10 + int(lastDigit-'0')
			totalSum += calibrationValue
		}
	}

	// Fehler beim Scannen überprüfen
	if err := scanner.Err(); err != nil {
		fmt.Println("Fehler beim Lesen der Datei:", err)
		return
	}

	// Ausgabe der Summe der Kalibrierungswerte
	fmt.Println("Gesamtsumme der Kalibrierungswerte:", totalSum)
}
