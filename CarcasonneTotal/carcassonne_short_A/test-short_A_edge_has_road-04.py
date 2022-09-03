#! /usr/bin/python3

""" Code to test the Carcassonne_Tile.edge_has_road() method

    Author: Russ Lewis
"""

import carcassonne_tile

N = 0
E = 1
S = 2
W = 3



print("START TESTCASE")

print(f"tile04.edge_has_road(N) returned: {carcassonne_tile.tile04.edge_has_road(N)}")
print(f"tile04.edge_has_road(E) returned: {carcassonne_tile.tile04.edge_has_road(E)}")
print(f"tile04.edge_has_road(S) returned: {carcassonne_tile.tile04.edge_has_road(S)}")
print(f"tile04.edge_has_road(W) returned: {carcassonne_tile.tile04.edge_has_road(W)}")

print("END TESTCASE")

