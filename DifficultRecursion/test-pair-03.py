#! /usr/bin/python3

""" Code to test the pair_recursive() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import linked_list_recursion_part2



# INPUT:
#   First, we build a list of nodes.
#   Then we chain them together.

vals1  = [10, 21, 31, 86, 56, 18, 80, 82, 24, -6, 85, 27, 58, 39, 15, 90]
vals2  = vals1[::-1]
nodes1 = [list_node.ListNode(val) for val in vals1]
nodes2 = [list_node.ListNode(val) for val in vals2]

in_list1 = nodes1[0]
for i in range(len(vals1)-1):
    nodes1[i].next = nodes1[i+1]

in_list2 = nodes2[0]
for i in range(len(vals2)-1):
    nodes2[i].next = nodes2[i+1]



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    print("Testing pair_recursive()...")
    print()
    print(f"Input list 1: {in_list1}")
    print(f"Input list 2: {in_list2}")
    print()

    out_list = linked_list_recursion_part2.pair_recursive(in_list1, in_list2)

    print(f"Output list: {out_list}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


