import list_node

def is_sorted(head):
    if head is None:
        return True
    elif head.next is None:
        return True
    else:
        cur = head
        first_val = cur.val
        while cur is not None:
            if cur.val < first_val:
                return False
            first_val = cur.val
            cur = cur.next
        return True


def is_sorted_recursive(head):
    if head is None:
        return True
    elif head.next is None:
        return True
    else:
        if head.val <= head.next.val:
            return is_sorted_recursive(head.next)
        else:
            return False
