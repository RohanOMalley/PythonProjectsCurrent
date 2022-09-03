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
print(f"tile04.city_connects(N,N) returned: {carcassonne_tile.tile04.city_connects(N,N)}")
print(f"tile04.city_connects(N,E) returned: {carcassonne_tile.tile04.city_connects(N,E)}")
print(f"tile04.city_connects(N,S) returned: {carcassonne_tile.tile04.city_connects(N,S)}")
print(f"tile04.city_connects(N,W) returned: {carcassonne_tile.tile04.city_connects(N,W)}")
print()
print("skipping E, because it doesn't have a city...")
print()
print("skipping S, because it doesn't have a city...")
print()
print("skipping W, because it doesn't have a city...")
print()

print("END TESTCASE")

