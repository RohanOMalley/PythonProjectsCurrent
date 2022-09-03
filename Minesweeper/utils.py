###
### File: utils.py
### Author: Rohan O'Malley
###
### Description: This program is attached with the minesweeper file. It goes through a game
### of minesweeper by checking each spot on the board if there is a mine there. Also, checks
### how many mines are nearby a players spot that they choose. Also takes in an file and reads it
### into a list to be used as the game board with all the locations of the mines. There is a function
### included that prints out the grid.

# Changes to this file should only be inside function definitions

def find_mine(grid, x, y, position):
    '''
    Determines if a square from a relative position contains a mine.
    Returns 1 if there is, otherwise returns 0.

    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                either the number of adjacent X's or 0.
    x:          Integer which is the x postiion to be scanned for mines.
    y:          Integer which is the y postiion to be scanned for mines.
    position:        A tuple containing the relative coordinates to scan

    Examples:
    grid = [["X", 0],
            [0, "0"]]

    find_mine(grid, 0, 0, (0, 0)))    Returns: 1
    find_mine(grid, 0, 0, (1, 0)))    Returns: 0
    find_mine(grid, 0, 0, (0, 1)))    Returns: 1
    find_mine(grid, 0, 0, (1, 1)))    Returns: 0
    find_mine(grid, 0, 0, (20, 20)))  Returns: 0
    '''

    pos_x = x + position[0]
    pos_y = y + position[1]

    if pos_x < 0 or pos_x > len(grid[0])-1 or pos_y < 0 or pos_y > len(grid)-1:
        return 0

    if grid[pos_y][pos_x] == 'X':
        return 1
    else:
        return 0



def count_total_moves(grid):
    '''
    Counts the number of moves that need to be made for the player to
    win the game. (Counts number of squares that are not mines)

    Parameter:
    grid:       2D list containing X's representing mines and numbers which are
                the number of adjacent X's.
    '''
    count = 0
    # loop finds how many spots
    # are left on the board
    for row in grid:
        for col in row:
            if col != 'X':
                count += 1
    return count


def determine_game_status(grid, count):
    '''
    Returns a boolean which is True if the game should continue or
    False if the game is over. False is returned if a mine has been
    revealed or count is 0 meaning there are no squares without mines
    that are not revealed.
    Parameter:
    grid:       2D list containing X's representing mines and numbers which are
                the number of adjacent X's.
    count:      Integer which is the number of mineless squares left to be revealed.
    '''

    if count <= 0:
        return False
    # loop finds out if the user
    # has stepped on a mine, which
    # ends the game
    for row in grid:
        for col in row:
            if col == 'X':
                return False
    else:
        return True

def dig(grid, coordinate, user_view):
    '''
    Translates an item at a coordinate on the grid to the correspoinding
    location on the user_view.

    Parameters:
    grid:       2D list containing X's representing mines and numbers which are
                the number of adjacent X's.
    coordinate: A string where the first character is the x-position and the
                characters that follow makes up the y-position for where to dig.
                NOTE: The x-position is a letter and the y-position is a number.
    user_view:  2D list containing X's representing mines and numbers which are
                either the number of adjacent X's or 0. Unlike grid, some of the
                values are empty meaning the user has not seen the square.
    '''

    # dictionary to reference for grid points
    alpha = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,\
            'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

    col = alpha[coordinate[0]]
    row = (len(grid)-1) - int(coordinate[1])
    # sets the spot on the grid to the new
    # spot on the users view
    new_spot = grid[row][col]

    user_view[row][col] = new_spot





def update_grid(grid):
    '''
    Populates non-mine squares with the number of adjacent mines.
    Basically, iterate through the grid and replace the ' ' strings with
    a string with a number in it, representing how many mines
    neighbor this location.
    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                either the number of adjacent X's or 0.
    '''
    position_list = [(1,1),(-1,-1),(-1,0),(1,0),(0,1),(0,-1),(-1,1),(1,-1)]

    # loop goes through each row in grid
    for j in range(len(grid)):
        # loop goes through each number in length
        # of grid row, and checks if it is a bomb
        for i in range(0,len(grid[0])):
            if grid[j][i] != 'X':
                count = 0
                # loop goes through each postion in the position list
                # and looks to see if a mine is near the users spot
                # that they chose
                for post in position_list:
                    count += find_mine(grid,i,j,post)
                grid[j][i] = str(count)




def print_grid(grid):
    '''
    Prints out a 2D grid with the y-axis labeled with numbers and the x-axis with letters.

    Parameters:
    grid:       2D list containing X's representing bombs and numbers which are
                the number of adjacent X's.
    '''
    i = len(grid)-1
    alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l',\
                'm','n','o','p','q','r','s','t','u','v','w','y','z']
    # loop prints out each row and col in
    # the grid with newlines placed where
    # they needed
    for row in grid:
        print('', str(i),end = ' ')
        for j in range(len(row)):
            if j < len(row)-1:
                print('['+str(row[j])+']',end = '')
            else:
                print('['+str(row[j])+']',end = '\n')
        i -= 1
    print('    ',end = '')
    # loop prints out the alphabet for the col
    # identification
    for i in range(len(grid[0])):
        if i < len(grid[0])-1:
            print(alpha_list[i], end ='  ')
        else:
            print(alpha_list[i], end ='\n')


def make_empty_clone(grid):
    '''
    Returns a 2D list which is the same dimensions (rows / columns) as a passed in grid.
    The returned list should contain ' ' strings only
    '''
    empty_grid = []

    # loop makes and empty grid for the user view
    for row in grid:
        empty_row = []
        for col in row:
            empty_row.append(' ')
        empty_grid.append(empty_row)
    return empty_grid