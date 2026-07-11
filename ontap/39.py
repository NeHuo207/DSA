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


def remove_kth_from_end(head, k):
    dummy = Node(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    for _ in range(k):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next


if __name__ == "__main__":
    print(to_pylist(remove_kth_from_end(build_list([1, 2, 3, 4, 5]), 2)))
    print(to_pylist(remove_kth_from_end(build_list([1, 2, 3, 4, 5]), 1)))
    print(to_pylist(remove_kth_from_end(build_list([1, 2, 3, 4, 5]), 5)))
