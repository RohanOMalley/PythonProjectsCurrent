'''
File: population.py
Author: Rohan O'Malley
Purpose: The purpose of this program is
 to read a file and set up a dictionary
by looping through the file and format
 the lines to be ordered into a dicitonary.
Then print out each step of sorting
 the dicitonary, putting each pair into tuples,
sorting the tuples. Then prints out the
 actual output of the sorted pairs.
Course: Fall CS 120
'''

file_name = input('File to scan:')
file_name = file_name.strip()

file = open(file_name,'r')
line_list = file.readlines()

diction = {}
trash = []
new_list = []

# loop formats each line into a pair and gets rid of
# the whitespace and the newline character.
for line in line_list:
    if line[0] != '\\':
        if '\t' in line:
            line = line.strip('\n').split('\t')
        else:
            line = line.strip('\n').split(' ')
        hold_list = []
        # sets up each pair to be put in the 
        # new_list that is formatted correctly
        for item in line:
            item = item.strip('\t')
            if item == '' or item == ' ':
                trash.append(3)
            else:
                hold_list.append(item)
        if len(hold_list) > 1:
            new_list.append(hold_list)

# loop sets up dictionary with word to value
# pair and sums up  dupilcates with different
# values
for line in new_list:
    if line[0] == '\n' or line[0] == '':
        trash.append('3')
    elif line[0] not in diction:
        diction[line[0]] = int(line[1])
    elif line[0] in diction:
        diction[line[0]] += int(line[1])

# prints out a sorted alphabetically dictionary 
print('STEP 1: THE ORIGINAL DICTIONARY')
for key, value in sorted(diction.items()):
    print('Key:',key, 'Value:', value)
print('\n')

tuple_list = []
# prints out an unsorted tuple
print('STEP 2: A LIST OF VALUE->KEY TUPLES')
for key, value in sorted(diction.items()):
    tuple_list.append(tuple((value,key)))

print(tuple_list)
print('\n')

tuple_list = sorted(tuple_list)
# prints out a sorted tuple
print('STEP 3: AFTER SORTING')
print(tuple_list)
print('\n')

# prints out each key value pair
print('STEP 4: THE ACTUAL OUTPUT')
for pair in tuple_list:
    print(pair[1],pair[0])
print('\n')




