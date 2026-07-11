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


def simulate(ops):
    st = Stack()
    for op in ops:
        if op[0] == "push":
            st.push(op[1])
        elif op == "pop":
            print(st.pop())
    print("Stack cuối:", st.arr[: st.top + 1])


ops = [("push", 10), ("push", 20), "pop", ("push", 30), ("push", 40)]
simulate(ops)
