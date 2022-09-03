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

print("Attempting to overwrite the origin with another copy of tile01, this should be rejected...")
print(f"  add() returned: {game.add(0,0, carcassonne_tile.tile01)}")
print("Attempting to overwrite the origin with another copy of tile02, this should be rejected...")
print(f"  add() returned: {game.add(0,0, carcassonne_tile.tile02)}")
print("Attempting to overwrite the origin with another copy of tile08, this should be rejected...")
print(f"  add() returned: {game.add(0,0, carcassonne_tile.tile08)}")
print()

print("The sides of (0,0) are now:")
print(f"  {game.get(0,0).get_edge(N)}")
print(f"  {game.get(0,0).get_edge(E)}")
print(f"  {game.get(0,0).get_edge(S)}")
print(f"  {game.get(0,0).get_edge(W)}")
print()

print(f"get_all_coords() returned: {sorted(game.get_all_coords())}")
print()

print(f"find_map_border() returned: {sorted(game.find_map_border())}")
print()

print("END TESTCASE")

