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

print("get_all_coords() returned:")
gac = game.get_all_coords()
print(f"  type           : {type(gac)}")
print(f"  values (sorted): {sorted(gac)}")
print()

print("find_map_border() returned:")
fmb = game.find_map_border()
print(f"  type           : {type(fmb)}")
print(f"  values (sorted): {sorted(fmb)}")
print()

print("*****************************")
print("* NOTE TO STUDENT           *")
print("*                           *")
print("* The rest of the testcases *")
print("* will always sort the vals *")
print("* above, so that ordering   *")
print("* will not cause testcase   *")
print("* failure.                  *")
print("*****************************")

print("END TESTCASE")

