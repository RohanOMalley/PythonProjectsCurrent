#! /usr/bin/python3

""" Code to test the annoying_climbUp() function

    Author: Russ Lewis
"""

import annoying_recursion





###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    val = 0

    print("Testing annoying_climbUp()...")
    print()
    print(f"Input val: {val}")

    retval = annoying_recursion.annoying_climbUp(val)

    print(f"Returned val: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


