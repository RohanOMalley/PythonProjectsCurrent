#! /usr/bin/python3

""" Code to test the trace_road_one_direction() method of CarcassonneMap

    Author: Russ Lewis
"""

import carcassonne_tile
import carcassonne_map

N = 0
E = 1
S = 2
W = 3



print("START TESTCASE")

print("This map was randomly generated.  This testcase builds the map, and checks every step.")
print("The next testcase will start with this map, and try to extend it in many ways.")
print()

print("Creating the initial map...")
game = carcassonne_map.CarcassonneMap()

print("Adding the many tiles...")
print(f"  add() returned: {game.add( 0, 1, carcassonne_tile.tile13.rotate().rotate())}")
print(f"  add() returned: {game.add( 0,-1, carcassonne_tile.tile10)}")
print(f"  add() returned: {game.add( 1, 0, carcassonne_tile.tile13)}")
print(f"  add() returned: {game.add( 0, 2, carcassonne_tile.tile15.rotate().rotate().rotate())}")
print(f"  add() returned: {game.add(-1, 2, carcassonne_tile.tile04.rotate().rotate())}")
print(f"  add() returned: {game.add(-1,-1, carcassonne_tile.tile01.rotate().rotate())}")
print(f"  add() returned: {game.add(-1, 3, carcassonne_tile.tile13.rotate())}")
print(f"  add() returned: {game.add(-2, 2, carcassonne_tile.tile06.rotate())}")
print(f"  add() returned: {game.add( 1, 2, carcassonne_tile.tile13.rotate().rotate())}")
print(f"  add() returned: {game.add(-2, 1, carcassonne_tile.tile12.rotate().rotate().rotate())}")
print(f"  add() returned: {game.add( 2, 0, carcassonne_tile.tile13)}")
print(f"  add() returned: {game.add(-3, 2, carcassonne_tile.tile11)}")
print(f"  add() returned: {game.add( 2, 2, carcassonne_tile.tile04.rotate().rotate())}")
print(f"  add() returned: {game.add( 3, 0, carcassonne_tile.tile11.rotate())}")
print(f"  add() returned: {game.add( 2,-1, carcassonne_tile.tile01.rotate().rotate().rotate())}")
print()

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

