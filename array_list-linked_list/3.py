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


def find(head, target):
    cur = head
    idx = 0
    while cur is not None:
        if cur.value == target:
            return idx
        cur = cur.next
        idx += 1
    return -1


h3 = build_list([1, 2, 3])
print(f"  1->2->3, tìm 2 -> vị trí {find(h3, 2)}")
