'''
File: dancing_figures.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to use the graphics module
to make an animation of 4 stick figures. Each figure does a letter
in the YMCA. Each figure also squats around every second and each
figure holds up a letter with thier arms. The letters reset at the end
of the loop.
Course: Fall CS 120
'''
import graphics
import time

def y_guy (gui,position):
    '''This function is for the stick figure with the
    Y. There are 2 main conditons for this function
    when the figure is squatting and standing up. Gui
    is the canvas passed in and the position is a number
    that tracks when the letter should be thrown up.'''
    # when to squat
    if position % 15 == 0:
        body = gui.rectangle( 60, 240, 2, 50, 'orange')
        head = gui.ellipse( 60,220,30,35,'orange')
        left_leg_lower = gui.line(40,300,40,350,'orange',width=2)
        right_leg_lower = gui.line(80,300,80,350,'orange',width=2)
        left_leg_upper = gui.line(61,285,40,300,'orange',width=2)
        right_leg_upper = gui.line(61,285,80,300,'orange',width=2)
        left_arm = gui.line(61, 265, 30, 200, 'orange', width=2)
        right_arm = gui.line(61, 265, 90, 200, 'orange', width=2)
    # when stick figure is standing up
    else:
        body = gui.rectangle( 60, 217, 2, 70, 'orange')
        head = gui.ellipse( 60,200,30,35,'orange')
        left_leg = gui.line(61,285,40,350,'orange',width=2)
        right_leg = gui.line(61,285,80,350,'orange',width=2)
        # holds up  the letter
        if position > 15:
            left_arm = gui.line(61, 240, 30, 180, 'orange', width=2)
            right_arm = gui.line(61, 240, 90, 180, 'orange', width=2)
        else:
            left_arm = gui.line(61, 235, 30, 280, 'orange', width=2)
            right_arm = gui.line(61, 235, 90, 280, 'orange', width=2)

def m_guy (gui, position):
    '''This function is for the figure holding
    the M. Has 2 main conditional statements for 
    standing up and squatting. Gui is canvas passed in.
    Position tracks the number that says when the letter
    is supposed to go up.'''
    # when to squat
    if position % 15 == 0:
        body = gui.rectangle( 190, 240, 2, 50, 'orange')
        head = gui.ellipse( 190,220,30,35,'orange')
        left_leg_lower = gui.line(170,300,170,350,'orange',width=2)
        right_leg_lower = gui.line(210,300,210,350,'orange',width=2)
        left_leg_upper = gui.line(191,285,170,300,'orange',width=2)
        right_leg_upper = gui.line(191,285,210,300,'orange',width=2)
        # holds up letter
        if position > 25:
            left_arm = gui.line(191, 245, 160, 200, 'dark orange', width=2)
            right_arm = gui.line(191, 245, 220, 200, 'dark orange', width=2)
            left_m_arm = gui.line(160,200,191,206,'dark orange', width= 2)
            right_arm_m = gui.line(220, 200, 191, 206, 'dark orange', width=2)
        else:
            left_arm = gui.line(191, 245, 160, 285, 'orange', width=2)
            right_arm = gui.line(191, 245, 220, 285, 'orange', width=2)
    # when stick figure stands up
    else:
        body = gui.rectangle( 190, 217, 2, 70, 'orange')
        head = gui.ellipse( 190,200,30,35,'orange')
        left_leg = gui.line(191,285,170,350,'orange',width=2)
        right_leg = gui.line(191,285,210,350,'orange',width=2)
        # holds up letter
        if position > 25:
            left_arm = gui.line(191, 235, 160, 180, 'dark orange', width=2)
            right_arm = gui.line(191, 235, 220, 180, 'dark orange', width=2)
            left_m_arm =gui.line(160,180,191,186,'dark orange', width= 2)
            right_arm_m = gui.line(220, 180, 191, 186, 'dark orange', width=2)
        else:
            left_arm = gui.line(191, 235, 160, 280, 'orange', width=2)
            right_arm = gui.line(191, 235, 220, 280, 'orange', width=2)

