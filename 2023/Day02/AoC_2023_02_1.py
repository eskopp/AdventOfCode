import pandas as pd
import re
from colorama import Fore, init
import os


def print_header():
    init(autoreset=True)
    print(f"{Fore.GREEN}Advent of Code 2023, Day 2, Task 1")
    print(f"Task: \t {Fore.BLUE} https://adventofcode.com/2023/day/2")
    print(f"Folder:  {Fore.BLUE} {os.path.abspath('.')}")
    print(f"Input: \t {Fore.BLUE} input.txt")


def read_game_records(file_path):
    game_records = []

    with open(file_path, "r") as file:
        for line in file:
            game_info, results = line.strip().split(":")
            game_number = int(game_info.split(" ")[-1])
            results_sets = results.split(";")

            for result_set in results_sets:
                green_match = re.search(r"(\d+)\s+green", result_set)
                red_match = re.search(r"(\d+)\s+red", result_set)
                blue_match = re.search(r"(\d+)\s+blue", result_set)

                game_data = {
                    "game_number": game_number,
                    "green": 0,
                    "red": 0,
                    "blue": 0,
                }

                if green_match:
                    game_data["green"] = int(green_match.group(1))
                if red_match:
                    game_data["red"] = int(red_match.group(1))
                if blue_match:
                    game_data["blue"] = int(blue_match.group(1))

                game_records.append(game_data)

    return pd.DataFrame(game_records)


def calculate_possible_games_sum(df):
    df["passed_test"] = (df["red"] <= 12) & (df["green"] <= 13) & (df["blue"] <= 14)
    df_percent = df.groupby("game_number")["passed_test"].mean().reset_index()

    return df_percent.query("passed_test == 1")["game_number"].sum()


if __name__ == "__main__":
    print_header()
    file_path = "input.txt"
    game_df = read_game_records(file_path)
    total_solution = calculate_possible_games_sum(game_df)
    print(f"Value:\t {Fore.BLUE} {total_solution}")
