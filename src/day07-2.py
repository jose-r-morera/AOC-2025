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
#INPUT_FILE = DATA_DIR / "day07-example.txt"

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

    for idx, elem in enumerate(matrix[0]):
        if elem == "S":
            current_beam_row = {idx:1} # use a position: count dictionaire of beams for each row
    count = 1 # Initial Beam at S
    # On each split, the "timelines" are added to the dict as a count of beam in that new position
    # Eg if two splits might produce a beam in column 3 -> 3:2
    # A split adds 1 to the position to its left and its right; whereas no split conservates previous beams
    for row in matrix[1:]:
        next_beam_row = {}
        for idx in current_beam_row.keys():
            if row[idx] == "^":
                count += current_beam_row[idx]
                next_beam_row[idx + 1] = next_beam_row.get(idx + 1, 0) + current_beam_row[idx]
                next_beam_row[idx - 1] = next_beam_row.get(idx - 1, 0) + current_beam_row[idx]
            else:
                next_beam_row[idx] = next_beam_row.get(idx, 0) + current_beam_row[idx]

        current_beam_row = next_beam_row
    print(f"Result: {count}")



        

    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)