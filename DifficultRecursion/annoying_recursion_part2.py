"""File: annoying_recursion_part2.py

   Author: Rohan O'Malley

   Purpose: The purpose of this program is to test recursion
   in a series of functions. The first function, takes a number
   and returns the sum of every number before it. The second
   function, takes in a number then returns an array of all the 
   fibonacci sequence numbers up to that number. The third
   function, prints out a 'valley' of dots according to the number
   that is passed in which tells how big the valley will be.
"""

def annoying_triangleNumbers(n):
    '''
    Function takes in a number (n) then returns
    the sum of all the numbers up until that (n)

    Params:
        - n - an integer that tells the function
        how much to sum up 
    Returns:
        - Recurses if n is 4 or greater and there are 
        4 base cases that just return what ever the 
        triangle sum is for that number
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 6
    elif n == 4:
        return 4 + annoying_triangleNumbers(3)
    elif n == 5:
        return 5 + annoying_triangleNumbers(4)
    elif n == 6:
        return 6 + annoying_triangleNumbers(5)
    elif n >= 7:
        return n + annoying_triangleNumbers(n - 1)


def annoying_fibonacci_sequence(n):
    '''
    Function takes in a number (n) that
    then prints out an array that has all
    the numbers up to that number (n)

    Params:
        - n - an integer that tells the function
        how many times to return and how many numbers 
        to have in the fibonacci sequence

    Returns:
        - Recurses dependent on the (n) parameter
        4 base cases and 4 recursive cases, 
    '''
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    elif n == 3:
        return [0,1,1]
    elif n == 4:
        return annoying_fibonacci_sequence(3) + [2]
    elif n == 5:
        return annoying_fibonacci_sequence(4) + [3]
    elif n == 6:
        return annoying_fibonacci_sequence(5) + [5]
    elif n >= 7:
        nminus = n - 1
        num_list = annoying_fibonacci_sequence(nminus)
        last2 = num_list[-1] + num_list[-2]
        return num_list + [last2]

def annoying_valley(n):
    '''
    Function take in a number (n) then
    prints out a series of dots with slashes
    that resemble a valley

    Params:
        - n - an integer that indicates how big the
        valley will be
    '''
    if n == 0:
        print()
    elif n == 1:
        print('*')
    elif n == 2:
        print('./')
        print('*')
        print('.\\')
    elif n == 3:
        print('../')
        print('./')
        print('*')
        print('.\\')
        print('..\\')
    elif n == 4:
        print('.../')
        annoying_valley(3)
        print('...\\')
    elif n == 5:
        print('..../')
        annoying_valley(4)
        print('....\\')
    elif n == 6:
        print('...../')
        annoying_valley(5)
        print('.....\\')
    elif n >= 7:
        print('.'* (n-1) +'/')
        annoying_valley(n-1)
        print('.'* (n-1) +'\\')

