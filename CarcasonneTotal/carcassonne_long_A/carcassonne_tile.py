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
        '''
        Function takes in a side
        and returns whatever object
        is on that side

        Params:
            - side - a direction in form of
            integer, 0, 1, 2, 3
        
        Returns:
            - the side of the tile passed in
            and what is on that side will be
            either: 'grass+road', 'city' or
            'grass'
        '''
        if side == 0:
            return self._north
        elif side == 1:
            return self._east
        elif side == 2:
            return self._south
        elif side == 3:
            return self._west

    def edge_has_road (self,side):
        '''
        Function takes in a side then
        looks to see if a road is on that
        side and returns True or False based
        on if there is a road there or not

        Params:
            - side- an integer that determines
            what side to look at: 0,1,2,3

        Returns:
            - True- if road is at side
            - False - if road is not at side
        '''
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
        '''
        Function takes in a side then
        looks to see if a city is on that
        side and returns True or False based
        on if there is a city there or not

        Params:
            - side- an integer that determines
            what side to look at: 0,1,2,3

        Returns:
            - True- if city is at side
            - False - if city is not at side
        '''
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
        '''
        Function checks to see if there
        are a crossroads in the tile, if so
        then True is returned if not False
        is returned

        Returns:
            - True - if self._crossroads is True
            - False - if self._crossroads is False
        '''
        if self._crossroads is True:
            return True
        else:
            return False

    def road_get_connection (self, from_side):
        '''
        Function takes in a side and checks to 
        see where that road is connected to and
        returns wherever that side was connected
        as a direction

        Params:
            - from_side - an integer that shows
            what road is connected to
        
        Returns:
            - returns side that passed in side
            is connected to
        '''
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
        '''
        Function checks to see if two cities
        are connected. Then it returns True
        if the cities are connected at those
        directions

        Params:
            - sideA, sideB - an integer that 
            is a direction as a side: 0,1,2,3
        
        Returns:
            - True - if both of the sides passed in
            connect
            - False - if the sides passed in do not
            connect
        '''
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
    
    def rotate(self):
        '''
        Function takes the current tile and rotates
        it 90 degress clockwise. All sides of the tile
        move over one direction. Then a new tile is created
        with all of the new sides and connections

        Returns:
            - New Tile with all of the new sides and
            directions after being rotated 90 degrees
        '''
        new_e = self._north 
        new_s = self._east
        new_w = self._south
        new_n = self._west

        if self._cities_connect is None:
            new_city_connect = None
        else:
            new_city_connect = {}
            for key in self._cities_connect:
                new_vals = []
                for num in self._cities_connect[key]:
                    if num == 3:
                        new_vals.append(0)
                    else:
                        new_vals.append(num + 1)
                if key == 'north':
                    new_city_connect['east'] = new_vals
                elif key == 'east':
                    new_city_connect['south'] = new_vals
                elif key == 'south':
                    new_city_connect['west'] = new_vals
                elif key == 'west':
                    new_city_connect['north'] = new_vals
        
        if self._road_connect is None:
            new_road_connect = None
        else:
            new_road_connect = {}
            for key in self._road_connect:
                direct = self._road_connect[key]
                if direct == 3:
                    new_direct = 0
                else:
                    new_direct = direct + 1
                if key == 'north':                   
                    new_road_connect['east'] = new_direct
                elif key == 'east':
                    new_road_connect['south'] = new_direct
                elif key == 'south':
                    new_road_connect['west'] = new_direct
                elif key == 'west':
                    new_road_connect['north'] = new_direct              
            
        return CarcassonneTile(new_n,new_e,new_s,new_w,self._crossroads,\
            new_city_connect,new_road_connect)


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

tile05 = CarcassonneTile('city','city','city','city', False,\
     {'north':[1,2,3], 'south':[0,1,3],'east':[0,2,3],'west':[0,1,2]}, None)

tile06 = CarcassonneTile('grass+road','grass','grass+road','grass',False,\
    None, {'north':2,'south':0} )

tile07 = CarcassonneTile('grass', 'city', 'grass','city',False, None, None)

tile08 = CarcassonneTile('grass', 'city', 'grass', 'city', False,\
    {'east':[3],'west':[1]}, None)

tile09 = CarcassonneTile('city','city','grass','grass',False,\
    {'north':[1],'east':[0]}, None)

tile10 = CarcassonneTile('grass','grass+road','grass+road','grass+road',True,\
    None, {'west':1,'east':3,'south':1})
    # might need to add a list to the road connect ^^^^^

tile11 = CarcassonneTile('city','grass+road','grass+road','city',False,\
    {'north':[3],'west':[0]}, {'south':1,'east':2})

tile12 = CarcassonneTile('city','grass','grass+road','grass+road',False,\
    None,{'west':2,'south':3})


