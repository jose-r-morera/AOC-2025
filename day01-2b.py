#!/usr/bin/env python3
"""
Project: AOC 2025 - Day 1: Secret Entrance; PART 2
Description: https://adventofcode.com/2025/day/1 ; MORE ELEGANT SOLUTION
Author: José Ramón Morera Campos
Date: 01/12/2025
"""

import os
import sys

#---------------------------------------------------------
# Constants
#---------------------------------------------------------
INPUT_FILE = "day01-1-input.txt"
INPUT_FILE = "day01-1-example.txt"


# ---------------------------------------------------------
# Auxiliar Functions
# ---------------------------------------------------------

# ---------------------------------------------------------
# Core Logic
# ---------------------------------------------------------
def main(args: list[str]) -> int:
    """Main entry point for the script."""

    position = 50
    zero_count = 0
    with open(INPUT_FILE, "r") as file:
        for line in file:
            s = line.strip()
            direction = s[0]
            movement = int(s[1:])

            zero_count += movement // 100
            movement %= 100


            print("Current position: ", position, " zero_count: ", zero_count)
            
    print("zero_count: ", zero_count)
    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)