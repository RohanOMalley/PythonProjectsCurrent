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
print()

print("This testcase calls add() many times, trying tiles 1 through 12.")
print("It tries to add each tile in all four legit locations.  However,")
print("it will pass the tryOnly=True parameter each time, so the map should")
print("never change.")
print()

print("Creating the initial map...")
game = carcassonne_map.CarcassonneMap()
print()



print(f"add( 0, 1, tile01, tryOnly=True) returned: {game.add( 0, 1, carcassonne_tile.tile01, tryOnly=True)}")
print(f"add( 0,-1, tile01, tryOnly=True) returned: {game.add( 0,-1, carcassonne_tile.tile01, tryOnly=True)}")
print(f"add( 1, 0, tile01, tryOnly=True) returned: {game.add( 1, 0, carcassonne_tile.tile01, tryOnly=True)}")
print(f"add(-1, 0, tile01, tryOnly=True) returned: {game.add(-1, 0, carcassonne_tile.tile01, tryOnly=True)}")
print()

print(f"add( 0, 1, tile02, tryOnly=True) returned: {game.add( 0, 1, carcassonne_tile.tile02, tryOnly=True)}")
print(f"add( 0,-1, tile02, tryOnly=True) returned: {game.add( 0,-1, carcassonne_tile.tile02, tryOnly=True)}")
print(f"add( 1, 0, tile02, tryOnly=True) returned: {game.add( 1, 0, carcassonne_tile.tile02, tryOnly=True)}")
print(f"add(-1, 0, tile02, tryOnly=True) returned: {game.add(-1, 0, carcassonne_tile.tile02, tryOnly=True)}")
print()

print(f"add( 0, 1, tile03, tryOnly=True) returned: {game.add( 0, 1, carcassonne_tile.tile03, tryOnly=True)}")
print(f"add( 0,-1, tile03, tryOnly=True) returned: {game.add( 0,-1, carcassonne_tile.tile03, tryOnly=True)}")
print(f"add( 1, 0, tile03, tryOnly=True) returned: {game.add( 1, 0, carcassonne_tile.tile03, tryOnly=True)}")
print(f"add(-1, 0, tile03, tryOnly=True) returned: {game.add(-1, 0, carcassonne_tile.tile03, tryOnly=True)}")
print()

print(f"add( 0, 1, tile04, tryOnly=True) returned: {game.add( 0, 1, carcassonne_tile.tile04, tryOnly=True)}")
print(f"add( 0,-1, tile04, tryOnly=True) returned: {game.add( 0,-1, carcassonne_tile.tile04, tryOnly=True)}")
print(f"add( 1, 0, tile04, tryOnly=True) returned: {game.add( 1, 0, carcassonne_tile.tile04, tryOnly=True)}")
print(f"add(-1, 0, tile04, tryOnly=True) returned: {game.add(-1, 0, carcassonne_tile.tile04, tryOnly=True)}")
print()

print(f"add( 0, 1, tile05, tryOnly=True) returned: {game.add( 0, 1, carcassonne_tile.tile05, tryOnly=True)}")
print(f"add( 0,-1, tile05, tryOnly=True) returned: {game.add( 0,-1, carcassonne_tile.tile05, tryOnly=True)}")
print(f"add( 1, 0, tile05, tryOnly=True) returned: {game.add( 1, 0, carcassonne_tile.tile05, tryOnly=True)}")
print(f"add(-1, 0, tile05, tryOnly=True) returned: {game.add(-1, 0, carcassonne_tile.tile05, tryOnly=True)}")
print()

print(f"add( 0, 1, tile06, tryOnly=True) returned: {game.add( 0, 1, carcassonne_tile.tile06, tryOnly=True)}")
print(f"add( 0,-1, tile06, tryOnly=True) returned: {game.add( 0,-1, carcassonne_tile.tile06, tryOnly=True)}")
print(f"add( 1, 0, tile06, tryOnly=True) returned: {game.add( 1, 0, carcassonne_tile.tile06, tryOnly=True)}")
print(f"add(-1, 0, tile06, tryOnly=True) returned: {game.add(-1, 0, carcassonne_tile.tile06, tryOnly=True)}")
print()

