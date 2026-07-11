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


def find_cycle_start(head):
    slow = head
    fast = head
    met = False
    while fast is not None and fast.next is not None:
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
    # Test 1: KHÔNG có chu trình
    h1 = build_list([1, 2, 3, 4, 5])
    result1 = find_cycle_start(h1)
    print(f"Test 1: 1->2->3->4->5->null")
    print(f"  => {result1} \n")

    # Test 2: chu trình bắt đầu tại nút giá trị 3
    h2 = build_list([1, 2, 3, 4, 5])
    tail = h2
    while tail.next is not None:
        tail = tail.next
    node3 = h2.next.next
    tail.next = node3

    result2 = find_cycle_start(h2)
    print(f"Test 2: 1->2->3->4->5->(quay về 3)")
    print(f"  => điểm bắt đầu chu trình = {result2.value}")

    # Test 3: chu trình bắt đầu ngay tại HEAD
    h3 = build_list([1, 2, 3])
    tail3 = h3
    while tail3.next is not None:
        tail3 = tail3.next
    tail3.next = h3

    result3 = find_cycle_start(h3)
    print(f"\nTest 3: 1->2->3->(quay về 1, tức head)")
    print(f"  => điểm bắt đầu chu trình = {result3.value}")

    # Test 4: chu trình là 1 nút tự trỏ về chính nó
    h4 = Node(7)
    h4.next = h4

    result4 = find_cycle_start(h4)
    print(f"\nTest 4: 7->(tự trỏ về chính nó)")
    print(f"  => điểm bắt đầu chu trình = {result4.value}")
