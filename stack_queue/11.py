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


def next_greater(a):
    n = len(a)
    result = [-1] * n
    st = Stack()
    for i in range(n):
        while (not st.isEmpty()) and a[st.top_val()] < a[i]:
            idx = st.pop()
            result[idx] = a[i]
        st.push(i)
    return result


a = [2, 1, 5, 3, 4]

print(next_greater(a))
