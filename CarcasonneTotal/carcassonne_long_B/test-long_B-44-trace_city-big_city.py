#! /usr/bin/python3

""" Code to test the trace_city() method of CarcassonneMap

    Author: Russ Lewis
"""

import carcassonne_tile
import carcassonne_map

N = 0
E = 1
S = 2
W = 3



def city_sort(city):
    # we have to sort the set of city elements, since sets do not have a
    # defined order.  But we can't just call sorted() on the trace_city()
    # retval, because it's a (bool,set) tuple
    closed,elements = city
    return (closed, sorted(elements))



print("START TESTCASE")

print("Creating the initial map...")
game = carcassonne_map.CarcassonneMap()
print()

print("This is the a looping city that a student dreamed up...")
print(f"  game.add(-1,0, ... ) returned: {game.add(-1,0, carcassonne_tile.tile01                           )}")
print(f"  game.add( 1,0, ... ) returned: {game.add( 1,0, carcassonne_tile.tile01                           )}")
print(f"  game.add(-1,1, ... ) returned: {game.add(-1,1, carcassonne_tile.tile05                           )}")
print(f"  game.add(-2,1, ... ) returned: {game.add(-2,1, carcassonne_tile.tile16.rotate()                  )}")
print(f"  game.add( 0,1, ... ) returned: {game.add( 0,1, carcassonne_tile.tile05                           )}")
print(f"  game.add( 1,1, ... ) returned: {game.add( 1,1, carcassonne_tile.tile05                           )}")
print(f"  game.add( 2,1, ... ) returned: {game.add( 2,1, carcassonne_tile.tile16.rotate().rotate().rotate())}")
print(f"  game.add(-2,2, ... ) returned: {game.add(-2,2, carcassonne_tile.tile16.rotate()                  )}")
print(f"  game.add(-1,2, ... ) returned: {game.add(-1,2, carcassonne_tile.tile05                           )}")
print(f"  game.add( 0,2, ... ) returned: {game.add( 0,2, carcassonne_tile.tile05                           )}")
print(f"  game.add( 1,2, ... ) returned: {game.add( 1,2, carcassonne_tile.tile05                           )}")
print(f"  game.add( 2,2, ... ) returned: {game.add( 2,2, carcassonne_tile.tile16.rotate().rotate().rotate())}")
print(f"  game.add(-2,3, ... ) returned: {game.add(-2,3, carcassonne_tile.tile16.rotate()                  )}")
print(f"  game.add(-1,3, ... ) returned: {game.add(-1,3, carcassonne_tile.tile05                           )}")
print(f"  game.add( 0,3, ... ) returned: {game.add( 0,3, carcassonne_tile.tile05                           )}")
print(f"  game.add( 1,3, ... ) returned: {game.add( 1,3, carcassonne_tile.tile05                           )}")
print(f"  game.add( 2,3, ... ) returned: {game.add( 2,3, carcassonne_tile.tile16.rotate().rotate().rotate())}")
print(f"  game.add(-1,4, ... ) returned: {game.add(-1,4, carcassonne_tile.tile01.rotate().rotate()         )}")
print(f"  game.add( 0,4, ... ) returned: {game.add( 0,4, carcassonne_tile.tile01.rotate().rotate()         )}")
print(f"  game.add( 1,4, ... ) returned: {game.add( 1,4, carcassonne_tile.tile01.rotate().rotate()         )}")
print()

print("Calling trace_city() from various start points:")
print(f"  t_c(0,3,W) returned: {city_sort(game.trace_city(0,3,W))}")
print()

print("END TESTCASE")



# import display_carcassonne_map
# import graphics
# win = graphics.graphics(600,600, "Test")
# display_carcassonne_map.display_map(game, win, 600)
# win.mainloop()

