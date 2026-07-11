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


def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 is not None and l2 is not None:
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 is not None else l2
    return dummy.next


def sort_list(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    right = slow.next
    slow.next = None

    left_sorted = sort_list(head)
    right_sorted = sort_list(right)
    return merge_sorted_lists(left_sorted, right_sorted)

h13 = build_list([3, 1, 2])
h13 = sort_list(h13)
print(f"  3->1->2 -> {to_pylist(h13)}")