class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, x):
        node = Node(x)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node

    def pushBack(self, x):
        node = Node(x)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def print_all(self):
        cur = self.head
        parts = []
        while cur is not None:
            parts.append(str(cur.value))
            cur = cur.next
        print(" -> ".join(parts) + " -> null")


def build_list(values):
    ll = LinkedList()
    for v in values:
        ll.pushBack(v)
    return ll.head


def to_pylist(head):
    result = []
    cur = head
    while cur is not None:
        result.append(cur.value)
        cur = cur.next
    return result


def reverse_iterative(head):
    prev = None
    cur = head
    while cur is not None:
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


h6 = build_list([1, 2, 3])
h6 = reverse_iterative(h6)
print(f"  lặp:    1->2->3 -> {to_pylist(h6)}")
h6b = build_list([1, 2, 3])
h6b = reverse_recursive(h6b)
print(f"  đệ quy: 1->2->3 -> {to_pylist(h6b)}")
