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


def insert_after_node(prev_node, x):
    node = Node(x)
    node.next = prev_node.next
    prev_node.next = node


def insert_after_position(head, k, x):
    cur = head
    for _ in range(k):
        if cur is None:
            raise IndexError("vị trí ngoài phạm vi")
        cur = cur.next
    if cur is None:
        raise IndexError("vị trí ngoài phạm vi")
    insert_after_node(cur, x)
    return head


h4 = build_list([1, 3])
insert_after_position(h4, 0, 2)
print(f"  1->3, chèn 2 sau nút 0 -> {to_pylist(h4)}")
