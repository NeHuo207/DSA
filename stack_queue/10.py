class Stack:
    def __init__(self):
        self.arr = []
        self.top = -1

    def push(self, x):
        self.top += 1
        if self.top == len(self.arr):
            self.arr.append(x)
        else:
            self.arr[self.top] = x

    def pop(self):
        if self.isEmpty():
            raise Exception("Underflow")
        x = self.arr[self.top]
        self.top -= 1
        return x

    def top_val(self):
        if self.isEmpty():
            raise Exception("Stack Empty")
        return self.arr[self.top]

    def isEmpty(self):
        return self.top == -1


class Queue:

    def __init__(self):
        self.arr = []
        self.front = 0

    def enqueue(self, x):
        self.arr.append(x)

    def dequeue(self):
        x = self.arr[self.front]
        self.front += 1
        return x

    def isEmpty(self):
        return self.front == len(self.arr)


class StackFromQueues:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.enqueue(x)
        while not self.q1.isEmpty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.dequeue()


st = StackFromQueues()

st.push(10)
st.push(20)
st.push(30)

print(st.pop())
print(st.pop())
print(st.pop())
