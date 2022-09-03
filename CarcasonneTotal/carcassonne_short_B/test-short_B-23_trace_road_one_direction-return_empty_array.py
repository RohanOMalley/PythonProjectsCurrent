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
game.add( 0, 1, carcassonne_tile.tile02.rotate().rotate().rotate(), confirm=False)
game.add( 0, 2, carcassonne_tile.tile05                           , confirm=False)
game.add(-1, 2, carcassonne_tile.tile07                           , confirm=False)
game.add(-1, 3, carcassonne_tile.tile06.rotate()                  , confirm=False)
game.add( 1, 2, carcassonne_tile.tile08                           , confirm=False)
game.add( 1, 3, carcassonne_tile.tile09.rotate().rotate().rotate(), confirm=False)
game.add( 2, 2, carcassonne_tile.tile12.rotate().rotate().rotate(), confirm=False)
game.add( 3, 2, carcassonne_tile.tile12.rotate()                  , confirm=False)
game.add(-1, 0, carcassonne_tile.tile03                           , confirm=False)
game.add(-2, 0, carcassonne_tile.tile12.rotate().rotate()         , confirm=False)
game.add(-2,-1, carcassonne_tile.tile05                           , confirm=False)
game.add(-2,-2, carcassonne_tile.tile11.rotate()                  , confirm=False)
game.add( 1, 0, carcassonne_tile.tile06.rotate()                  , confirm=False)
game.add( 0,-1, carcassonne_tile.tile09.rotate()                  , confirm=False)
game.add( 0,-2, carcassonne_tile.tile05                           , confirm=False)
game.add( 0,-3, carcassonne_tile.tile07.rotate()                  , confirm=False)
game.add( 1,-1, carcassonne_tile.tile08                           , confirm=False)
game.add( 2,-1, carcassonne_tile.tile08                           , confirm=False)
game.add( 1,-2, carcassonne_tile.tile07                           , confirm=False)
game.add( 2,-2, carcassonne_tile.tile08                           , confirm=False)
print()

print("Calling trace_road_one_direction() on a few locations...")
print(f"  t_r_o_d(-1, 3,W) returned: {game.trace_road_one_direction(-1, 3,W)}")
print(f"  t_r_o_d(-1, 3,E) returned: {game.trace_road_one_direction(-1, 3,E)}")
print(f"  t_r_o_d( 2, 2,S) returned: {game.trace_road_one_direction( 2, 2,S)}")
print(f"  t_r_o_d( 3, 2,N) returned: {game.trace_road_one_direction( 3, 2,N)}")
print(f"  t_r_o_d( 1, 0,E) returned: {game.trace_road_one_direction( 1, 0,E)}")
print(f"  t_r_o_d(-1, 0,N) returned: {game.trace_road_one_direction(-1, 0,N)}")
print(f"  t_r_o_d(-1, 0,S) returned: {game.trace_road_one_direction(-1, 0,S)}")
print(f"  t_r_o_d(-2, 0,N) returned: {game.trace_road_one_direction(-2, 0,N)}")
print(f"  t_r_o_d(-2,-2,W) returned: {game.trace_road_one_direction(-2,-2,W)}")
print(f"  t_r_o_d(-2,-2,S) returned: {game.trace_road_one_direction(-2,-2,S)}")

print("END TESTCASE")



# import display_carcassonne_map
# import graphics
# win = graphics.graphics(600,600, "Test")
# display_carcassonne_map.display_map(game, win, 600)
# win.mainloop()

