class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if not self.stack:
            raise IndexError("stack rong")
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


if __name__ == "__main__":
    st = MinStack()
    st.push(5)
    st.push(3)
    st.push(7)
    print(st.getMin())
    st.pop()
    print(st.getMin())
    st.pop()
    print(st.getMin())
