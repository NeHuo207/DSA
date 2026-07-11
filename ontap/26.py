class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, x):
        self.arr.append(x)

    def dequeue(self):
        if not self.arr:
            raise IndexError("rong")
        return self.arr.pop(0)

    def isEmpty(self):
        return len(self.arr) == 0


class CircularQueue:
    def __init__(self, cap):
        self.cap = cap
        self.arr = [None] * cap
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, x):
        if self.count == self.cap:
            raise Exception("day")
        self.arr[self.rear] = x
        self.rear = (self.rear + 1) % self.cap
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception("rong")
        x = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.cap
        self.count -= 1
        return x

    def isFull(self):
        return self.count == self.cap

    def isEmpty(self):
        return self.count == 0


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())

    cq = CircularQueue(4)
    for i in [1, 2, 3, 4]:
        cq.enqueue(i)
    print(cq.isFull())
    print(cq.dequeue(), cq.dequeue())
    cq.enqueue(5)
    cq.enqueue(6)
    print(cq.arr, cq.front, cq.rear)
