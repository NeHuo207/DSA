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


def add_two_numbers(l1, l2):
    dummy = Node(0)
    tail = dummy
    carry = 0
    while l1 is not None or l2 is not None or carry != 0:
        v1 = l1.value if l1 is not None else 0
        v2 = l2.value if l2 is not None else 0
        total = v1 + v2 + carry
        carry = total // 10
        tail.next = Node(total % 10)
        tail = tail.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    return dummy.next


n1 = build_list([2, 4, 3])
n2 = build_list([5, 6, 4])
print(f"  (2->4->3) + (5->6->4) -> {to_pylist(add_two_numbers(n1, n2))}")
