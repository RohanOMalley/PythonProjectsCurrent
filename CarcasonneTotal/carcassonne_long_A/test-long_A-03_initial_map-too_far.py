#! /usr/bin/python3

""" Code to test the initial state of the CarcassonneMap class

    Author: Russ Lewis
"""

import carcassonne_tile
import carcassonne_map

N = 0
E = 1
S = 2
W = 3



print("START TESTCASE")

print("Creating the initial map...")
game = carcassonne_map.CarcassonneMap()
print()

print("Adding at (1,1), this should be rejected because it's not adjacent...")
print(f"  add() returned: {game.add(1,1, carcassonne_tile.tile04)}")
print()

print(f"get_all_coords() returned: {sorted(game.get_all_coords())}")
print()

print(f"find_map_border() returned: {sorted(game.find_map_border())}")
print()

print("END TESTCASE")

