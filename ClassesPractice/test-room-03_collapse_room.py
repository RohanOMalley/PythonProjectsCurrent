#! /usr/bin/env python3


import classes_prob3



print("TESTING A 6x4 GRID.")
print()



print("Calling build_grid(6,4)...")
sw_corner = classes_prob3.build_grid(6,4)
print()



print("Finding the room 3 east, 2 north from the retval...")
print()

targ = sw_corner.e.e.e.n.n



print("Finding the 4 neighbors of that object...")
print()

n = targ.n
s = targ.s
w = targ.w
e = targ.e



print("Checking the incoming links to the target room...")
print()

assert n.s is targ
assert s.n is targ
assert w.e is targ
assert e.w is targ



print("Collapsing the target room...")
print()

targ.collapse_room()



print("Checking the links inside the target room...")
print(f"  North: {targ.n}")
print(f"  South: {targ.s}")
print(f"  West:  {targ.w}")
print(f"  East:  {targ.e}")
print()

print("Checking the links that *used* to come into the target room...")
print(f"  North room, headed South: {n.s}")
print(f"  South room, headed North: {s.n}")
print(f"  West  room, headed East:  {w.e}")
print(f"  East  room, headed West:  {e.w}")
print()



print("Checking a few more links, using the links in the rooms around the target...")
print()

assert n.w.s is w
assert w.s.e is s
assert s.e.n is e
assert e.n.w is n



print("TESTCASE COMPLETED")

