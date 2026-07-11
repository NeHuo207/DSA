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


class Stack:

    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack Empty")
        return self.arr.pop()

    def isEmpty(self):
        return len(self.arr) == 0


class QueueByStack:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, x):
        self.s1.push(x)

    def dequeue(self):
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
        if self.s2.isEmpty():
            raise Exception("Queue Empty")
        return self.s2.pop()


q = QueueByStack()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.dequeue())

q.enqueue(40)

print(q.dequeue())
print(q.dequeue())
