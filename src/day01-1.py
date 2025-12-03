#!/usr/bin/env python3
"""
Project: AOC 2025 - Day 1: Secret Entrance; PART 1
Description: https://adventofcode.com/2025/day/1
Author: José Ramón Morera Campos
Date: 01/12/2025
"""

import os
import sys

#---------------------------------------------------------
# Constants
#---------------------------------------------------------
INPUT_FILE = "../data/day01-1-input.txt"

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
            if direction == "L":
                movement = -int(s[1:]) % 100
            else:
                movement = int(s[1:]) % 100

            position = position + movement
            if position >= 100:
                position = position - 100
            elif position < 0:
                position = position + 100
            if position == 0:
                zero_count += 1
            
    print("zero_count: ", zero_count)
    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)