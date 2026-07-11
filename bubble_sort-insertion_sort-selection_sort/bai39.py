class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
 
def selection_sort_ll(head):
    curr = head
    while curr:
        min_node = curr
        runner = curr.next
        while runner:
            if runner.val < min_node.val:
                min_node = runner
            runner = runner.next
        curr.val, min_node.val = min_node.val, curr.val
        curr = curr.next
    return head
 
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
print("Bài 14:", ll_to_list(selection_sort_ll(head)))  # [1, 2, 3]
 