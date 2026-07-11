class BoundedStack:
    def __init__(self, cap):
        self.arr = [0] * cap
        self.cap = cap
        self.top = -1

    def push(self, x):
        if self.top == self.cap - 1:
            raise Exception("Overflow")
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            raise Exception("Underflow")
        x = self.arr[self.top]
        self.top -= 1
        return x


st = BoundedStack(3)
st.push(5)
st.push(10)
st.push(15)
print(st.pop())
print(st.pop())
