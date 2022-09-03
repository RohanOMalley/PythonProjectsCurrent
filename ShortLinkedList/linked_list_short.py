import list_node


def list_to_array (head):
    cur = head
    return_list = []
    if head is None:
        return []
    while cur is not None:
        return_list.append(cur.val)
        cur = cur.next
    return return_list

sh = ['T','e','s','t','i','n','g','!']

def array_to_list (data):
    if len(data) == 0:
        return None
    i = 1
    in_list = list_node.ListNode(data[0])
    cur = in_list
    while i < len(data):
        cur.next = list_node.ListNode(data[i])
        cur = cur.next
        i += 1
    return in_list

array_to_list(sh)

def list_length(head):
    i = 0
    cur = head
    while cur is not None:
        i += 1
        cur = cur.next
    return i
    

def split_list (old_head):
    count = 0
    cur = old_head
    while cur is not None:
        count += 1
        cur = cur.next
    
    if count == 1:
        head1 = old_head
        head2 = None
        return head1, head2
    elif count % 2 == 0:
        split = count // 2
        i = 0

        head1 = old_head
        new_cur = head1

        while i < split - 1:
            new_cur = new_cur.next
            i += 1
        
        head2 = new_cur.next
        new_cur.next = None
        cur_last = head2
        
        # while i < count:

        #     cur_last = cur_last.next

        #     i += 1

        return head1, head2


    else:
        num = count / 2
        split_low = (int(num))

        head1 = old_head
        new_cur = head1

        i = 0
        while i < split_low :
            new_cur = new_cur.next
            i += 1
        
        head2 = new_cur.next
        new_cur.next = None
        last_cur = head2

        while i < num:
            last_cur = last_cur.next
            i += 1

        return old_head , head2


    