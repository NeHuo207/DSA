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


class CircularQueue:

    def __init__(self, cap):
        self.arr = [0] * cap
        self.cap = cap
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, x):
        if self.count == self.cap:
            raise Exception("Queue Full")

        self.arr[self.rear] = x
        self.rear = (self.rear + 1) % self.cap
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception("Queue Empty")

        x = self.arr[self.front]
        self.front = (self.front + 1) % self.cap
        self.count -= 1
        return x

    def isEmpty(self):
        return self.count == 0


def safe_dequeue(q):
    if q.isEmpty():
        raise Exception("Queue Empty")
    return q.dequeue()


def safe_enqueue(q, x, cap):
    if q.count == cap:
        raise Exception("Queue Full")
    q.enqueue(x)


q = CircularQueue(3)

safe_enqueue(q, 10, 3)
safe_enqueue(q, 20, 3)
safe_enqueue(q, 30, 3)

print(safe_dequeue(q))
print(safe_dequeue(q))
