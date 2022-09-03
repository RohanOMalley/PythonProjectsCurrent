###
### Author: Rohan O'Malley
### Course: CSC 110
### Description: Program aims to print out a mountain scene with a parallax effect.
### Program split into multiple functions. The major parts that move are the Sun,
### Mountains, grass and tree. Also, there is a night and day change with the birds
### that move through the scene and wrap around.

from graphics import graphics
import random

def random_color (gui) :
    # Function is used to generate random colors, uses gui
    # parameter that lets it use colors from graphics module
    red = random.randint (0,255)
    green = random.randint (0,255)
    blue = random.randint (0,255)
    return gui.get_color_string (red, green, blue)

def sun (gui, mouse_x, mouse_y):
    # Function prints out a sun that follows the mouse.
    # The gui parameter is used to be able to draw shapes, the mouse_x
    # and mouse_y parameters are used so that the sun follows the mouse
    # according to the mouses position all from the graphics module.
    mouse_x = mouse_x//600
    mouse_y = mouse_y//600
    sun_in_sky = gui.ellipse (mouse_x+400, mouse_y+50, 70, 70, 'yellow')

def mid_mountain (gui, mid_color, mouse_x, mouse_y) :
    # Function is used to generate the mountain in the middle.
    # The gui parameter is used to draw the mountain. The mid_color
    # parameter is used to give the mountain a different color every
    # the program runs. The mouse_x and mouse_y parameters are so the
    # mountain follows the mouse but slower than the other mountains
    # since it is far away to create the parallax effect.
    mouse_x = mouse_x // 200
    mouse_y = mouse_y // 300
    gui.triangle (mouse_x + 300, mouse_y + 200, mouse_x+125, mouse_y+550, mouse_x + 450,mouse_y +550, mid_color)

def left_mountain (gui, left_color,mouse_x, mouse_y) :
    # Function is used to print out the left mountain. Gui
    # is used to draw the triangle shape, left_color is used to generate a
    # random color for the left mountain every time the program runs.
    # Mouse_x and mouse_y parameters are used to let the mountain follow my mouse
    # to create parallax effect.
    mouse_x = mouse_x // 40
    mouse_y = mouse_y // 200
    left_triangle = gui.triangle (mouse_x+175,mouse_y+235, mouse_x-75, mouse_y + 550, mouse_x+300, mouse_y+550, left_color)

def right_mountain (gui, right_color, mouse_x, mouse_y) :
    # Function is used to print out the right mountain. Gui
    # is used to draw the triangle shape, right_color is used to generate a
    # random color for the right mountain every time the program runs.
    # Mouse_x and mouse_y parameters are used to let the mountain follow my mouse
    # to create parallax effect.
    mouse_x = mouse_x // 40
    mouse_y = mouse_y // 200
    right_triangle = gui.triangle (mouse_x + 420, mouse_y + 240, mouse_x+225, mouse_y + 550, mouse_x + 650, mouse_y + 550, right_color)

def grass_and_blades (gui, mouse_x, mouse_y) :
    # Function is used to print out the grass and grass blades
    # under the mountain. The gui parameter is used to draw the rectangles used
    # for grass and each blade. The mouse_x and mouse_y parameters are used to create
    # parallax effect when they follow my mouse.

    x_coord = -50
    mouse_x = mouse_x // 10
    mouse_y = mouse_y // 10
    grass = gui.rectangle (mouse_x-100, mouse_y+480, 900, 400, 'light green')

    # loop used to print each blade of grass across the screen

    while x_coord < 650 :
        blades = gui.rectangle (mouse_x+ x_coord, mouse_y + 470, 2, 12,'green')
        x_coord += 4


def tree (gui, mouse_x, mouse_y) :
    # Function used to print out the tree that sits on the grass
    # It uses the gui function to print out the rectangle for the body
    # and ellipse for the leaves. The mouse_x and mouse_y are used so the tree
    # will follow my mouse to create the parallax effect.
    mouse_x = mouse_x // 10
    mouse_y = mouse_y // 10
    gui.rectangle (mouse_x+408,mouse_y+470,35,70,'brown')
    gui.ellipse (mouse_x+425,mouse_y+450, 60,80, 'green')

def birds (gui, x_coord_1) :
    # Function used to print out the moving birds across the screen.
    # Gui is used to draw each line for each part of the bird. The
    # the x_coord_1 is used to increment the positon of each of the lines
    # so they look like they are moving
    # in the main function.
        bird1_line_1 = gui.line (x_coord_1, 120, (x_coord_1 + 30),130,'black')
        bird1_line_2 = gui.line (x_coord_1+ 30, 130, (x_coord_1+60),120,'black')
        bird2_line_1 = gui.line (x_coord_1+ 70, 125, (x_coord_1+100),135,'black')
        bird2_line_2 = gui.line (x_coord_1+ 100, 135, (x_coord_1+130),125,'black')
        bird3_line_1 = gui.line (x_coord_1+ 140, 130, (x_coord_1+170),140,'black')
        bird3_line_2 = gui.line (x_coord_1+ 170, 140, (x_coord_1+200),130,'black')
        bird4_line_1 = gui.line (x_coord_1+ 210, 135, (x_coord_1+240),145,'black')
        bird4_line_2 = gui.line (x_coord_1+ 240, 145, (x_coord_1+270),135,'black')
        bird5_line_1 = gui.line (x_coord_1+ 280, 140, (x_coord_1+310),150,'black')
        bird5_line_2 = gui.line (x_coord_1+ 310, 150, (x_coord_1+340),140,'black')

def x_coordinates (x_coord_1, x_coord_2, x_coord_3) :
    # Function has all the if statements to reset the postions
    # of the Birds, and the day and night change of the background.
    # Also, there are the increments for each of x coordinates.
    if x_coord_1 == 700 :
        x_coord_1 = -350
    x_coord_1 += 10
    if x_coord_2 == 600 :
        x_coord_2 = -600
    x_coord_2 += 10
    if x_coord_3 == 600 :
        x_coord_3 = -600
    x_coord_3 += 10
    return x_coord_1, x_coord_2, x_coord_3


def main() :
    gui = graphics (600, 600, 'Parallax')

    # different colors for each of the mountains

    mid_color = random_color (gui)
    left_color = random_color (gui)
    right_color = random_color (gui)

    # Beginning positions of day and night cycle, and the birds

    x_coord_1 = -350
    x_coord_2 = 0
    x_coord_3 = -600

    # Loop since the parallax is considered an animation, so we want the loop to runs
    # forever.

    while True :
        gui.clear()
        mouse_x = gui.mouse_x
        mouse_y = gui.mouse_y
        background_night = gui.rectangle (x_coord_3, -100, 600,2000, 'purple')
        background = gui.rectangle (x_coord_2, -100, 600, 2000, 'light blue')
        sun (gui, mouse_x, mouse_y)
        mid_mountain (gui, mid_color, mouse_x, mouse_y)
        left_mountain (gui,left_color, mouse_x, mouse_y)
        right_mountain (gui, right_color, mouse_x, mouse_y)
        grass_and_blades (gui, mouse_x, mouse_y)
        tree (gui,mouse_x,mouse_y)
        birds (gui, x_coord_1)
        x_coord_1, x_coord_2, x_coord_3 = x_coordinates (x_coord_1, x_coord_2, x_coord_3)
        gui.update_frame(45)

main ()