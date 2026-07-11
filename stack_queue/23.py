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


class Deque:

    def __init__(self):
        self.arr = []

    def push_front(self, x):
        self.arr.insert(0, x)

    def push_back(self, x):
        self.arr.append(x)

    def pop_front(self):
        return self.arr.pop(0)

    def pop_back(self):
        return self.arr.pop()


dq = Deque()

dq.push_back(10)
dq.push_back(20)
dq.push_front(5)
dq.push_front(1)

print(dq.pop_front())
print(dq.pop_back())
print(dq.pop_front())
print(dq.pop_back())
