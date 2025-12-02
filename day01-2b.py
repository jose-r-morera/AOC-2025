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
#INPUT_FILE = "day01-1-example.txt"


# ---------------------------------------------------------
# Auxiliar Functions
# ---------------------------------------------------------

# ---------------------------------------------------------
# Core Logic
# --------------------------------------------- = int(s------------
def main(args: list[str]) -> int:
    """Main entry point for the script."""

    position = 50
    zero_count = 0
    with open(INPUT_FILE, "r") as file:
        for line in file:
            s = line.strip()
            direction, movement = s[0], int(s[1:])

            zero_count += movement // 100
            movement %= 100
            if direction == 'L':
                new_pos = position - movement
                if new_pos < 0:
                    if position != 0: zero_count += 1
                    new_pos += 100
                elif new_pos == 0: zero_count += 1
            elif direction == 'R':
                new_pos = position + movement
                if new_pos >= 100:
                    zero_count += 1
                    new_pos -= 100
            position = new_pos 

            #print("Current position: ", position, " zero_count: ", zero_count)
            
    print("zero_count: ", zero_count)
    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)