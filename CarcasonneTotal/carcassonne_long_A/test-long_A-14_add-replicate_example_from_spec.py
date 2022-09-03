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

print("Adding two tiles (with confirm=False); these should never fail...")
print(f"  add() returned: {game.add(1,0, carcassonne_tile.tile06.rotate(), confirm=False)}")
print(f"  add() returned: {game.add(2,0, carcassonne_tile.tile10,          confirm=False)}")
print(f"  get_all_coords() returned: {sorted(game.get_all_coords())}")
print(f"  find_map_border() returned: {sorted(game.find_map_border())}")
print()

print("These two add() attempts should fail")
print(f"  add() returned: {game.add(0, 1, carcassonne_tile.tile06.rotate())}")
print(f"  add() returned: {game.add(2,-1, carcassonne_tile.tile06.rotate())}")
print(f"  get_all_coords() returned: {sorted(game.get_all_coords())}")
print(f"  find_map_border() returned: {sorted(game.find_map_border())}")
print()

print("This add() attempt should succeed")
print(f"  add() returned: {game.add(2,-1, carcassonne_tile.tile06)}")
print(f"  get_all_coords() returned: {sorted(game.get_all_coords())}")
print(f"  find_map_border() returned: {sorted(game.find_map_border())}")
print()

print("This add() attempt should fail")
print(f"  add() returned: {game.add(1,-1, carcassonne_tile.tile07.rotate())}")
print(f"  get_all_coords() returned: {sorted(game.get_all_coords())}")
print(f"  find_map_border() returned: {sorted(game.find_map_border())}")
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

