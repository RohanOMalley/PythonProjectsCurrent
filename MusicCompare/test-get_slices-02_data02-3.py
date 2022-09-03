#! /usr/bin/python3

from utils import *



filename = "data02.txt"
n        = 3

print(f"INPUT FILE: {filename}")
print(f"N:          {n}")
print()


songs = read_file(open(filename))


for s in songs:
    print(f"--- SLICES FROM id={s[0]}")
    print(get_slices(s[2], n))
    print()


print()
print("TESTCASE COMPLETED")


