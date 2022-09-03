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

print(f"tile03.road_get_connection(N) returned: {carcassonne_tile.tile03.road_get_connection(N)}")
print(f"tile03.road_get_connection(E) returned: {carcassonne_tile.tile03.road_get_connection(E)}")
print(f"tile03.road_get_connection(S) returned: {carcassonne_tile.tile03.road_get_connection(S)}")
print(f"tile03.road_get_connection(W) returned: {carcassonne_tile.tile03.road_get_connection(W)}")

print("END TESTCASE")

