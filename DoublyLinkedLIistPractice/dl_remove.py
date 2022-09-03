import dlist_node
import utils

def dl_remove( head, node_in_list ):

    if head is node_in_list and node_in_list.next is None:
        return None
    
    elif head is node_in_list:
        head = node_in_list.next
        node_in_list.next = None
        node_in_list.prev = None
        head.prev = None
        return head
    

    elif node_in_list.next is None:
        node_in_list.prev.next = None
        node_in_list.prev = None
        return head

    else:
        node_in_list.prev.next = node_in_list.next
        node_in_list.next.prev = node_in_list.prev
        return head
