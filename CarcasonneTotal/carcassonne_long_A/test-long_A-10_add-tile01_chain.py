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

print("Adding tile01 at (2,0), this should fail because it's too far...")
print(f"  add() returned: {game.add(2,0, carcassonne_tile.tile01)}")
print()

print("Adding tile01 in a long horizontal line, these should all work, including at (2,0)...")
print(f"  add(1,0) returned: {game.add(1,0, carcassonne_tile.tile01)}")
print(f"  add(2,0) returned: {game.add(2,0, carcassonne_tile.tile01)}")
print(f"  add(3,0) returned: {game.add(3,0, carcassonne_tile.tile01)}")
print(f"  add(4,0) returned: {game.add(4,0, carcassonne_tile.tile01)}")
print(f"  add(-1,0) returned: {game.add(-1,0, carcassonne_tile.tile01)}")
print(f"  add(-2,0) returned: {game.add(-2,0, carcassonne_tile.tile01)}")
print(f"  add(-3,0) returned: {game.add(-3,0, carcassonne_tile.tile01)}")
print(f"  add(-4,0) returned: {game.add(-4,0, carcassonne_tile.tile01)}")

print(f"get_all_coords() returned: {sorted(game.get_all_coords())}")
print()

print(f"find_map_border() returned: {sorted(game.find_map_border())}")
print()

print("----------------------------")
print("Dumping the edges of the various tiles:")
print()

for x,y in sorted(game.get_all_coords()):
    print(f"({x},{y})")
    print(f"  {game.get(x,y).get_edge(N)}")
    print(f"  {game.get(x,y).get_edge(E)}")
    print(f"  {game.get(x,y).get_edge(S)}")
    print(f"  {game.get(x,y).get_edge(W)}")
print()

print("END TESTCASE")



# import display_carcassonne_map
# import graphics
# win = graphics.graphics(600,600, "Test")
# display_carcassonne_map.display_map(game, win, 600)
# win.mainloop()

