#! /usr/bin/python3

from utils import compare_sets



data1 = {"asdf", "qwerty", "foobar"}
data2 = {        "qwerty", "foobar", "uiop", 123}
data3 = set(range(124))


print("--- COMPARISON: ---")
print(f"data1 / data2: {compare_sets(data1, data2)}")
print(f"data2 / data1: {compare_sets(data2, data1)}")
print(f"data1 / data3: {compare_sets(data1, data3)}")
print(f"data3 / data1: {compare_sets(data3, data1)}")
print(f"data2 / data3: {compare_sets(data2, data3)}")
print(f"data3 / data2: {compare_sets(data3, data2)}")
print()


print()
print("TESTCASE COMPLETED")


