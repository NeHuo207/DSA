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


def is_balanced(s):
    st = Stack()
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            st.push(ch)
        elif ch in ")]}":
            if st.isEmpty():
                return False
            if st.pop() != pairs[ch]:
                return False
    return st.isEmpty()


print(is_balanced("()"))
print(is_balanced("{[()]}"))
print(is_balanced("([)]"))
print(is_balanced("((("))
