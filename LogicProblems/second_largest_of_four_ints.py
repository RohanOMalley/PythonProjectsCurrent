'''
File: second_largest_of_four_ints.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to take in 4 inouts 
from the user and put them into a list. Then the program will
sort the list and find the number that is second largest
and print it out.
Course: Fall CS 120
'''
# list used to append all of the user's
# inputs
number_list =[]

# loop takes all the inputs and appends
# list
for put in range(4):
    user = int(input())
    number_list.append(user)

sorted_num = sorted(number_list)

# find the second largest
second_largest = len(sorted_num)-2

print(sorted_num[second_largest])