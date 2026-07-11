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


def largest_rectangle(h):
    st = Stack()
    max_area = 0
    for i in range(len(h) + 1):
        if i == len(h):
            cur = 0
        else:
            cur = h[i]
        while (not st.isEmpty()) and h[st.top_val()] >= cur:
            height = h[st.pop()]
            if st.isEmpty():
                width = i
            else:
                width = i - st.top_val() - 1
            area = height * width
            if area > max_area:
                max_area = area
        st.push(i)
    return max_area


h = [2, 1, 5, 6, 2, 3]

print(largest_rectangle(h))
