#!/usr/bin/env python3
"""
Project: AOC 2025 - Day 03:  PART 2
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
def max_k_digits_in_order(s: str, k: int):
    """
    Return the largest k-digit number obtainable by choosing k digits
    from s without reordering. 

    Greedy traverse where the last stored digits are popped if larger appear
    (eg, from 85173 stored we might pop 3, 7, 1 if 8 appear and we can still reach k digits,
    getting 858xx)
    """
    n = len(s)
    stack = []
    for i, ch in enumerate(s):
        # pop while we can (to replace a smaller digit) still reach k digits later:
        while stack and stack[-1][0] < ch and (len(stack) - 1 + (n - i)) >= k:
            stack.pop()
        # push current digit
        stack.append(ch)

    # we might have more than k in stack (if never popped enough); take first k
    chosen = stack[:k]
    digits_str = ''.join(chosen)
    return int(digits_str)

# ---------------------------------------------------------
# Core Logic
# ---------------------------------------------------------
def main(args: list[str]) -> int:
    """Main entry point for the script."""

    total = 0
    with open(INPUT_FILE, "r") as file:

        for line in file:
            s = line.strip()
            total += max_k_digits_in_order(s, 12)
        print(total)
    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)