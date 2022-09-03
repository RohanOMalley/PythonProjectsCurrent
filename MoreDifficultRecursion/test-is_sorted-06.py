#! /usr/bin/python3

""" Code to test the is_sorted() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import linked_list_recursion





# INPUT:
#   First, we build a list of nodes.
#   Then we chain them together.

vals  = []
nodes = [list_node.ListNode(val) for val in vals]

in_list = None



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    print("Testing is_sorted()...")
    print()
    print(f"Input list: {in_list}")

    retval = linked_list_recursion.is_sorted(in_list)

    print(f"retval: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


