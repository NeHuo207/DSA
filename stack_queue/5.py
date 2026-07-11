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


def print_and_restore(st):
    temp = Stack()
    count = 0
    while not st.isEmpty():
        x = st.pop()
        print(x)
        temp.push(x)
        count += 1
    while not temp.isEmpty():
        st.push(temp.pop())
    return count


st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
count = print_and_restore(st)
print("Count =", count)
print("Top =", st.top_val())
