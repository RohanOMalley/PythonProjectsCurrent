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
game.add( 0, 1, carcassonne_tile.tile13.rotate().rotate()         , confirm=False)
game.add( 0,-1, carcassonne_tile.tile10                           , confirm=False)
game.add( 1, 0, carcassonne_tile.tile13                           , confirm=False)
game.add( 0, 2, carcassonne_tile.tile15.rotate().rotate().rotate(), confirm=False)
game.add(-1, 2, carcassonne_tile.tile04.rotate().rotate()         , confirm=False)
game.add(-1,-1, carcassonne_tile.tile01.rotate().rotate()         , confirm=False)
game.add(-1, 3, carcassonne_tile.tile13.rotate()                  , confirm=False)
game.add(-2, 2, carcassonne_tile.tile06.rotate()                  , confirm=False)
game.add( 1, 2, carcassonne_tile.tile13.rotate().rotate()         , confirm=False)
game.add(-2, 1, carcassonne_tile.tile12.rotate().rotate().rotate(), confirm=False)
game.add( 2, 0, carcassonne_tile.tile13                           , confirm=False)
game.add(-3, 2, carcassonne_tile.tile11                           , confirm=False)
game.add( 2, 2, carcassonne_tile.tile04.rotate().rotate()         , confirm=False)
game.add( 3, 0, carcassonne_tile.tile11.rotate()                  , confirm=False)
game.add( 2,-1, carcassonne_tile.tile01.rotate().rotate().rotate(), confirm=False)
print()

print("Calling trace_road_one_direction() on a few locations...")
for x,y in sorted(game.get_all_coords()):
    for i in range(4):
        if game.get(x,y).get_edge(i) == "grass+road":
            print(f"  t_r_o_d({x},{y},{i}) returned: {game.trace_road_one_direction(x,y,i)}")
print()

print("END TESTCASE")



import display_carcassonne_map
import graphics
win = graphics.graphics(600,600, "Test")
display_carcassonne_map.display_map(game, win, 600)
win.mainloop()

