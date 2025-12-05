#!/usr/bin/env python3
"""
Project: AOC 2025 - Day 06: 
Description: https://adventofcode.com/2025/day/6
Author: José Ramón Morera Campos
Date: 06/12/2025
"""

import os
import sys
from pathlib import Path

#---------------------------------------------------------
# Constants
#---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_FILE = DATA_DIR / "day06-1-input.txt"
#INPUT_FILE = DATA_DIR / "day06-1-example.txt"

# ---------------------------------------------------------
# Auxiliar Functions
# ---------------------------------------------------------

# ---------------------------------------------------------
# Core Logic
# ---------------------------------------------------------
def main(args: list[str]) -> int:
    """Main entry point for the script."""

    with open(INPUT_FILE, "r") as file:
        for line in file:
            s = line.strip()
    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)