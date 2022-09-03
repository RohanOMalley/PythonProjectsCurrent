'''
File: classes_prob2.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to create a Color class
that takes in rgb values and converts to hex, can change the colors
based on input from user and can print out values of the rgb when asked.
Also, will remove red when asked.
Course: Fall CS 120
'''

class Color:
    '''
    Class takes in a set of rgb values and initializes them.
    Can turn numbers into a string, translates to hex, returns
    rgb values, can change the rgb values to a certain color if
    asked, can also remove color red.

    Constructor:
        - self.r ,b and g all set by the user input
        ** if inputs greater than 255 they are set to 255
        and if less than 0 values are set to 0
    
    Methods:
        - __str__(self) - rgb values returned as strings
        - html_hex_color(self) - rgb values are formatted into hex
        - get_rgb(self) - rgb values returned
        - set_standard_color(self, name) - can change the rgb values based
                                            on color input from user
        - remove_red(self) - red value is set to 0 and returned.
    '''
    def __init__(self,r ,g, b):
        if r > 255 :
            r = 255
        elif r < 0:
            r = 0
        if g > 255:
            g = 255
        elif g < 0:
            g = 0
        if b > 255:
            b = 255
        elif b < 0:
            b = 0
        self.r = r
        self.g = g
        self.b = b
    def __str__(self):
        '''
        Function turns rgb value into a string and 
        returns it
        '''
        stringed = (f'rgb({self.r},{self.g},{self.b})')
        return stringed
    def html_hex_color(self):
        '''
        Function takes the current rgb values and formats
        them into hex and returns the hex value
        '''
        tup_rgb = ((self.r, self.g, self.b))
        word = '#%02x%02x%02x' % tup_rgb
        word = word.upper()
        return word

    def get_rgb (self):
        '''
        Function returns the current rgb values
        '''
        return ((self.r,self.g,self.b))

    def set_standard_color (self, name):
        '''
        Function takes in a name of a color and based on
        the color the rgb will change to whatever color was
        passed in
        
        Params:
            - name - name of the color to change the
            rgb values to
        Returns:
            - new rgb values
        '''
        name = name.lower()
        if name == 'yellow':
            self.r = 255
            self.g = 255
            self.b = 0
            return self.r, self.g, self.b
        elif name == 'red':
            self.r = 255
            self.g = 0
            self.b = 0
            return self.r, self.g, self.b
        elif name == 'black':
            self.r = 0
            self.g = 0
            self.b = 0 
            return self.r, self.g, self.b
        elif name == 'white':
            # white
            self.r = 255
            self.g = 255
            self.b = 255
            return self.r, self.g, self.b
            
    def remove_red (self):
        '''
        Function take the current r value and
        sets it to 0
        '''
        self.r = 0 
        return self.r

