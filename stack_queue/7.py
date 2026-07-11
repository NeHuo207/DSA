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


class MinStack:
    def __init__(self):
        self.st = Stack()
        self.minSt = Stack()

    def push(self, x):
        self.st.push(x)
        if self.minSt.isEmpty() or x <= self.minSt.top_val():
            self.minSt.push(x)
        else:
            self.minSt.push(self.minSt.top_val())

    def pop(self):
        self.minSt.pop()
        return self.st.pop()

    def getMin(self):
        return self.minSt.top_val()


st = MinStack()
st.push(5)
st.push(2)
st.push(7)
st.push(1)
print(st.getMin())
st.pop()
print(st.getMin())
