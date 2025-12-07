#!/usr/bin/env python3
"""
Project: AOC 2025 - Day 07: 
Description: https://adventofcode.com/2025/day/7
Author: José Ramón Morera Campos
Date: 07/12/2025
"""

import sys
from pathlib import Path

#---------------------------------------------------------
# Constants
#---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_FILE = DATA_DIR / "day07-input.txt"
# INPUT_FILE = DATA_DIR / "day07-example.txt"

# ---------------------------------------------------------
# Auxiliar Functions
# ---------------------------------------------------------

# ---------------------------------------------------------
# Core Logic
# ---------------------------------------------------------
def main(args: list[str]) -> int:
    """Main entry point for the script."""

    with open(INPUT_FILE, "r") as file:
        matrix = [line.strip() for line in file]

    count = 0   
    for idx, elem in enumerate(matrix[0]):
        print (elem, idx)
        if elem == "S":
            current_beam = [idx]
    for row in matrix[1:]:
        next_beam = set()
        for idx in current_beam:
            if row[idx] == "^":
                count += 1
                next_beam.add(idx + 1)
                next_beam.add(idx -1)
            else:
                next_beam.add(idx)
        current_beam = next_beam
    print(f"Result: {count}")

    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)