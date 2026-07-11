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


def delete_value(head, x):
    if head is None:
        return head
    if head.value == x:
        return head.next
    cur = head
    while cur.next is not None:
        if cur.next.value == x:
            cur.next = cur.next.next
            return head
        cur = cur.next
    return head


h5 = build_list([1, 2, 3, 2])
h5 = delete_value(h5, 2)
print(f"  1->2->3->2, xóa 2 -> {to_pylist(h5)}")
