from collections import deque
class Queue:
    def __init__(self):
        self.arr = []
        self.front_idx = 0

    def enqueue(self, x):
        self.arr.append(x)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue Empty")
        x = self.arr[self.front_idx]
        self.front_idx += 1
        return x

    def isEmpty(self):
        return self.front_idx == len(self.arr)


def josephus(n, k):
    q = deque(range(1, n + 1))

    while len(q) > 1:
        for _ in range(k - 1):
            q.append(q.popleft())
        q.popleft()

    return q[0]
print(f"  n=5, k=2 -> người sống sót số {josephus(5, 2)}")  