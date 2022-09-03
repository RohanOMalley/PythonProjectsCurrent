#! /usr/bin/python3

""" Code to test the bst_insert_loop() function

    Author: Russ Lewis
"""

import tree_funcs_long

from tree_node import TreeNode



###########################################################
#                       INPUT                             #
###########################################################

vals = [ -19, 52 ]



###########################################################
#                     TEST CODE                           #
###########################################################
def main():
    print("Testing bst_insert_loop()...")
    print()

    root = TreeNode(vals[0])
    for v in vals[1:]:
        tree_funcs_long.bst_insert_loop(root, v)

    print("IN-ORDER TRAVERSAL:")
    tree_funcs_long.in_order_traversal_print(root)
    print()

    print("PRE-ORDER TRAVERSAL:")
    tree_funcs_long.pre_order_traversal_print(root)
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


