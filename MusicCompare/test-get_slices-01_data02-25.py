#! /usr/bin/python3

from utils import read_file, get_slices



filename = "/Users/rohanomalley/Documents/CSC 120/Project 2 Long/data02.txt"
n        = 25

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


