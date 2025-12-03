#!/usr/bin/env python3
"""
Project: AOC 2025 - Day 03: 
Description: https://adventofcode.com/2025/day/03
Author: José Ramón Morera Campos
Date: 03/12/2025
"""

import os
import sys
from pathlib import Path


#---------------------------------------------------------
# Constants
#---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_FILE = DATA_DIR / "day03-1-input.txt"
#INPUT_FILE = DATA_DIR / "day03-1-example.txt"


# ---------------------------------------------------------
# Auxiliar Functions
# ---------------------------------------------------------

# ---------------------------------------------------------
# Core Logic
# ---------------------------------------------------------
def main(args: list[str]) -> int:
    """Main entry point for the script."""

    total = 0
    with open(INPUT_FILE, "r") as file:

        for line in file:
            best_number = -1 
            best_second_digit = -1
            s = line.strip()
            # Travel in reverse to expoit choosing the biggest second digit before the first
            for c in reversed(s):
                digit = int(c)
                
                # try pairing this digit as the first digit
                if best_second_digit != -1:
                    best_number = max(best_number, digit * 10 + best_second_digit)
                
                best_second_digit = max(best_second_digit, digit)
            #print(f"Best for line '{s}' is {best_number}")
                
            total += best_number
        print(total)
    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)