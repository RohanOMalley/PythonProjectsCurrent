
'''
File: classes_prob3.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to create a Room class
that makes a dungeon like room that can link to other rooms. Then,
in build_grid a grid of these rooms are built using the Room class
then in another loop all the rooms are then linked together.
Course: Fall CS 120
'''

class Room:
    '''
    Class builds a singular room with exits on n,s,e,w sides

    Constructor:
        - builds each direction self.n,self.s,self.e,self.w
          and sets to none, also sets name to param passed in
          from user

    Methods:
        - get_name(self) - returns name of room
        - set_name(self, name) - changes name of current room  
    '''
    def __init__(self,name):
        self.name = name
        self.n = None
        self.s = None
        self.w = None
        self.e = None

    def get_name (self):
        '''
        Function returns current name of room
        '''
        return self.name
        
    def set_name (self, name):
        '''Function changes the name of the
        current room and returns it
        Params:
            - name - name to make the room'''
        self.name = name

    def collapse_room (self):
        '''
        Funciton takes all exits and the surrounding
        rooms and sets them to None, making that room
        impossible to get to
        '''
        if self.n is not None:
            self.n.s = None
            self.n = None
        if self.s is not None:
            self.s.n = None
            self.s = None
        if self.e is not None:
            self.e.w = None
            self.e = None
        if self.w is not None:
            self.w.e = None
            self.w = None


def build_grid (wid, hei):
    '''
    Function builds a grid of rooms using the Room class
    Params:
        - wid - is a integer saying how wide the grid should be
        - hei - is an intger saying how tall grid should be
    Returns:
        - returns the first room in the grid at [0][0]
    '''
    grid = []
    # builds all the rooms
    for x in range(wid):
        column = []
        for y in range(hei):
            current_room = (f'room{str(x)},{str(y)}')
            column.append(Room(current_room))
        grid.append(column)
    
    m_grid = len(grid) - 1
    mg_grid = len(grid[0]) - 1

    for y in range(len(grid[0])):
        for x in range(len(grid)):
            # for the northeast corner since alreadly linked
            if x == m_grid and y == mg_grid:
                trash = 0
            # for every room at the top of the grid
            elif y == mg_grid:
                grid[x][y].e = grid[x+1][y]
                grid[x+1][y].w = grid[x][y]
            # for every room on the right side of grid
            elif x == m_grid:
                grid[x][y].n = grid[x][y+1]
                grid[x][y+1].s = grid[x][y]
            # for all other rooms
            else:
                grid[x][y].e = grid[x+1][y]
                grid[x+1][y].w = grid[x][y]
                grid[x][y].n = grid[x][y+1]
                grid[x][y+1].s = grid[x][y]

    return grid[0][0]
