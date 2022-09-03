"""File: linked_list_recurison_part2.py

   Author: Rohan O'Malley

   Purpose: The purpose of this program is to set up 3 functions 
   that each test different aspects of linked list recursion. The
   first function takes and array then builds a linked list from the
   array. The second function, keeps every other node in the list
   and discards the rest. The third funciton, takes 2 lists and at 
   iteration each node from each list is put into a tuple into a new
   node in a new linked list.
"""
import list_node
def array_to_list_recursive (data):
    '''
    Function takes an array that is passed in
    and recursively builds a linked list.
    
    Params:
        - data - an array
    
    Returns:
        - head - a linked list of that represents
        all the data from the array passed in
    '''
    if data == []:
        return None
    head = list_node.ListNode(data[0])
    head.next = array_to_list_recursive(data[1:])
    return head

def accordion_recursive (head):
    '''
    Function takes in a linked list then
    recurses through the list and removes 
    every other node then returns the list
    with the nodes removed

    Params:
        - head - a linked list

    Returns:
        - head - same list as before but 
        without every other node, so a smaller list
    '''
    if head is None:
        return None
    head = head.next
    if head is None:
        return None
    head.next = accordion_recursive(head.next)
    
    return head

def pair_recursive (head1, head2):
    '''
    Function takes 2 linked lists
    then at each node takes both nodes
    and makes a tuple pair and puts that
    tuple in a new list, then at the end
    that list is returned

    Params:
        - head1 - a linked list
        - head2- a linked list
    Returns:
        - if head1 or head2 none it returns None
        - at the end it will return the new_head
        which is the linked list with all of the tuples
    '''
    if head1 is None or head2 is None:
        return None
    else:
        new_head = list_node.ListNode((head1.val, head2.val))
        new_head.next = pair_recursive(head1.next, head2.next)
        return new_head
