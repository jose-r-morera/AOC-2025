#!/usr/bin/env python3
"""
Project: AOC 2025 - Day NUMBER: 
Description: https://adventofcode.com/2025/day/NUMBER
Author: José Ramón Morera Campos
Date: NUMBER/12/2025
"""

import os
import sys

#---------------------------------------------------------
# Constants
#---------------------------------------------------------
INPUT_FILE = "dayNUMBER-1-input.txt"
#INPUT_FILE = "dayNUMBER-1-example.txt"


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