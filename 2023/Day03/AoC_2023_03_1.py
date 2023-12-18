from colorama import Fore, init
import os

# Header
init(autoreset=True)
print(f"{Fore.GREEN}Advent of Code 2023, Day 3, Task 1")
print(f"Task: \t {Fore.BLUE}https://adventofcode.com/2023/day/3")
print(f"Folder:  {Fore.BLUE} {os.path.abspath('.')}")
print(f"Input: \t {Fore.BLUE}input.txt")


# Lösung
def is_symbol(char):
    return char in {"*", "+", "#"}


def is_valid_position(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


def calculate_part_numbers(engine):
    rows, cols = len(engine), len(engine[0])
    part_numbers = []

    for row in range(rows):
        for col in range(cols):
            char = engine[row][col]

            if char.isdigit():
                adjacent_symbols = [
                    engine[i][j]
                    for i in range(row - 1, row + 2)
                    for j in range(col - 1, col + 2)
                    if is_valid_position(i, j, rows, cols)
                    and not engine[i][j].isdigit()
                ]

                if any(is_symbol(symbol) for symbol in adjacent_symbols):
                    part_numbers.append(int(char))

    return sum(part_numbers)


# Daten aus der "input.txt"-Datei lesen
with open("input.txt", "r") as file:
    engine_data = [line.strip() for line in file]

# Ergebnis berechnen und ausgeben
result = calculate_part_numbers(engine_data)
print(f"Result: {Fore.YELLOW} {result}")
