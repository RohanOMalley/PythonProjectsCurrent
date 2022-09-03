'''
File: indentation_print.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to read lines of input and
count up the leading whitespaces of the input, then print it out after.
The user then has the option to type in "quit" to stop the loop
and end the program.
Course: Fall CS 120
'''
# used to skip over useless lines
trash = []

# loop goes through inputs until 
# user types quit
while True:
    user = input()
    # variable holds the count for leading whitespaces
    space_count = 0
    if user.strip() == 'quit':
        break
    elif user == '\n' or user == '' or user == '\t':
        trash.append(4)
    elif user[0] == ' ':
        # loop counts spaces in the input
        for space in user:
            if space == ' ':
                space_count += 1
            else:
                break
    print(space_count)
