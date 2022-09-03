#! /usr/bin/python3

""" Code to test the in_order_vals() function

    Author: Russ Lewis
"""

import tree_funcs_long



###########################################################
#                       INPUT                             #
###########################################################

from tree_node import TreeNode

root = TreeNode(-19)
root.left = TreeNode(52)



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing in_order_vals()...")
    print()

    retval = tree_funcs_long.in_order_vals(root)

    print(f"Returned value: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


