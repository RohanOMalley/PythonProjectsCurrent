#! /usr/bin/python3

""" Code to test the post_order_traversal_print() function

    Author: Russ Lewis
"""

import tree_funcs_long



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = None



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing post_order_traversal_print()...")
    print()

    retval = tree_funcs_long.post_order_traversal_print(root)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


