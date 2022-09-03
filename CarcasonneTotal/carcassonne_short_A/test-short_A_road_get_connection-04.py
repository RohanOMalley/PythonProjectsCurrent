#! /usr/bin/python3

""" Code to test the Carcassonne_Tile.road_get_connection() method

    Author: Russ Lewis
"""

import carcassonne_tile

N = 0
E = 1
S = 2
W = 3



print("START TESTCASE")

print("skipping N, because it doesn't have a road...")
print(f"tile04.road_get_connection(E) returned: {carcassonne_tile.tile04.road_get_connection(E)}")
print(f"tile04.road_get_connection(S) returned: {carcassonne_tile.tile04.road_get_connection(S)}")
print("skipping W, because it doesn't have a road...")

print("END TESTCASE")

