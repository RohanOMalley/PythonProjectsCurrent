#! /usr/bin/python3

from utils import *



filename = "data03.txt"
n        = 4

print(f"INPUT FILE: {filename}")
print(f"N:          {n}")
print()


songs = read_file(open(filename))


print("--- COMPARING: first song to the last one ---")
song1 = songs[0]
song2 = songs[-1]

print(f"id_a = {song1[0]}")
print(f"id_a = {song2[0]}")
print()

print(f"comparison: {compare_melodies(song1[2], song2[2], n)}")


print()
print("TESTCASE COMPLETED")


