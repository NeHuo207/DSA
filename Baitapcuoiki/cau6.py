'''
Câu 6 (Danh sách liên kết - Linked List)
Khi phát hiện chu trình trong danh sách liên kết bằng thuật toán Floyd (Rùa chạy 1 bước, Thỏ chạy 2 bước), hai con trỏ sẽ gặp nhau tại một điểm nằm trong chu trình. Sau đó, thuật toán đưa 1 con trỏ về lại Node đầu tiên (Head), cả 2 con trỏ cùng đi mỗi nhịp 1 bước thì chúng sẽ gặp nhau tại chính xác nút bắt đầu chu trình. Hãy giải thích nguyên lý toán học đằng sau giai đoạn 2 này.
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def detect_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None 

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow 


n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2  
start = detect_cycle_start(n1)
print(start.val if start else None)