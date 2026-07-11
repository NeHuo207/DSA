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


def to_pylist(head):
    result = []
    cur = head
    while cur:
        result.append(cur.value)
        cur = cur.next
    return result


def reverse_iterative(head):
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev


def reverse_recursive(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    h1 = build_list([1, 2, 3])
    print(to_pylist(reverse_iterative(h1)))

    h2 = build_list([1, 2, 3])
    print(to_pylist(reverse_recursive(h2)))

    h3 = build_list([1])
    print(to_pylist(reverse_iterative(h3)))