print(f"add( 0, 1, tile07, tryOnly=True) returned: {game.add( 0, 1, carcassonne_tile.tile07, tryOnly=True)}")
print(f"add( 0,-1, tile07, tryOnly=True) returned: {game.add( 0,-1, carcassonne_tile.tile07, tryOnly=True)}")
print(f"add( 1, 0, tile07, tryOnly=True) returned: {game.add( 1, 0, carcassonne_tile.tile07, tryOnly=True)}")
print(f"add(-1, 0, tile07, tryOnly=True) returned: {game.add(-1, 0, carcassonne_tile.tile07, tryOnly=True)}")
print()

print(f"add( 0, 1, tile08, tryOnly=True) returned: {game.add( 0, 1, carcassonne_tile.tile08, tryOnly=True)}")
print(f"add( 0,-1, tile08, tryOnly=True) returned: {game.add( 0,-1, carcassonne_tile.tile08, tryOnly=True)}")
print(f"add( 1, 0, tile08, tryOnly=True) returned: {game.add( 1, 0, carcassonne_tile.tile08, tryOnly=True)}")
print(f"add(-1, 0, tile08, tryOnly=True) returned: {game.add(-1, 0, carcassonne_tile.tile08, tryOnly=True)}")
print()

print(f"add( 0, 1, tile09, tryOnly=True) returned: {game.add( 0, 1, carcassonne_tile.tile09, tryOnly=True)}")
print(f"add( 0,-1, tile09, tryOnly=True) returned: {game.add( 0,-1, carcassonne_tile.tile09, tryOnly=True)}")
print(f"add( 1, 0, tile09, tryOnly=True) returned: {game.add( 1, 0, carcassonne_tile.tile09, tryOnly=True)}")
print(f"add(-1, 0, tile09, tryOnly=True) returned: {game.add(-1, 0, carcassonne_tile.tile09, tryOnly=True)}")
print()

print(f"add( 0, 1, tile10, tryOnly=True) returned: {game.add( 0, 1, carcassonne_tile.tile10, tryOnly=True)}")
print(f"add( 0,-1, tile10, tryOnly=True) returned: {game.add( 0,-1, carcassonne_tile.tile10, tryOnly=True)}")
print(f"add( 1, 0, tile10, tryOnly=True) returned: {game.add( 1, 0, carcassonne_tile.tile10, tryOnly=True)}")
print(f"add(-1, 0, tile10, tryOnly=True) returned: {game.add(-1, 0, carcassonne_tile.tile10, tryOnly=True)}")
print()

print(f"add( 0, 1, tile11, tryOnly=True) returned: {game.add( 0, 1, carcassonne_tile.tile11, tryOnly=True)}")
print(f"add( 0,-1, tile11, tryOnly=True) returned: {game.add( 0,-1, carcassonne_tile.tile11, tryOnly=True)}")
print(f"add( 1, 0, tile11, tryOnly=True) returned: {game.add( 1, 0, carcassonne_tile.tile11, tryOnly=True)}")
print(f"add(-1, 0, tile11, tryOnly=True) returned: {game.add(-1, 0, carcassonne_tile.tile11, tryOnly=True)}")
print()

print(f"add( 0, 1, tile12, tryOnly=True) returned: {game.add( 0, 1, carcassonne_tile.tile12, tryOnly=True)}")
print(f"add( 0,-1, tile12, tryOnly=True) returned: {game.add( 0,-1, carcassonne_tile.tile12, tryOnly=True)}")
print(f"add( 1, 0, tile12, tryOnly=True) returned: {game.add( 1, 0, carcassonne_tile.tile12, tryOnly=True)}")
print(f"add(-1, 0, tile12, tryOnly=True) returned: {game.add(-1, 0, carcassonne_tile.tile12, tryOnly=True)}")
print()




print("----------------------------------")
print("All of the add() calls have completed.  Because we passed tryOnly=True")
print("every time, no new tiles should have been added.  Testing this...")
print()

print(f"get_all_coords() returned: {sorted(game.get_all_coords())}")
print()

print(f"find_map_border() returned: {sorted(game.find_map_border())}")
print()

print("END TESTCASE")

