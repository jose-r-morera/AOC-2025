#!/usr/bin/env python3
"""
Project: AOC 2025 - Day 08: 
Description: https://adventofcode.com/2025/day/8
Author: José Ramón Morera Campos
Date: 08/12/2025
"""

import sys
from pathlib import Path
import math
import heapq
from collections import defaultdict

#---------------------------------------------------------
# Constants
#---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_FILE = DATA_DIR / "day08-input.txt"
#INPUT_FILE = DATA_DIR / "day08-example.txt"

JUNCTION_PAIRS = 1000
n = 3


# ---------------------------------------------------------
# Auxiliar Functions
# ---------------------------------------------------------
def euclidean_distance(a, b):
    return math.dist(a,b)
    
# ---------------------------------------------------------
# Core Logic
# ---------------------------------------------------------
def main(args: list[str]) -> int:
    """Main entry point for the script."""

    junction_boxes = {} # map of coordinates: group
    with open(INPUT_FILE, "r") as file:
        for lineno, line in enumerate(file):
            coordinates = tuple(int(x) for x in line.strip().split(","))           
            junction_boxes[coordinates] = lineno

    heap = [] # Max sorted heap; smallest element is removed with pop
    keys = list(junction_boxes.keys())  # Get a list of keys

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            d = euclidean_distance(keys[i], keys[j])
            # USE NEGATIVE distance to pop biggest distances
            if len(heap) < JUNCTION_PAIRS:
                heapq.heappush(heap, (-d, i, j))
            else:
                heapq.heappushpop(heap, (-d, i, j))

    best_pairs = sorted((-d, i, j) for d, i, j in heap)

    # Assign groups
    group_length = defaultdict(int)
    for pair in best_pairs:
        box_1_group = junction_boxes[keys[pair[1]]]
        box_2_group = junction_boxes[keys[pair[2]]]
        if box_1_group != box_2_group: 
            if group_length[box_1_group] > group_length[box_2_group]:
                old = box_2_group
                new = box_1_group
            else: 
                old = box_1_group
                new = box_2_group
            # Update groups
            for key in junction_boxes.keys():
                if junction_boxes[key] == old:
                    junction_boxes[key] = new
                    group_length[new] += 1
            group_length[old] = 0
    
    largest_n = heapq.nlargest(n, group_length.items(), key=lambda x: x[1])
    total = 1
    for group in largest_n:
        total *= (group[1] + 1) # +1 as the group length started at 0
    print(total)
   

    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)