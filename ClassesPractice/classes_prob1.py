'''
File: classes_prob1.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to create a few
different classes. Simplest just initializes 3 variables
as a, b, c. Rotate class takes in 3 variables and rotates
the variables for which position they are in order. Then 
user can ask to see the first, second or third object. 
Band class creates a band with members and a list of
guitar players. User can add or fire guitar players, 
change drummers and singers. Then they will play music
based on the inputs.
Course: Fall CS 120
'''

import copy

class Simplest:
    '''
    This class takes in 3 varuiables and initializes them,
    Pub fields:
        - a, some object
        - b, some object
        - c, some object
    '''
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

class Rotate:
    '''
    Class takes in 3 variables noted by first, second and third,
    then can rotate the order of the variables so when called they
    move spots.
    Private fields:
        - first, given by user
        - second, given by user
        - third, given by user
    Constructor:
        - Builds those variable given by user
    Methods:
        - get_first(self) - returns what the value of the first variable
        - get_second(self) - returns what the value of the second variable
        - get_third(self) - returns what the value of the third variable
        - rotate(self) - holds temp variables for the third and second
         variables then swaps the references for each variable by one
         position
    
    '''
    def __init__(self, first, second, third):
        self._first = first
        self._second = second
        self._third = third
    def get_first(self):
        '''
        Funciton returns first value
        '''
        return self._first

    def get_second(self):
        '''
        Function returns second value
        '''
        return self._second

    def get_third (self):
        '''
        Funciton returns third value
        '''
        return self._third

    def rotate(self):
        '''
        Function takes the first value and
        sets it to the third, sets second value
        equal to first and thrid value is equal
        to second value. Movin up every value by one
        position
        '''
        temp = self._third
        self._third = self._first
        temp2 = self._second
        self._second = temp
        self._first = temp2
        return self._first, self._second, self._third

class Band:
    '''
    Class creates a band with a singer, drummer and however many 
    guitar playes user wants can also fire all guitar players. Then 
    certain messages will print out when music is played.

    Constructor:
        - builds a singer, drummer and guitar player list
          guitar player list will be able to be added to
    Methods:
        - get_singer - returns the current name of singer
        - get_drummer - returns current name of drummer
        - set_singer - changes who singer is
        - set_drummer - changes who drummer is
    '''
    def __init__(self, singer):
        self._singer = singer
        self._drummer = None
        self._guitar = []

    def get_singer (self):
        '''
        Function returns name of  current singer
        '''
        return self._singer

    def set_singer(self, new_singer):
        '''
        Function sets singer to a new name
        then returns it
        Params:
            - new_singer - name of singer to change to
        '''
        self._singer = new_singer
        return self._singer

    def get_drummer (self):
        '''
        Function just returns current drummer name
        '''
        return self._drummer

    def set_drummer (self, new_drummer):
        '''
        Function sets the drummer to a new name given
        by user and returns it
        Params:
            - new_drummer- name of drummer to set
        '''
        self._drummer = new_drummer
        return self._drummer

    def add_guitar_player (self, new_guitar_player):
        '''Function adds a new guitar player to the
        guitar player list based on input from user 
        then returns it
        Param:
            - new_guitar_player - name of guitar player to add'''
        self._guitar.append(new_guitar_player)
        arr = self._guitar.copy()

    def fire_all_guitar_players (self):
        '''
        Function sets guitar player list to
        empty and returns it
        '''
        self._guitar = []
        return self._guitar

    def get_guitar_players (self):
        '''
        Makes a copy of the guitar player list and
        returns it
        '''
        arr = self._guitar.copy()
        return arr
    
    def play_music (self):
        '''
        Function prints out a series of lines
        based on what the names of the band
        members are
        '''
        if self._singer == 'Frank Sinatra':
            print('Do be do be do')
        elif self._singer == 'Kurt Cobain':
            print('bargle nawdle zouss')
        else:
            print('La la la')
        
        if self._drummer is None:
            trash = 0
        else:
            print('Bang bang bang!')
        
        # am I allowed to use len
        if len(self._guitar) > 0:
            for val in self._guitar:
                print('Strum!')

