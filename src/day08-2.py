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

#---------------------------------------------------------
# Constants
#---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_FILE = DATA_DIR / "day08-input.txt"
#INPUT_FILE = DATA_DIR / "day08-example.txt"
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

    keys = list(junction_boxes.keys())  # Get a list of keys

    # Find the box whose shortest distance to any other is the longest among all. 
    longest_shortest = 0 # (only positive distance)
    longest_shortest_key1 = 0
    longest_shortest_key2 = 0

    for i, key1 in enumerate(keys[:-1]):
        shortest = euclidean_distance(key1, keys[i+1]) # start with distance to a different box
        for key2 in keys:
            if key2 == key1: continue
            dist = euclidean_distance(key1, key2)
            shortest = min(dist, shortest) # Could use an if and store closest key here, so key2 is set below
        if shortest > longest_shortest:
            longest_shortest = shortest
            longest_shortest_key1 = key1

    # Retrieve key 2 (could be done inside prev loop, but seems more ineficient)
    for key2 in keys:
        if euclidean_distance(longest_shortest_key1, key2) == longest_shortest:
            longest_shortest_key2 = key2
                
    distance = longest_shortest_key1[0] * longest_shortest_key2[0]
    print(distance)

    return 0


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)