#!/usr/bin/env python3
"""
Project: AOC 2025 - Day 02: 
Description: https://adventofcode.com/2025/day/02
Author: José Ramón Morera Campos
Date: 02/12/2025
"""

import os
import sys
import re
#---------------------------------------------------------
# Constants
#---------------------------------------------------------
INPUT_FILE = "../data/day02-1-input.txt"
#INPUT_FILE = "day02-1-example.txt"


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
            s = line.strip().split(sep=",")

    count = 0
    for i in range(len(s)):
        interval = s[i].split(sep="-")
        for i in range(int(interval[0]), int(interval[1]) + 1):
            # Alternative: use re.fullmatch(r'^([0-9]+)\1+$', str(i))
            for group_size in range(1, len(str(i)) // 2 + 1):
                group = str(i)[:group_size]
                if re.fullmatch(f"^({group})+$", str(i)):
                    count += i
                    break


    print(f"Total count: {count}")
    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)