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


def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    print(find_middle(build_list([1, 2, 3, 4, 5])).value)
    print(find_middle(build_list([1, 2, 3, 4])).value)
    print(find_middle(build_list([1])).value)
