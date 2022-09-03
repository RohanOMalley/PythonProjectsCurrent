""" File: classes_prob3.py
    Author: Sebastian Magri
    Purpose: A program that contains a room class that is implemented with
             a maze
    Course: CSC 120 Semester 2
"""


class Room:
    """
    Represents a single room with a name and and 4 possible exits (n,s,e,w)

    Constuction:
        Name param needed, but fields of self.e, self.w, self.n,
        and self.s set to None

    Methods:
        get_name(self): Get name of a room
        set_name(self, name): Change name of a room obj

        collapse_room(self): Collapse room so all exits point to None as
                             well as entrances from other rooms are bloked
    """

    def __init__(self, name):

        self._name = name
        self.e = None
        self.w = None
        self.n = None
        self.s = None

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name

    def get_name(self):
        """
        Get the name of a room obj
        Returns: {str} name of obj
        """

        return self._name

    def set_name(self, new_name):
        """
        Change the name of existing obj
        Args:
            new_name: {str} name to change for room

        Returns: None
        """

        self._name = new_name

    def collapse_room(self):
        """
        Collapses all entrances and exits to a room
        Returns: None
        """

        if self.e is not None:
            self.e.w = None
            self.e = None

        if self.w is not None:
            self.w.e = None
            self.w = None

        if self.n is not None:
            self.n.s = None
            self.n = None

        if self.s is not None:
            self.s.n = None
            self.s = None





def build_grid(wid, hei):
    """
    Build a 2D array of room objs and link those objects together in the
    appropriate way
    Args:
        wid: {int} width of the grid
        hei: {int} height of the grid

    Returns: sw_corner {linked list} with head at sw_corner
    """


    def right_middle(grid, x, y):
        """Link grid on right middle boundary"""
        grid[x][y].n = grid[x][y+1]
        grid[x][y+1].s = grid[x][y]

    def top_links(grid, x, y):
        """Links top of grid to each other"""
        grid[x][y].e = grid[x+1][y]
        grid[x+1][y].w = grid[x][y]

    def general(grid, x, y):
        """Link Rooms not at top or far east side"""
        grid[x][y].e = grid[x+1][y]
        grid[x+1][y].w = grid[x][y]
        grid[x][y].n = grid[x][y+1]
        grid[x][y+1].s = grid[x][y]




    grid = []
    for x in range(wid):
        column = []

        for y in range(hei):

            name = 'room_' + str(x) + '_'+ str(y)
            cls = Room(name)
            column.append(cls)

        grid.append(column)

    y = 0
    print(len(grid)-1)
    print(len(grid[0])-1)

    while y < len(grid[0]):

        x = 0

        while x < len(grid):

            if x == len(grid)-1 and y == len(grid[0])-1:
                pass  # NE corner already linked
            elif x == len(grid)-1:
                right_middle(grid, x, y)
            elif y == len(grid[0])-1:
                top_links(grid, x, y)
            else:
                general(grid, x, y)

            x += 1

        y += 1

    return grid[0][0]


rooms = build_grid(5,5)
