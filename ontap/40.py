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


def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next


def sort_list(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    right = slow.next
    slow.next = None

    left_sorted = sort_list(head)
    right_sorted = sort_list(right)
    return merge_sorted_lists(left_sorted, right_sorted)


if __name__ == "__main__":
    print(to_pylist(sort_list(build_list([3, 1, 2]))))
    print(to_pylist(sort_list(build_list([4, 2, 1, 3]))))
    print(to_pylist(sort_list(build_list([5, 4, 3, 2, 1]))))
