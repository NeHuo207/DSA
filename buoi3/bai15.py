class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
 
def insertion_sort_ll(head):
    dummy = Node(0)
    curr = head
    while curr:
        prev = dummy
        while prev.next and prev.next.val < curr.val:
            prev = prev.next
        nxt = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = nxt
    return dummy.next
 
def list_to_ll(lst):
    d = Node(0); c = d
    for v in lst:
        c.next = Node(v); c = c.next
    return d.next
 
def ll_to_list(head):
    res = []
    while head:
        res.append(head.val); head = head.next
    return res
 
head = list_to_ll([3, 1, 2])
print("Bài 15:", ll_to_list(insertion_sort_ll(head)))  # [1, 2, 3]