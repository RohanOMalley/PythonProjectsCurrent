#! /usr/bin/python3

""" Code to test the Carcassonne_Tile.edge_has_city() method

    Author: Russ Lewis
"""

import carcassonne_tile

N = 0
E = 1
S = 2
W = 3



print("START TESTCASE")

print(f"tile02.edge_has_city(N) returned: {carcassonne_tile.tile02.edge_has_city(N)}")
print(f"tile02.edge_has_city(E) returned: {carcassonne_tile.tile02.edge_has_city(E)}")
print(f"tile02.edge_has_city(S) returned: {carcassonne_tile.tile02.edge_has_city(S)}")
print(f"tile02.edge_has_city(W) returned: {carcassonne_tile.tile02.edge_has_city(W)}")

print("END TESTCASE")

