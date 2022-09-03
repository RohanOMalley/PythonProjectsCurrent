'''
File: twine.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to create a game that
lets the user enter in certain commands to move around a grid. 
The user can move n,s,e or w or back track thier steps. They can
also print out a map of where they have been like unrolling a ball
of twine that shows the path of the user.
Course: Fall CS 120
'''

def read_obstacles (filename):
    '''This function takes in a file name opens it
    and reads it into a list then is formatted into
    a tuple list then returned. Also, certain error
    messages will read if file name or contents in 
    file are not correct.'''
    
    if filename == '-':
        return
    elif filename == '':
        print('ERROR: The file name is blank')
        return
    
    # takes care of EOF for the input file being 
    # hooked up
    try:
        file = open(filename, 'r').readlines()
    except FileNotFoundError:
        print('ERROR: Obstacle File is not Found')
    
    # loop to turn obstacle file into
    # a tuple list also checks to see
    # if contents are valid
    tup_list = []
    try:
        for line in file:
            line = line.strip().split()
            int_list = []
            for ele in line:
                int_list.append(int(ele))
            tup_list.append(tuple((int_list[0],int_list[1])))
        return tup_list
    except:
        print('ERROR: The obstacle file has invalid contents')


def move_around (direction, cur_position):
    '''This function is to move the previous
    position to new position given by the user.
    The direction is n,s,w,e given by user. The
    cur_position is the previous position that
    is being changed in the function.'''
    if direction == 'n':
        new_y = cur_position[1] + 1
        x = cur_position[0]
        new_position = tuple((x, new_y))
        return new_position

    elif direction == 's':
        new_y = cur_position[1] - 1
        x = cur_position[0]
        new_position = tuple((x, new_y))
        return new_position 

    elif direction == 'e':
        y = cur_position[1]
        new_x = cur_position[0] + 1
        new_position = tuple((new_x, y))
        return new_position

    elif direction == 'w':
        y = cur_position[1]
        new_x = cur_position[0] - 1
        new_position = tuple((new_x, y))
        return new_position

def invalid_commands (command):
    '''This function tests if the command
    given by the user is formatted right.
    If the format is wrong an error message
    will print out.'''
    if ' ' in command:
        print('ERROR: Enter only one word in the command line')
    elif command == '':
        print('You do nothing.')
    else:
        print('ERROR: Command is not recongized')

def crossings (cur_position, history):
    '''This function takes in the cur_position
    and looks through the history and then
    prints out how many times the cur_position
    appears in the history.'''
    pos_count = 0
    for i in range(len(history)):
        if history[i] == cur_position:
            pos_count += 1
    print(f'There have been {pos_count} times in the history\
        when you were at this point.')

def map (history, obtup):
    '''This function takes in the history and
    loops through and prints out a map of the path
    of the user. Certain symbols will print out 
    for the history, obstacles and origin.'''
    y = 5
    # loop goes through a x and y 
    # variables and checks each coordinate
    # to see if something needs to be printed
    print('+-----------+')
    while y != -6:
        x = -5
        print('|', end = '')
        while x != 6:
            cur = tuple((x,y))
            if cur == history[-1]:
                print('+',end = '')
            elif cur in obtup:
                print('X', end = '')
            elif cur == (0,0):
                print('*', end = '')
            elif cur in history:
                print('.',end = '')
            else:
                print(' ',end = '')
            x += 1
        print('|')
        y -= 1
    print('+-----------+')

def ranges (history):
    '''This function loops through the history and
    counts up the greatest length the twine goes
    in each direction then prints out each count.'''
    north_count = 0 
    south_count = 0
    east_count = 0
    west_count = 0
    # loop checks each tuple in history
    # and keeps the greatest number in 
    # each direction
    for tup in history:
        if tup[0] > 0:
            if east_count <= tup[0]:
                east_count = tup[0]

        elif tup[0] < 0:
            if west_count >= tup[0]:
                west_count = tup[0]

        if tup[1] > 0:
            if north_count <= tup[1]:
                north_count = tup[1]
        
        elif tup[1] < 0:
            if south_count >= tup[1]:
                south_count = tup[1]
    
    print(f'The furthest West your twine goes is {west_count}')
    print(f'The furthest East your twine goes is {east_count}')
    print(f'The furthest South your twine goes is {south_count}')
    print(f'The furthest North your twine goes is {north_count}')
        

def main():
    print('Please give the name of the obstacles filename, or - for none:')
    obstacle_file = input()
    ob_tup = read_obstacles(obstacle_file)
    # setting variables
    history = [(0,0)]
    i = 0
    nsew = ['n','s','e','w']

    # loop asks the user for command
    # until the file hooked up runs out
    # of inputs
    while True:
        cur_position = history[i]

        print(f'Current position: {history[i]}')
        print(f'Your history:     {history}')
        print(f'What is your next command?')

        try:
            command = input()
        except EOFError :
            break

        if command in nsew:
            if ob_tup != None:
                new = move_around(command, history[i])
                if new in ob_tup:
                    print('You could not move in that direction,\
                        because there is an obstacle in the way.')
                    print('You stay where you are.')
                    continue
                else:
                    history.append(new)
                    i += 1
            else:
                new = move_around(command, history[i])
                history.append(new)
                i += 1

        elif command == 'back':
            if len(history) <= 1:
                print("Cannot move back, as you're at the start!")
                i = 0
            else:
                yuh = history.pop()
                print('You retrace your steps by one space')
                i -= 1
        
        elif command == 'crossings':
            crossings(cur_position,history)

        elif command == 'map':
            map(history, ob_tup)

        elif command == 'ranges':
            ranges(history)
        
        else:
            invalid_commands(command)
        
        print()

main()