#! /usr/bin/python3

""" Code to test the Carcassonne_Tile.city_connects() method

    Author: Russ Lewis
"""

import carcassonne_tile

N = 0
E = 1
S = 2
W = 3



print("START TESTCASE")

print()
print(f"tile02.city_connects(N,N) returned: {carcassonne_tile.tile02.city_connects(N,N)}")
print(f"tile02.city_connects(N,E) returned: {carcassonne_tile.tile02.city_connects(N,E)}")
print(f"tile02.city_connects(N,S) returned: {carcassonne_tile.tile02.city_connects(N,S)}")
print(f"tile02.city_connects(N,W) returned: {carcassonne_tile.tile02.city_connects(N,W)}")
print()
print(f"tile02.city_connects(E,N) returned: {carcassonne_tile.tile02.city_connects(E,N)}")
print(f"tile02.city_connects(E,E) returned: {carcassonne_tile.tile02.city_connects(E,E)}")
print(f"tile02.city_connects(E,S) returned: {carcassonne_tile.tile02.city_connects(E,S)}")
print(f"tile02.city_connects(E,W) returned: {carcassonne_tile.tile02.city_connects(E,W)}")
print()
print("skipping S, because it doesn't have a city...")
print()
print(f"tile02.city_connects(W,N) returned: {carcassonne_tile.tile02.city_connects(W,N)}")
print(f"tile02.city_connects(W,E) returned: {carcassonne_tile.tile02.city_connects(W,E)}")
print(f"tile02.city_connects(W,S) returned: {carcassonne_tile.tile02.city_connects(W,S)}")
print(f"tile02.city_connects(W,W) returned: {carcassonne_tile.tile02.city_connects(W,W)}")
print()

print("END TESTCASE")

