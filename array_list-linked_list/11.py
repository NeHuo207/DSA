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


class DNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, x):
        node = DNode(x)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
        return node

    def pushBack(self, x):
        node = DNode(x)
        node.prev = self.tail
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
        return node

    def popFront(self):
        if self.head is None:
            raise IndexError("danh sách rỗng")
        node = self.head
        self.head = node.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return node.value

    def popBack(self):
        if self.tail is None:
            raise IndexError("danh sách rỗng")
        node = self.tail
        self.tail = node.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return node.value

    def remove(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = node.next = None

    def traverse_forward(self):
        result = []
        cur = self.head
        while cur is not None:
            result.append(cur.value)
            cur = cur.next
        return result

    def traverse_backward(self):
        result = []
        cur = self.tail
        while cur is not None:
            result.append(cur.value)
            cur = cur.prev
        return result


dll = DoublyLinkedList()
dll.pushFront(2)
dll.pushBack(3)
dll.pushFront(1)
print(f"  duyệt xuôi:  {dll.traverse_forward()}")
print(f"  duyệt ngược: {dll.traverse_backward()}")
print(
    f"  popFront = {dll.popFront()}, popBack = {dll.popBack()} -> {dll.traverse_forward()}"
)
