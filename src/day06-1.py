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

# ---------------------------------------------------------
# Core Logic
# ---------------------------------------------------------
def main(args: list[str]) -> int:
    """Main entry point for the script."""

    with open(INPUT_FILE, "r") as file:
        matrix = [list(line.strip().split()) for line in file]

    total = 0
    print("Matrix loaded:")
    for col in range(len(matrix[0])):
        operator =  matrix[-1][col]
        column_result = int(matrix[0][col])
        for row in range(1, len(matrix) - 1):
            value = int(matrix[row][col])
            if operator == "+":
                column_result += value
            elif operator == "*":
                column_result *= value
        total += column_result

    print(f"Result: {total}")

    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)