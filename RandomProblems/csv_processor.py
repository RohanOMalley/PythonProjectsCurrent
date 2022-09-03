###
### Author: Rohan O'Malley
### Course: Csc 110
### Description: This program looks into a CSV file given by the user. The user
### then chooses a column to look into and will pick to find the max, min or
### average of that column. At the end of the program, there will be a print
### out of what the answer is in that column.

def average (col_number, last_list):
    '''This function takes the list of the rows and the column number
    from the user and goes through each row at the index of the col_number
    -1 and adds them up. Then divides that total sum by how many rows there
    are to find the average. Then the column number is printed out along with
    the average of that column'''

    total = 0
    # loop is used to go through each row and add to the total
    # at the index given by the user
    for row in last_list:
        total += row[col_number-1]

    # the math done to find the average
    denom = len(last_list)
    avg = total/denom

    print('The average for column',str(col_number),'is:',str(avg))



def minimum (col_number,last_list):
    '''This function takes the column number from the user and
    the list of the rows of the CSV file and first sets the minimun
    number at the first row and column number from the user. Then loops
    through each row and checks that if the column number in the row is less than
    the minimum number then the minimum number will be changed to the current number'''
    min_number = last_list[0][col_number-1]
    # for loop runs through and looks for a minimum value in the list
    for row in last_list:
        if row[col_number-1] < min_number:
            min_number = row[col_number-1]

    print('The minimum value in column',str(col_number),'is:',str(min_number))




def maximum (col_number,last_list):
    '''This function takes in the column number and the list of the rows
    and sets the max number at 0 and then loops through the rows at the
    column number index and checks to see if the current number is greater
    than the max and if it is the max number gets chanegd to the current number.
    Then the max is printed out at the end'''
    max_number = 0
    # for loop runs through list and determines the maxium value
    for rows in last_list:
        if rows[col_number-1] > max_number:
            max_number = rows[col_number-1]

    print('The maximum value in column',str(col_number),'is:',str(max_number))


def main ():
    # the prompts for the user
    csv_file = input('Enter CSV file name:\n')
    col_number = int(input('Enter column number:\n'))
    col_operation = input('Enter column operation:\n')
    csv_2d_list = []

    # reads CSV file into a list
    csv_file = open(csv_file,'r')
    csv_list = csv_file.readlines()
    last_list = []

    # loop goes through the list read from file and
    # turns the strings into floats to be used in the
    # max, min and average functions
    for line in csv_list:
        csv_hold_list = line.strip('\n').split(',')
        final_list = []
        for character in csv_hold_list:
            character = float(character)
            final_list.append(character)
        last_list.append(final_list)

    # if statements check to see what should run based on
    # desired operation from user
    if col_operation == 'max':
        maximum(col_number,last_list)
    elif col_operation == 'min':
        minimum(col_number,last_list)
    elif col_operation == 'avg':
        average(col_number,last_list)

main()