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


def apply(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b


def eval_rpn(tokens):
    st = Stack()
    for tok in tokens:
        if str(tok).isdigit():
            st.push(int(tok))
        else:
            b = st.pop()
            a = st.pop()
            st.push(apply(a, b, tok))
    return st.pop()


tokens = ["2", "3", "4", "*", "+"]
print(eval_rpn(tokens))
