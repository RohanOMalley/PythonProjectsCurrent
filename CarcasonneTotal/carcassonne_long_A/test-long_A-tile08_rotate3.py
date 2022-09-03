#! /usr/bin/python3

""" Code to test one of the Carcassonne tiles

    Author: Russ Lewis
"""

import carcassonne_tile

N = 0
E = 1
S = 2
W = 3



print("START TESTCASE: Testing all methods for tile08, rotated three times")
the_tile = carcassonne_tile.tile08.rotate().rotate().rotate()

print(f"get_edge(N) returned: {the_tile.get_edge(N)}")
print(f"get_edge(E) returned: {the_tile.get_edge(E)}")
print(f"get_edge(S) returned: {the_tile.get_edge(S)}")
print(f"get_edge(W) returned: {the_tile.get_edge(W)}")
print()

print("edge_has_road() and edge_has_city():")
print(f"  {the_tile.edge_has_road(N)} {the_tile.edge_has_city(N)}")
print(f"  {the_tile.edge_has_road(E)} {the_tile.edge_has_city(E)}")
print(f"  {the_tile.edge_has_road(S)} {the_tile.edge_has_city(S)}")
print(f"  {the_tile.edge_has_road(W)} {the_tile.edge_has_city(W)}")
print()

print(f"has_crossroads(): {the_tile.has_crossroads()}")
print()

print("Road connections:")
if the_tile.edge_has_road(N):
    print(f"  road_get_connection(N): {the_tile.road_get_connection(N)}")
if the_tile.edge_has_road(E):
    print(f"  road_get_connection(E): {the_tile.road_get_connection(E)}")
if the_tile.edge_has_road(S):
    print(f"  road_get_connection(S): {the_tile.road_get_connection(S)}")
if the_tile.edge_has_road(W):
    print(f"  road_get_connection(W): {the_tile.road_get_connection(W)}")
print()

print("City connections:")
if the_tile.edge_has_city(N):
    print(f"  city_connects(N,N): {the_tile.city_connects(N,N)}")
    print(f"  city_connects(N,E): {the_tile.city_connects(N,E)}")
    print(f"  city_connects(N,S): {the_tile.city_connects(N,S)}")
    print(f"  city_connects(N,W): {the_tile.city_connects(N,W)}")
    print("--")
if the_tile.edge_has_city(E):
    print(f"  city_connects(E,N): {the_tile.city_connects(E,N)}")
    print(f"  city_connects(E,E): {the_tile.city_connects(E,E)}")
    print(f"  city_connects(E,S): {the_tile.city_connects(E,S)}")
    print(f"  city_connects(E,W): {the_tile.city_connects(E,W)}")
    print("--")
if the_tile.edge_has_city(S):
    print(f"  city_connects(S,N): {the_tile.city_connects(S,N)}")
    print(f"  city_connects(S,E): {the_tile.city_connects(S,E)}")
    print(f"  city_connects(S,S): {the_tile.city_connects(S,S)}")
    print(f"  city_connects(S,W): {the_tile.city_connects(S,W)}")
    print("--")
if the_tile.edge_has_city(W):
    print(f"  city_connects(W,N): {the_tile.city_connects(W,N)}")
    print(f"  city_connects(W,E): {the_tile.city_connects(W,E)}")
    print(f"  city_connects(W,S): {the_tile.city_connects(W,S)}")
    print(f"  city_connects(W,W): {the_tile.city_connects(W,W)}")
    print("--")
print()

print("END TESTCASE")

