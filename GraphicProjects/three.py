###
### Author : Rohan O'Malley
### Course : CSC 110
### Description : Program prints out 3 shapes. A square, a circle, and a triangle.
### All shapes move across in sync and when they wrap around to the begining their
### y coordinate is randomized. The loop continues forever.

from graphics import graphics
import random

def main ():

    gui = graphics(700, 700, 'three')
    x_coord = -50

    while True :
        gui.clear()
        if x_coord == -50 :
            y_coord_rec = random.randint(50, 650)
            y_coord_tri = random.randint (50, 650)
            y_coord_circle = random.randint (50, 650)

        gui.rectangle(x_coord-25,y_coord_rec, 50, 50,'blue')
        gui.triangle (x_coord,y_coord_tri,(x_coord-25),(y_coord_tri+45),(x_coord+25),\
        (y_coord_tri+45), 'orange')
        gui.ellipse (x_coord, y_coord_circle, 50, 50,'red')
        x_coord += 5
        if x_coord == 750:
            x_coord = -50
        gui.update_frame(45)


main ()