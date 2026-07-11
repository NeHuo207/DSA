class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head


def has_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    h1 = build_list([1, 2, 3, 4, 5])
    print(f"1->2->3->4->5->null  =>  has_cycle = {has_cycle(h1)}")
    h2 = build_list([1, 2, 3, 4, 5])
    tail = h2
    while tail.next is not None:
        tail = tail.next
    node3 = h2.next.next
    tail.next = node3

    print(f"1->2->3->4->5->(quay về 3)  =>  has_cycle = {has_cycle(h2)}")