def c_guy(gui, position):
    '''Function is for the figure holding the
    C. There are 2 main conditonals for standing up
    and squatting. Gui is canvas passed in. Position
    is number that tracks when the letter goes up'''
    # when to squat
    if position % 15 == 0:
        body = gui.rectangle( 325, 240, 2, 50, 'orange')
        head = gui.ellipse( 325,220,30,35,'orange')
        upper_left_leg = gui.line(326,285,305,300, 'orange', width=2)
        upper_right_leg = gui.line(326, 285, 345,300 , 'orange', width=2)
        left_leg = gui.line(305, 300, 305, 350,'orange',width=2)
        right_leg = gui.line(345,300,345,350,'orange',width=2)
        # holds up letter
        if position > 35:
            top_arm = gui.line( 326, 245, 365, 200, 'orange', width=2)
            bottom_arm = gui.line( 326, 245, 365, 290, 'orange', width=2)
        else:
            left_arm = gui.line(326, 245, 295, 290, 'orange', width=2)
            right_arm = gui.line(326, 245, 355, 290, 'orange', width=2)
    # when stick figure stands up
    else:
        body = gui.rectangle( 325, 217, 2, 70, 'orange')
        head = gui.ellipse( 325,200,30,35,'orange')
        left_leg = gui.line(326,285,305,350,'orange',width=2)
        right_leg = gui.line(326,285,345,350,'orange',width=2)

        if position > 35:
            top_arm = gui.line( 326, 235, 365, 190, 'orange', width=2)
            bottom_arm = gui.line( 326, 235, 365, 280, 'orange', width=2)
        else:
            left_arm = gui.line(326, 235, 295, 280, 'orange', width=2)
            right_arm = gui.line(326, 235, 355, 280, 'orange', width=2)

def a_guy (gui,position):
    '''Function is for figure holding the A.
    Gui is canvas passed in. 2 main conditonal
    statements for sitting and squatting. Position is number
    that tracks when the letter goes up'''
    # when to squat
    if position % 15 == 0:
        body = gui.rectangle( 450, 240, 2, 50, 'orange')
        head = gui.ellipse( 450, 220, 30,35,'orange')
        upper_left_leg = gui.line(451, 285, 430, 300, 'orange', width=2)
        upper_right_leg = gui.line(451, 285, 470, 300, 'orange', width=2)
        left_leg = gui.line(430, 300, 430,350,'orange',width=2)
        right_leg = gui.line(470, 300, 470,350,'orange',width=2)
        # when to hold up letter
        if position > 45:
            lower_left_arm = gui.line(451, 245, 420, 215, 'dark orange', width=2)
            lower_right_arm = gui.line(451, 245, 480,215, 'dark orange', width=2)
            upper_right_arm = gui.line(480, 215, 460 ,180, 'dark orange', width=2)
            upper_left_arm = gui.line(420, 215, 440, 180, 'dark orange', width=2)
        else:
            left_arm = gui.line(451, 245, 420, 290, 'orange', width=2)
            right_arm = gui.line(451, 245, 480, 290, 'orange', width=2)
    # when person stands up
    else:
        body = gui.rectangle( 450, 217, 2, 70, 'orange')
        head = gui.ellipse( 450, 200, 30,35,'orange')
        left_leg = gui.line(451, 285, 430,350,'orange',width=2)
        right_leg = gui.line(451, 285, 470,350,'orange',width=2)
        if position > 45:
            lower_left_arm = gui.line(451, 225, 420, 200, 'dark orange', width=2)
            lower_right_arm = gui.line(451, 225, 480,200, 'dark orange', width=2)
            upper_right_arm = gui.line(480, 200, 460 ,170, 'dark orange', width=2)
            upper_left_arm = gui.line(420, 200, 440, 170, 'dark orange', width=2)
        else:
            left_arm = gui.line(451, 235, 420, 280, 'orange', width=2)
            right_arm = gui.line(451, 235, 480, 280, 'orange', width=2)

def main():
    gui = graphics.graphics(500,350,'sticks')
    position = 0
    # opens the animation
    while not gui.is_destroyed():
        # when to restart animation loop
        position += 1
        if position > 70:
            position = 0
        
        gui.clear()
        # background
        gui.rectangle(0,0,700,700,'gray')
        y_guy(gui, position)
        m_guy(gui, position)
        c_guy(gui, position)
        a_guy(gui, position)
        gui.update_frame(10)

main()