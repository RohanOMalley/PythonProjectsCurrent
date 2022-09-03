'''
File: swap.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to 
take an input remove the whitespace from
both ends. Then find the midpoint and swap
 the front and back ends and print it out.
If the length is odd then take the
 middle character and swap the front and back ends
but keep the middle character in the middle.
Course: Fall CS 120
'''

first_input = input('Please give a string to swap: ')

# remove whitespace
stripped = first_input.strip()

# find midppoint in input
midpoint = len(stripped)/2

# if the input is even this statement runs
if len(stripped) % 2 == 0:
    midpoint = int(midpoint)
    print(stripped[(midpoint):len(stripped)],end = '')
    print(stripped[0:midpoint])

# if the input is odd this statement runs
elif len(stripped) % .5 == 0:
    midpoint = int(midpoint)
    print(stripped[(midpoint):len(stripped)+1], end='')
    print(stripped[midpoint], end = '')
    print(stripped[0:(midpoint)])