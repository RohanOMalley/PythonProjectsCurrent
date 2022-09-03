###
### Author: Rohan O'Malley
### Course: CSC 110
### Description: user inputs a shape they want to display either an
### hourglass, plumbbob or a house. Then, they can choose what character
### will print out in the shape they choose and the height of the rows in
### the shape.

def up_arrow (character):

    # Prints out character from user input
    # with spaces to make it into an
    # upward facing arrow

    print('     ' + character * 1)
    print('    ' + character * 3)
    print('   ' + character * 5)
    print('  ' + character * 7)
    print(' ' + character * 9)
    print('' + character * 11)

def down_arrow (character) :

    # Prints out character from user inputs
    # into a downward facing arrow using
    # different numbered spaces

    print('' + character * 11)
    print(' ' + character * 9)
    print('  ' + character * 7)
    print('   ' + character * 5)
    print('    ' + character * 3)
    print('     ' + character * 1)

def rows (height):

    # Uses user input to figure out how many rows to print
    # in the main fuction

    i = 0
    while i < height:
        print('|---------|')

        i += 1


def main ():

    display=input('Enter shape to display:\n')
    character=input('Enter arrow character:\n')
    height=int(input('Enter row-area height:\n'))

    print(' ')

    if display == ('hourglass') :
        rows(height)
        down_arrow(character)
        up_arrow(character)
        rows (height)

    elif display == ('plumbbob') :
        up_arrow(character)
        rows(height)
        down_arrow(character)

    elif display == ('house') :
        up_arrow(character)
        rows(height)

main()