'''
File: population.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to read
 a file with states and populations and
prints out the state with its population labeled
 below it one by one. The program will
ignore blank lines and lines that
 are comments. At the end of the program the total number
of states found and the total population 
number which is the sum of all the populations.
Course: Fall CS 120
'''

file_name = input('file: ')
file_name = file_name.strip()

line_list = open(file_name).readlines()
trash = []

population_list = []
state_list = []


# loop runs through each line and formats it
# to be printed at the end of the loop.
# Also skips over comments and blank lines.
for line in line_list:
    # if statements take care of lines to ignore
    if line[0] == '\n':
        trash.append(4)
        line = line.strip('\n')
    elif line[0] == '#':
        trash.append(4)
    elif line[0] == '\n':
        trash.append(4)
    else:
        if '\t' in line:
            line = line.strip().split('\t')
        else:
            line = line.strip().split(' ')
        state_string = ''
        # loop puts each word into a list for the 
        # population and the state list.
        for word in line:
            if word.isnumeric() == False:
                state_string += (word + ' ')
            elif word.isnumeric() == True:
                population_num = int(word)
                population_list.append(population_num)
        state_list.append(state_string)
        # prints out each state and population
        # one by one
        print('State/Territory:', state_string)
        print('Population: ',population_num)
        print('\n')

print('# of States/Territories:',len(state_list))
print('Total Population:',sum(population_list))

