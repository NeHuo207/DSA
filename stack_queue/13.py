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


def dfs_iterative(adj, start):
    visited = set()
    st = Stack()
    st.push(start)
    order = []
    while not st.isEmpty():
        u = st.pop()
        if u in visited:
            continue
        visited.add(u)
        order.append(u)
        for v in reversed(adj[u]):
            if v not in visited:
                st.push(v)
    return order


adj = {0: [1, 2], 1: [3], 2: [4], 3: [], 4: []}

print(dfs_iterative(adj, 0))
