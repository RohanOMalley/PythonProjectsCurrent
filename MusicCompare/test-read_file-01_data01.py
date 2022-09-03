#! /usr/bin/python3

from utils import read_file



filename = input('file:')
print(f"INPUT FILE: {filename}")
print()


songs = read_file(open(filename))
for s in songs:
    print(s)


print()
print("TESTCASE COMPLETED")


