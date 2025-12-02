#!/usr/bin/env python3
"""
Project: AOC 2025 - Day 1: Secret Entrance; PART 2
Description: https://adventofcode.com/2025/day/1
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
                movement = -int(s[1:])
            else:
                movement = int(s[1:])

            # Use cummulative position and // operator, which defines intervals [-100, 0), [0, 100), [100, 200), ... 
            # Due to that, we have to handle the case where we move to the left and land on boundary x%100 == 0
            # as it is one extra lap unaccounted by the integer division

            # Special case, we are already on boundary x%100 == 0
            if position % 100 == 0:
                zero_count += abs(movement) // 100
                position += movement
            # Regural case, we are not on boundary
            else:
                previous_laps = position // 100
                position += movement
                current_laps = position // 100
                zero_count += abs(current_laps - previous_laps)
                # Case where we land exactly on 0
                if position % 100 == 0 and movement < 0:
                        zero_count += 1
            
    print("zero_count: ", zero_count)
    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)