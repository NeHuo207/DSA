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


def length(head):
    count = 0
    cur = head
    while cur is not None:
        count += 1
        cur = cur.next
    return count


def build_list(values):
    ll = LinkedList()
    for v in values:
        ll.pushBack(v)
    return ll.head


h = build_list([1, 2, 3])
print(f"  1->2->3 -> độ dài {length(h)}")
