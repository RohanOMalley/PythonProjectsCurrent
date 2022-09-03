#! /usr/bin/python3

""" Code to test the Carcassonne_Tile.has_crossroads() method

    Author: Russ Lewis
"""

import carcassonne_tile

N = 0
E = 1
S = 2
W = 3



print("START TESTCASE")

print(f"tile01.has_crossroads() returned: {carcassonne_tile.tile01.has_crossroads()}")
print(f"tile02.has_crossroads() returned: {carcassonne_tile.tile02.has_crossroads()}")
print(f"tile03.has_crossroads() returned: {carcassonne_tile.tile03.has_crossroads()}")
print(f"tile04.has_crossroads() returned: {carcassonne_tile.tile04.has_crossroads()}")

print("END TESTCASE")

