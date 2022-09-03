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

print("This map was randomly generated.  This testcase builds the map, and checks every step.")
print("The next testcase will start with this map, and try to extend it in many ways.")
print()

print("Creating the initial map...")
game = carcassonne_map.CarcassonneMap()
print()

print("Each of these add() operations should return True...")
print(f"  add( 0, 1) returned: {game.add( 0, 1, carcassonne_tile.tile02.rotate().rotate().rotate(), confirm=False)}")
print(f"  add( 0, 2) returned: {game.add( 0, 2, carcassonne_tile.tile05                           , confirm=False)}")
print(f"  add(-1, 2) returned: {game.add(-1, 2, carcassonne_tile.tile07                           , confirm=False)}")
print(f"  add(-1, 3) returned: {game.add(-1, 3, carcassonne_tile.tile06.rotate()                  , confirm=False)}")
print(f"  add( 1, 2) returned: {game.add( 1, 2, carcassonne_tile.tile08                           , confirm=False)}")
print(f"  add( 1, 3) returned: {game.add( 1, 3, carcassonne_tile.tile09.rotate().rotate().rotate(), confirm=False)}")
print(f"  add( 2, 2) returned: {game.add( 2, 2, carcassonne_tile.tile12.rotate().rotate().rotate(), confirm=False)}")
print(f"  add( 3, 2) returned: {game.add( 3, 2, carcassonne_tile.tile12.rotate()                  , confirm=False)}")
print(f"  add(-1, 0) returned: {game.add(-1, 0, carcassonne_tile.tile03                           , confirm=False)}")
print(f"  add(-2, 0) returned: {game.add(-2, 0, carcassonne_tile.tile12.rotate().rotate()         , confirm=False)}")
print(f"  add(-2,-1) returned: {game.add(-2,-1, carcassonne_tile.tile05                           , confirm=False)}")
print(f"  add(-2,-2) returned: {game.add(-2,-2, carcassonne_tile.tile11.rotate()                  , confirm=False)}")
print(f"  add( 1, 0) returned: {game.add( 1, 0, carcassonne_tile.tile06.rotate()                  , confirm=False)}")
print(f"  add( 0,-1) returned: {game.add( 0,-1, carcassonne_tile.tile09.rotate()                  , confirm=False)}")
print(f"  add( 0,-2) returned: {game.add( 0,-2, carcassonne_tile.tile05                           , confirm=False)}")
print(f"  add( 0,-3) returned: {game.add( 0,-3, carcassonne_tile.tile07.rotate()                  , confirm=False)}")
print(f"  add( 1,-1) returned: {game.add( 1,-1, carcassonne_tile.tile08                           , confirm=False)}")
print(f"  add( 2,-1) returned: {game.add( 2,-1, carcassonne_tile.tile08                           , confirm=False)}")
print(f"  add( 1,-2) returned: {game.add( 1,-2, carcassonne_tile.tile07                           , confirm=False)}")
print(f"  add( 2,-2) returned: {game.add( 2,-2, carcassonne_tile.tile08                           , confirm=False)}")
print()

print(f"get_all_coords() returned: {sorted(game.get_all_coords())}")
print()

print(f"find_map_border() returned: {sorted(game.find_map_border())}")
print()

print("Each of these add() operations should fail...")
for x,y in sorted(game.get_all_coords()):
    print(f"  add() returned: {game.add(x,y, carcassonne_tile.tile01)}")
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

