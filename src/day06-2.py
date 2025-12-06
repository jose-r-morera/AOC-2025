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
    return int("".join(matrix[row][col] for row in range(0, len(matrix) -1) if str.isdigit(matrix[row][col])))
# ---------------------------------------------------------
# Core Logic
# ---------------------------------------------------------
def main(args: list[str]) -> int:
    """Main entry point for the script."""

    with open(INPUT_FILE, "r") as file:
        matrix = [list(line) for line in file]

    # Make all operators have the same format / right limit = " " + "char"
    matrix[-1].append(" ")
    matrix[-1].append("\n")

    total_result = 0 # sum of all results
    segment_start = 0
    for segment_end in range(1, len(matrix[-1])):
        if matrix[-1][segment_end] == " ":
            continue
        else: 
            operator = matrix[-1][segment_start]
            current_op_result = read_vertical_number(matrix, segment_start)
            for col in range(segment_start + 1, segment_end - 1):
                number = read_vertical_number(matrix, col)
                if operator == "+": current_op_result += number
                elif operator == "*": current_op_result *= number
            total_result += current_op_result

            segment_start = segment_end

    print(f"Result: {total_result}")

    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)