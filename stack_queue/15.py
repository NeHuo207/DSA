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


def sort_stack(st):
    aux = Stack()
    while not st.isEmpty():
        temp = st.pop()
        while (not aux.isEmpty()) and aux.top_val() > temp:
            st.push(aux.pop())
        aux.push(temp)
    while not aux.isEmpty():
        st.push(aux.pop())
    return st


st = Stack()

st.push(4)
st.push(1)
st.push(3)
st.push(2)

sort_stack(st)

while not st.isEmpty():

    print(st.pop(), end=" ")
