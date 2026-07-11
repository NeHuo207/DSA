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


def peek_front(q):
    return q.arr[q.front_idx]


def peek_rear(q):
    return q.arr[len(q.arr) - 1]


q = Queue()

q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

print(peek_front(q))
print(peek_rear(q))
