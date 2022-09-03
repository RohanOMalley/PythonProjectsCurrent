import dlist_node
import utils

def dl_insert_before(head,node_in_list,node_to_insert):

    if head is node_in_list:
        node_to_insert.next = head
        node_in_list.prev = node_to_insert
        node_to_insert.prev = None
        head = node_to_insert
        return head
    else:
        node_to_insert.prev = node_in_list.prev
        node_in_list.prev.next = node_to_insert
        node_in_list.prev = node_to_insert
        node_to_insert.next = node_in_list
        return head
        



def dl_insert_after (head,node_in_list,node_to_insert):

    if head is node_in_list:
        node_in_list.next.prev = node_to_insert
        node_to_insert.next = node_in_list.next
        node_in_list.next = node_to_insert
        node_to_insert.prev = node_in_list
        head = node_in_list
        return head

    elif node_in_list.next is None:
        node_in_list.next = node_to_insert
        node_to_insert.prev = node_in_list
        node_to_insert.next = None
        return head
    else:
        node_in_list.next.prev = node_to_insert
        node_to_insert.next = node_in_list
        node_in_list.next = node_to_insert
        node_to_insert.prev = node_in_list
        return head

