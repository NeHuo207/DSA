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
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def find_cycle_start(head):
    slow = head
    fast = head
    met = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            met = True
            break

    if not met:
        return None

    ptr1 = head
    ptr2 = slow
    while ptr1 is not ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1


if __name__ == "__main__":
    h1 = build_list([1, 2, 3, 4, 5])
    print(has_cycle(h1), find_cycle_start(h1))

    h2 = build_list([1, 2, 3, 4, 5])
    tail = h2
    while tail.next:
        tail = tail.next
    node3 = h2.next.next
    tail.next = node3

    print(has_cycle(h2), find_cycle_start(h2).value)

    h3 = build_list([1, 2, 3])
    tail3 = h3
    while tail3.next:
        tail3 = tail3.next
    tail3.next = h3
    print(has_cycle(h3), find_cycle_start(h3).value)
