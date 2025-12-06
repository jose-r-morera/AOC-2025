#!/usr/bin/env python3
"""
Project: AOC 2025 - Day 06: 
Description: https://adventofcode.com/2025/day/6
Author: José Ramón Morera Campos
Date: 06/12/2025
"""

import sys
from pathlib import Path

#---------------------------------------------------------
# Constants
#---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_FILE = DATA_DIR / "day06-input.txt"
# INPUT_FILE = DATA_DIR / "day06-example.txt"

# ---------------------------------------------------------
# Auxiliar Functions
# ---------------------------------------------------------
def read_vertical_number(matrix: list[list[str]], col: int) -> str:
    """Reads a vertical number from the matrix at the given column."""
    return "".join([matrix[row][col] for row in range(1, len(matrix) -1) if str.isdigit(matrix[row][col])])
# ---------------------------------------------------------
# Core Logic
# ---------------------------------------------------------
def main(args: list[str]) -> int:
    """Main entry point for the script."""

    with open(INPUT_FILE, "r") as file:
        matrix = [list(line) for line in file]

    # Make all operators have the same format / right limit
    matrix[-1].append(" ")
    matrix[-1].append("\n")

    result = 0
    segmet_start = 0
    for segment_end in range(1, len(matrix[-1])):
        if matrix[-1][segment_end] == " ":
            continue
        else: 
            current_len = segment_end - segmet_start -1
            operator = matrix[-1][segmet_start]
            operation_total = 1 if operator == "*" else 0
            for col in range(segmet_start, segmet_start+current_len):
                number = matrix[0][col] if matrix[0][col] != " " else ""
                number = number + read_vertical_number(matrix, col)
                if operator == "+": operation_total += int(number)
                elif operator == "*": operation_total *= int(number)
            result += operation_total

            segmet_start = segment_end

    print(f"Result: {result}")

    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)