#!/usr/bin/env python3
"""
Project: AOC 2025 - Day 05: 
Description: https://adventofcode.com/2025/day/5
Author: José Ramón Morera Campos
Date: 05/12/2025
"""

import os
import sys
from pathlib import Path

#---------------------------------------------------------
# Constants
#---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_FILE = DATA_DIR / "day05-1-input.txt"
#INPUT_FILE = DATA_DIR / "day05-1-example.txt"

# ---------------------------------------------------------
# Auxiliar Functions
# ---------------------------------------------------------
def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x[0]) # sort by first element
    
    if intervals:
        result = [intervals[0]]
        for val in intervals[1:]:
            if val[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], val[1])
            else:
                result.append(val)
    else: 
        result = []
    return result

# ---------------------------------------------------------
# Core Logic
# ---------------------------------------------------------
def main(args: list[str]) -> int:
    """Main entry point for the script."""

    intervals = []
    fresh_count = 0

    with open(INPUT_FILE, "r") as file:
        for line in file:
            s = line.strip()
            if s == "":
                break
            else: 
                begin, end = s.split("-")
                intervals.append([int(begin), int(end)])
        
        merged = mergeIntervals(intervals)

        for interval in merged:
            fresh_count += interval[1] - interval[0] + 1

        print(f"Number of fresh items: {fresh_count}")

    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)