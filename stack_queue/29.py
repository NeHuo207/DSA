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


class SlidingWindowCounter:
    def __init__(self):
        self.q = deque()

    def add_event(self, t):
        self.q.append(t)

    def count_in_last(self, T, now):
        while self.q and self.q[0] <= now - T:
            self.q.popleft()
        return len(self.q)
counter = SlidingWindowCounter()
for t in [10, 50, 120, 200, 290, 305]:
        counter.add_event(t)
print(f"  số sự kiện trong 300s gần nhất (tính tại now=305): {counter.count_in_last(300, 305)}")