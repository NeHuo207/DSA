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


def stock_span(prices):
    n = len(prices)
    span = [0] * n
    st = Stack()
    for i in range(n):
        while (not st.isEmpty()) and prices[st.top_val()] <= prices[i]:

            st.pop()
        if st.isEmpty():
            span[i] = i + 1
        else:
            span[i] = i - st.top_val()
        st.push(i)
    return span


prices = [100, 80, 60, 70, 60, 75, 85]

print(stock_span(prices))
