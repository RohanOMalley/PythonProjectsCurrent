"""File: carcassonne_map.py

   Author: Rohan O'Malley

   Course: CSC 120

   Purpose: The purpose of this program is to help create
   the map of all the carcassonne tiles. It can add tiles
   to the map and check to make sure that the tile is added
   in the correct place. Program also finds all the border
   positons of the current map and returns them as a set.
"""
from carcassonne_tile import tile01

class CarcassonneMap:
    '''
    Class purpose is to create the map of carcassonne tiles
    and make sure they are added in the correct spot. Can
    also find border spots, check to see if tiles are already
    in dicitonary and check to see if a tile can be added
    without actually adding it

    Private Fields:
        - _tile_dict - a dictionary of all the coordinates
        mapped to a ceratin tile on the grid
    
    Constructor:
        - builds the tile dictionary of all the tiles,
        the first tile being at (0,0)
    
    Methods:
        - get_all_coords - returns a set of all the
        coordinates 
        - find_map_border - returns set of all the border
        coordinates of the current map
        - get - checks to see if (x,y) passed in
        is in the current tile dictionary
        - add - adds a tile to the current tile dictionary
        and can also just check to see if its able to be added
        to the dictionary 
    '''
    def __init__(self):
        self._tile_dict = {(0,0):tile01}

    def get_all_coords (self):
        '''
        Function returns all the keys of the
        tile dicitonary which are tuples of
        x, y coordinates of tiles

        Returns:
            - set of tuples that are keys from the 
            tile dictionary
        '''
        return set(self._tile_dict.keys())

    def find_map_border (self):
        '''
        Function loops through the keys in the
        tile dicitonary and looks to see if there
        is not a tile near that current tile, if 
        not then that coordinate without a tile is
        added to a set and returned

        Returns:
            - a set of all the border places where
            a tile can be placed in the form of
            x, y tuples
        '''
        border_set = set()
        for i in self._tile_dict:
            x = i[0]
            y = i[1]
            if ( x + 1 , y ) not in self._tile_dict:
                border_set.add( (x + 1, y))

            if ( x - 1 , y ) not in self._tile_dict:
                border_set.add( (x - 1, y))

            if ( x , y + 1 ) not in self._tile_dict:
                border_set.add( (x , y + 1))

            if ( x , y - 1 ) not in self._tile_dict:
                border_set.add( (x , y - 1))
        return border_set
            

    def get (self, x, y):
        '''
        Function takes in an x and y coordinate
        and checks to see if that coordinate is in
        the current tile dictionary, if it is then
        the tile at the coordinate is returned if
        not then None is returned

        Params:
            - x - an integer representing spot on
             x axis
            - y - an integer representing spot
            on y axis

        Returns:
            - None is there is no coordinate pair
            in tile dictionary
            - returns the tile object if the pair
            is in the tile dictionary
        '''
        check = (x,y)
        if check not in self._tile_dict:
            return None
        else:
            return self._tile_dict[check]

    def add (self, x, y, tile, confirm=True, tryOnly=False):
        '''
        Function looks to see if the tile passed in
        can be placed at the x, y coordinate pair 
        also passed in. Checks to see if the sides
        match up and will return False if cannot be 
        placed or True if can be placed

        Params:
            - x, y - integers that are coordinates
            - tile - a new tile object
            - confirm=True - if set to False there
            is no need to do checks just set tile
            - tryOnly=False - if set to True then
            all checks done but tile is not added

        Returns:
            - False - if tile cannot be added to 
            tile dictionary
            - True - if tile has been added to
            dictionary
        '''
        north_tile = self.get(x,y + 1)
        south_tile = self.get(x,y - 1)
        east_tile = self.get(x + 1,y)
        west_tile = self.get(x - 1,y)

        if not confirm:
            self._tile_dict[ (x, y) ] = tile
            return True

        if north_tile is None and south_tile is None and\
             east_tile is None and west_tile is None:
            return False
     
        if (x,y) in self._tile_dict:
            return False

        if north_tile is not None:
            if north_tile.get_edge(2) != tile.get_edge(0):
                return False

        if east_tile is not None:
            if east_tile.get_edge(3) != tile.get_edge(1):
                return False
                
        if south_tile is not None:
            if south_tile.get_edge(0) != tile.get_edge(2):
                return False

        if west_tile is not None:
            if west_tile.get_edge(1) != tile.get_edge(3):
                return False
        
        if tryOnly is True:
            return True
        else:
            self._tile_dict[(x,y)] = tile
            return True

    def trace_road_one_direction (self, x, y, side):
        # north
        if side == 0:
            if (x,y + 1) not in self._tile_dict:
                return []
            else:
                next_tile = self._tile_dict[ (x, y + 1)]
                if next_tile._crossroads is True:
                    tup = (x,y + 1,2,-1)
                    return [tup]
                else:
                    south_connect = next_tile._road_connect['south']
                    tup = (x,y + 1,2,south_connect)
                    return [tup] + self.trace_road_one_direction( x, y + 1, south_connect)
        # east
        if side == 1:
            if (x + 1, y) not in self._tile_dict:
                return []
            else:
                next_tile = self._tile_dict[ (x + 1, y)]
                if next_tile._crossroads is True:
                    tup = (x + 1,y, 3,-1)
                    return [tup]
                else:
                    west_connect = next_tile._road_connect['west']
                    tup = (x + 1, y, 3, west_connect)
                    return [tup] + self.trace_road_one_direction( x + 1, y ,west_connect)
        # south
        if side == 2:
            if (x,y - 1) not in self._tile_dict:
                return []
            else:
                next_tile = self._tile_dict[ (x, y - 1)]
                if next_tile._crossroads is True:
                    tup = (x,y - 1, 0, -1)
                    return [tup]
                else:
                    north_connect = next_tile._road_connect['north']
                    tup = (x, y - 1, 0, north_connect)
                    return [tup] + self.trace_road_one_direction( x, y - 1, north_connect)
        # west
        if side == 3:
            if (x - 1, y) not in self._tile_dict:
                return []
            else:
                next_tile = self._tile_dict[ (x - 1, y)]
                if next_tile._crossroads is True:
                    tup = (x - 1, y, 1,-1)
                    return [tup]
                else:
                    east_connect = next_tile._road_connect['east']
                    tup = (x - 1, y, 1, east_connect)
                    return [tup] + self.trace_road_one_direction( x - 1, y, east_connect)

    def trace_road(self, x, y, side):
        '''
        Function takes in x and y coordinated then
        traces the road to the right and the road to
        the left of the coordinate. Then returns a list
        of tuples for all the road connections.

        Params:
            - x and y - integers that are coordinates
            to a tile on map
            -  side - an integer represents a direction
            either: north,east,west,south as 0,1,2,3
        
        Returns:
            - a list of tuples from left to right for
            all the roads connected to the point orginally
            passed in
        '''
        start_tile = self.get(x,y)
        other_side = start_tile.road_get_connection(side)
        back_path = self. trace_road_one_direction(x, y, other_side)

        new_backpath = []
        
        if back_path is None:
            back_path = []
        else:
            for city_tup in back_path:
                new_3 = city_tup[2]
                new_2 = city_tup[3]
                new_tup = (city_tup[0],city_tup[1],new_2,new_3)
                new_backpath.append(new_tup)
        
    
        if new_backpath is None:
            new_backpath = []

        one_direct = self.trace_road_one_direction(x, y, side)
        start = [(x, y , other_side ,side)]
        
        if one_direct == []:
            new_backpath = new_backpath[::-1]
            if new_backpath is None:
                new_backpath = []
            return new_backpath + start
        
        if other_side == -1:
            return start + one_direct
        
        return new_backpath[::-1] + start + one_direct
    
    def trace_city (self, x, y, side):
        '''
        Function takes in an x,y coordinate then
        finds all the cities connected to that point
        passed in. Then returns a tuple telling whether
        the city was complete or not and a set of tuples
        that are locations of all the cities.

        Params:
            - x and y - integers are coordinates to a tile 
            on the map
            -  side - an integer represents a direction
            either: north,east,west,south as 0,1,2,3

        Returns:
            - Tuple with 2 values, a boolean: True if
            city is complete, False: if city is not
            complete. Then a set with all the locations
            of the cities
        '''
        city_set = {(x, y, side)}
        finding_tiles = True
        complete = True

        while finding_tiles is True:

            finding_tiles = False

            for city in list(city_set):
                pass_tile = self._tile_dict[(city[0], city[1])]

                x = city[0]
                y = city[1]
                side = city[2]

                if side == 0:
                    key = 'north'
                elif side == 1:
                    key = 'east'
                elif side == 2:
                    key = 'south'
                elif side == 3:
                    key = 'west'
                
                if pass_tile._cities_connect is not None:
                    if key in pass_tile._cities_connect:

                        city_list = pass_tile._cities_connect[key]

                        for city_dir in city_list:

                            if (x, y, city_dir) not in city_set:
                                city_set.add((x, y, city_dir))
                                finding_tiles = True
                            
                            if city_dir == 0:
                                if (x, y + 1) in self._tile_dict:
                                    north_tile = self._tile_dict[(x, y + 1)]
                                    if north_tile.get_edge(2) == 'city':
                                        if (x, y + 1, 2) not in city_set:
                                            city_set.add((x, y + 1, 2))
                                            finding_tiles = True
                                else:
                                    complete = False
                            
                            elif city_dir == 1:
                                if (x + 1, y) in self._tile_dict:
                                    east_tile = self._tile_dict[(x + 1, y)]
                                    if east_tile.get_edge(3) == 'city':
                                        if (x + 1, y, 3) not in city_set:
                                            city_set.add((x + 1, y, 3))
                                            finding_tiles = True
                                else:
                                    complete = False
                            
                            elif city_dir == 2:
                                if (x, y - 1) in self._tile_dict:
                                    south_tile = self._tile_dict[(x, y - 1)]
                                    if south_tile.get_edge(0) == 'city':
                                        if (x, y - 1, 0) not in city_set:
                                            city_set.add((x, y - 1, 0))
                                            finding_tiles = True
                                else:
                                    complete = False
                            
                            elif city_dir == 3:
                                if (x - 1, y) in self._tile_dict:
                                    west_tile = self._tile_dict[(x - 1, y)]
                                    if west_tile.get_edge(1) == 'city':
                                        if (x - 1, y, 1) not in city_set:
                                            city_set.add((x - 1, y, 1))
                                            finding_tiles = True
                                else:
                                    complete = False
                    else:
                        finding_tiles = False
                else:
                    if side == 0:
                        if (x, y + 1) in self._tile_dict:
                            north_tile = self._tile_dict[(x, y + 1)]
                            if north_tile.get_edge(2) == 'city':
                                if (x, y + 1, 2) not in city_set:
                                    city_set.add((x, y + 1, 2))
                                    finding_tiles = True
                        else:
                            complete = False
                    
                    elif side == 1:
                        if (x + 1, y) in self._tile_dict:
                            east_tile = self._tile_dict[(x + 1, y)]
                            if east_tile.get_edge(3) == 'city':
                                if (x + 1, y, 3) not in city_set:
                                    city_set.add((x + 1, y, 3))
                                    finding_tiles = True
                        else:
                            complete = False
                    
                    elif side == 2:
                        if (x, y - 1) in self._tile_dict:
                            south_tile = self._tile_dict[(x, y - 1)]
                            if south_tile.get_edge(0) == 'city':
                                if (x, y - 1, 0) not in city_set:
                                    city_set.add((x, y - 1, 0))
                                    finding_tiles = True
                        else:
                            complete = False
                    
                    elif side == 3:
                        if (x - 1, y) in self._tile_dict:
                            west_tile = self._tile_dict[(x - 1, y)]
                            if west_tile.get_edge(1) == 'city':
                                if (x - 1, y, 1) not in city_set:
                                    city_set.add((x - 1, y, 1))
                                    finding_tiles = True
                        else:
                            complete = False
                        


        

        return (complete, city_set)
                        

                
                
                        

    
