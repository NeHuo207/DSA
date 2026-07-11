class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, x):
        self.arr.append(x)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue Empty")
        return self.arr.pop(0)

    def isEmpty(self):
        return len(self.arr) == 0


class Stack:
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        return self.arr.pop()

    def isEmpty(self):
        return len(self.arr) == 0


def reverse_queue(q):
    st = Stack()
    while not q.isEmpty():
        st.push(q.dequeue())
    while not st.isEmpty():
        q.enqueue(st.pop())


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

reverse_queue(q)

while not q.isEmpty():
    print(q.dequeue(), end=" ")
