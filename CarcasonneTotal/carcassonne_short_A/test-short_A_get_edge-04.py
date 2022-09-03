#! /usr/bin/python3

""" Code to test the Carcassonne_Tile.get_edge() method

    Author: Russ Lewis
"""

import carcassonne_tile

N = 0
E = 1
S = 2
W = 3



print("START TESTCASE")

print(f"tile04.get_edge(N) returned: {carcassonne_tile.tile04.get_edge(N)}")
print(f"tile04.get_edge(E) returned: {carcassonne_tile.tile04.get_edge(E)}")
print(f"tile04.get_edge(S) returned: {carcassonne_tile.tile04.get_edge(S)}")
print(f"tile04.get_edge(W) returned: {carcassonne_tile.tile04.get_edge(W)}")

print("END TESTCASE")

