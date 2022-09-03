#! /usr/bin/env python3


import classes_prob3



print("TESTING A 20x20 GRID.  DO THEY ALL HAVE SEPARATE NAMES?")
print()



print("Calling build_grid(20,20)...")
sw_corner = classes_prob3.build_grid(20,20)
print()



print("Collecting all of the rooms into a list...")
print()

rooms = []

left_edge_cur = sw_corner
while left_edge_cur is not None:
    rooms.append(left_edge_cur)
    while rooms[-1].e is not None:
        rooms.append(rooms[-1].e)
    left_edge_cur = left_edge_cur.n



print("Extracting all of the names from the node list, into a set...")
print()

names = set()
for r in rooms:
    my_name = r.get_name()

    if type(my_name) != str:
        print(f"ERROR: The name of one of the rooms is not a string!  name={repr(name)}")
    if my_name == "":
        print(f"ERROR: The name of one of the rooms is an empty string!")

    names.add(my_name)



print("Checking for duplicates.  If there are no duplicates, then the size of the name set should be the same as the room list.")
print(f"  room count: {len(rooms)}")
print(f"  name count: {len(names)}")
print()



print("TESTCASE COMPLETED")

