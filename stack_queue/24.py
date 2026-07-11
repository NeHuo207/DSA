class Queue:

    def __init__(self):
        self.arr = []

    def enqueue(self, x):
        self.arr.append(x)

    def dequeue(self):
        return self.arr.pop(0)

    def isEmpty(self):
        return len(self.arr) == 0


def bfs(adj, start):
    visited = set()
    q = Queue()
    q.enqueue(start)
    visited.add(start)
    while not q.isEmpty():
        u = q.dequeue()
        print(u, end=" ")
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                q.enqueue(v)


adj = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [], 5: []}

bfs(adj, 0)
