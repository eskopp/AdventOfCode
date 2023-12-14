from colorama import Fore, init
import os

# Header
init(autoreset=True)
print(f"{Fore.GREEN}Advent of Code 2023, Day 1, Task 1")
print(f"Task: \t {Fore.BLUE} https://adventofcode.com/2023/day/1")
print(f"Folder:  {Fore.BLUE} {os.path.abspath('.')}")
print(f"Input: \t {Fore.BLUE} input.txt")


def calculate_calibration_sum(calibration_document):
    total_sum = 0
    for line in calibration_document:
        numbers = [int(char) for char in line if char.isdigit()]
        if not numbers:
            continue
        calibration_value = (numbers[0] * 10) + numbers[-1]
        total_sum += calibration_value

    return total_sum


with open("./input.txt", "r") as file:
    calibration_document = [line.strip() for line in file]

result = calculate_calibration_sum(calibration_document)

print(f"Value:\t  {Fore.BLUE}{result}")
