#!/usr/bin/env python3
"""
Project: AOC 2025 - Day 04: 
Description: https://adventofcode.com/2025/day/04
Author: José Ramón Morera Campos
Date: 04/12/2025
"""

import os
import sys
from pathlib import Path

#---------------------------------------------------------
# Constants
#---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_FILE = DATA_DIR / "day04-1-input.txt"
#INPUT_FILE = DATA_DIR / "day04-1-example.txt"

PAPER_CHAR = "@"
REMOVED_CHAR = "X"
IGNORE_CHAR = "."

ADJACENTOFFSETS = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),          (0, 1),
                    (1, -1),  (1, 0), (1, 1)]
ADJACENTOFFSETSL = [        (-1, 0), (-1, 1),
                                        (0, 1),
                                (1, 0), (1, 1)]
ADJACENTOFFSETSR = [(-1, -1), (-1, 0),      
                    (0, -1),          
                    (1, -1),  (1, 0)         ]

# ---------------------------------------------------------
# Auxiliar Functions
# ---------------------------------------------------------

# ---------------------------------------------------------
# Core Logic
# ---------------------------------------------------------
def main(args: list[str]) -> int:
    """Main entry point for the script."""

    with open(INPUT_FILE, "r") as file:
        matrix = [list(line.strip()) for line in file]

    pad = 0
    matrix.insert(0, [pad] * len(matrix[0]))
    matrix.append([pad] * len(matrix[0]))
    total = 0
    current_iteration = -1
    while current_iteration != 0:
        current_iteration = 0
        for row_idx in range(1, len(matrix) - 1):
            for pos, char in enumerate(matrix[row_idx]):
                if char != PAPER_CHAR:
                    continue
                sum = 0
                if pos == 0:
                    adjacency = ADJACENTOFFSETSL
                elif pos == len(matrix[0]) - 1:
                    adjacency = ADJACENTOFFSETSR
                else:
                    adjacency = ADJACENTOFFSETS
                for adj in adjacency:
                    adj_row = row_idx + adj[0]
                    adj_col = pos + adj[1]
                    sum += matrix[adj_row][adj_col] == PAPER_CHAR
                if sum < 4:
                    matrix[row_idx][pos] = REMOVED_CHAR
                    current_iteration += 1
        total += current_iteration
        # Remove all paper_CHAR
        for row_idx in range(1, len(matrix) - 1):
            for pos, char in enumerate(matrix[row_idx]):
                if char == REMOVED_CHAR:
                    matrix[row_idx][pos] = IGNORE_CHAR

    print(f"Total positions to put paper_CHAR: {total}")

    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)