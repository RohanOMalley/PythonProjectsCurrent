#! /usr/bin/python3

""" Code to test the annoying_climbDownUp() function

    Author: Russ Lewis
"""

import annoying_recursion





###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    val = 5

    print("Testing annoying_climbDownUp()...")
    print()
    print(f"Input val: {val}")

    retval = annoying_recursion.annoying_climbDownUp(val)

    print(f"Returned val: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


