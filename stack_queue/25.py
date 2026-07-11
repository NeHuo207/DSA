import heapq


class Queue:
    def __init__(self):
        self.arr = []
        self.front_idx = 0

    def enqueue(self, x):
        self.arr.append(x)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue Empty")
        x = self.arr[self.front_idx]
        self.front_idx += 1
        return x

    def isEmpty(self):
        return self.front_idx == len(self.arr)


class PriorityQueue:

    def __init__(self):
        self.heap = []

    def push(self, x):
        heapq.heappush(self.heap, x)

    def pop(self):
        if len(self.heap) == 0:
            raise Exception("Priority Queue Empty")
        return heapq.heappop(self.heap)

    def isEmpty(self):
        return len(self.heap) == 0


pq = PriorityQueue()

pq.push(5)
pq.push(2)
pq.push(8)
pq.push(1)

while not pq.isEmpty():

    print(pq.pop(), end=" ")
