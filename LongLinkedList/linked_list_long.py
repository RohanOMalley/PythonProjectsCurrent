'''
File: linked_list_long.py
Author: Rohan O'Malley
Purpose: The purpose of this program is to hold 5 different 
functions that test certain aspects of linked lists. The first 
function checks to see if the linked list is in order, Second funct
find the sum of all the numbers in the linked list and returns it,
Third funct puts even nodes in a list and odd nodes in a list
Fourth funct starts at a node and then keeps every 4th node after that,
Course: Fall CS 120
'''
import list_node

def is_sorted (head):
    '''
    Function checks to see if the list is in 
    ascending order
    Parameters:
        head - a linked list 
    Returns:
        True - if the list is in ascending order
               or there is nothing in linked list
               or there is only one element in the 
               list
        False - the list is not in ascending order
    '''
    if head.next is None or head is None:
        return True

    cur = head
    # loop goes through list and checks to see
    # if each val from the node is in ascending order
    while cur is not None:
        holder = cur.val
        if cur.next is None:
            break
        elif holder <= cur.next.val:
            cur = cur.next
            continue
        else:
            return False
    return True

def list_sum (head):
    '''
    This function runs through a list of numbers
    and adds them up 
    Parameter:
        head - this is a linked list 
    Returns:
        sum_of_list - this is the sum of all
                      the numbers in the list
    '''
    if head is None:
        return 0
    else:
        cur = head
        sum_of_list = 0
        # adds up every val in list
        while cur is not None:
            sum_of_list += cur.val
            cur = cur.next
        return sum_of_list


def partition_list (head):
    '''
    This function goes through a list and puts every other
    node into an even list and odd list then returns them
    Parameter:
        head - a linked list 
    Returns:
        even_list - list with all the even nodes 
        odd_list - list with all the odd nodes
    Misc:
        - there are 2 different temp variables since there
        are 2 different lists that need to be tracked
    '''
    count = 0
    cur = head
    even_head = None
    even_cur = even_head
    odd_head = None
    odd_cur = odd_head
    # loop goes through each node in list and assigns to 
    # a different node to the even list or the odd list
    while cur is not None:
        # for the even list
        if count % 2 == 0 :
            if even_head is None:
                temp = cur
                even_head = cur
                cur = cur.next
                temp.next = None
            else:
                temp.next = cur
                temp = cur
                even_cur = cur.next
                cur = cur.next
                temp.next = None
        else:
            # for the odd list
            if odd_head is None: 
                odd_temp = cur
                odd_head = cur
                cur = cur.next
                odd_temp.next = None
            else:
                odd_temp.next = cur
                odd_temp = cur
                odd_cur = cur.next
                cur = cur.next
                odd_temp.next = None
        count += 1
    return even_head, odd_head

        
def accordion_4 (head, start_pos):
    '''
    Function takes in a list that starts at a certain
    node and then keeps every 4th node after that in a list
    Parameters:
        head - a linked list passed in
    Returns:
        None - if start position is negative,
               if there is nothing in the linked list
        new_head - list with all the 4th nodes and
                    start position
    Misc:
        - the temporary variable holds the place in the 
        list 
    '''
    # if start pos is less than 0
    if start_pos < 0:
        return None
    # if nothing in list
    elif head is None:
        return None
    else:
        count = 0
        remove_node = start_pos + 4
        cur = head
        new_head = None
        # loop goes through the head list
        # takes 
        while cur is not None:
            # to start the list 
            if count == start_pos:
                temp = cur
                new_head = cur
                cur = cur.next
                temp.next = None
            # to add every 4th node to the list
            elif count > start_pos and count == remove_node:
                temp.next = cur
                temp = cur
                cur = cur.next
                temp.next = None
                remove_node += 4
            else:
                cur = cur.next
            count += 1
    return new_head

def pair (list_1, list_2):
    '''
    Function reads through two lists then makes 
    a tuple with each position in each list. Then
    each tuple is put into a list and returned
    Parameters:
        list_1 - a linked list
        list_2 - a linked list
    Returns:
        new_head - a linked list with all the tuple pairs
    Misc:
        - The length of the shorter list is how many tuples
        there will be in returned list
    '''
    head = list_1
    cur = head

    first_count = 0
    # loop goes through and finds length of
    # first list
    while cur is not None:
        first_count += 1
        cur = cur.next
    
    head = list_2
    cur = head
    second_count = 0
    # loop goes through and finds length of 
    # second list
    while cur is not None:
        second_count += 1
        cur = cur.next
    # ifs pick which list is shorter
    # then use that to put that many tuples 
    if first_count > second_count:
        short = second_count
    elif second_count > first_count:
        short = first_count
    else:
        short = first_count
    
    head1 = list_1
    head2 = list_2
    cur1 = head1
    cur2 = head2

    new_head = None
    # loop goes through each till the end
    # of the shorter list
    for i in range(short):
        if i == 0:
            new_head = list_node.ListNode(tuple((cur1.val,cur2.val)))
            new_cur = new_head
            cur1 = cur1.next
            cur2 = cur2.next
        else:
            new_node = list_node.ListNode(tuple((cur1.val,cur2.val)))
            new_cur.next = new_node
            new_cur = new_cur.next
            cur1 = cur1.next
            cur2 = cur2.next
    return new_head

            



