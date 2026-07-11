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


q = CircularQueue(4)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())

q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
