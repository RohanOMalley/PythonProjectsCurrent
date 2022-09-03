"""File: carcassonne_tile.py

   Author: Rohan O'Malley

   Purpose: The purpose of this program is to create a class
   that creates a tile object that has certain spefcific attributes.
   Has 4 directions north, south, east, west. Can have grass, grass+road
   or a city on each side. Also class can tell which roads are connected
   and to each other and what cities are connected.
"""

class CarcassonneTile:
    '''
    Class creates a a Tile object to be used in a 
    game. Tile has North, South, East, West and at each
    direction there can be a city, a road or grass. Those
    cities can be connected as well as the roads.

    Private Fields:
        - north, south, east, west - either 'grass', 'grass+road' or 'city'
        - crossroads - a boolean that determine if there are 4 roads that meet 
        in the middle
        - cities_connect - a dictionary of directions and where they are
        connected
        - road_connect - a dictionary of where the cities are connected
    
    Constructor:
        - builds a tile with all of the directions set to either grass, road
        or city. Then also builds the connection between the cities and the 
        roads within the tile

    Methods:
        - get_edge - passed in a direction and whatever is on that
        side is returned
        - edge_has_road - passsed in a direction to see if that
        side has a road if it does True is returned else False
        - edge_has_city - passed in a direction and that side is
        checked to see if it has a city on it, returns True if
        there is city, False if not
        - has_crossroads - checks the crossroads variable and
        returns the boolean it holds
        - road_get_connection - a side is passed in and whatever
        side that road is connected to is returned
        - city_connects - 2 sides passed in to check what cities
        have connections then
    '''
    def __init__(self, n, e, s, w, crossroads, city_connect, road_connect):
        self._north = n
        self._east = e
        self._south = s
        self._west = w
        self._crossroads = crossroads
        self._cities_connect = city_connect
        self._road_connect = road_connect

    def get_edge (self, side):
        if side == 0:
            return self._north
        elif side == 1:
            return self._east
        elif side == 2:
            return self._south
        elif side == 3:
            return self._west

    def edge_has_road (self,side):
        if side == 0:
            if self._north == 'grass+road':
                return True
            else:
                return False
        elif side == 1:
            if self._east == 'grass+road':
                return True
            else:
                return False
        elif side == 2:
            if self._south == 'grass+road':
                return True
            else:
                return False
        elif side == 3:
            if self._west == 'grass+road':
                return True
            else:
                return False
        else:
            return False
        
    def edge_has_city (self,side):
        if side == 0:
            if self._north == 'city':
                return True
            else:
                return False
        elif side == 1:
            if self._east == 'city':
                return True
            else:
                return False
        elif side == 2:
            if self._south == 'city':
                return True
            else:
                return False
        elif side == 3:
            if self._west == 'city':
                return True
            else:
                return False 
        else:
            return False
    
    def has_crossroads (self):
        if self._crossroads is True:
            return True
        else:
            return False

    def road_get_connection (self, from_side):
        if self._crossroads is True:
            return -1
        # north
        elif from_side == 0:
            return self._road_connect['north']

        # east
        elif from_side == 1:
            return self._road_connect['east']

        # south
        elif from_side == 2:
            return self._road_connect['south']

        # west
        elif from_side == 3:
            return self._road_connect['west']
            
    
    def city_connects (self, sideA, sideB):
        if sideA == sideB:
            return True
        if self._cities_connect is None:
            return False
        # north
        elif sideA == 0:
            if sideB in self._cities_connect['north']:
                return True
            else:
                return False
        # east
        elif sideA == 1:
            if sideB in self._cities_connect['east']:
                return True
            else:
                return False
        # south
        elif sideA == 2:
            if sideB in self._cities_connect['south']:
                return True
            else:
                return False
        # west
        elif sideA == 3:
            if sideB in self._cities_connect['west']:
                return True
            else:
                return False

# 0, 1, 2, 3
# n, e, s, w, crossroads, city_connect, road_connect

tile01 = CarcassonneTile('city', 'grass+road','grass','grass+road',False,\
     {'north':[0]},{'east':3, 'west':1})
tile02 = CarcassonneTile('city','city','grass','city',False,\
     {'north':[1,3],'east':[0,3], 'west':[0,1]}, None)
tile03 = CarcassonneTile('grass+road','grass+road','grass+road','grass+road',\
    True,None, None)
tile04 = CarcassonneTile('city', 'grass+road','grass+road','grass', False,\
     None, {'south':1, 'east': 2})