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


def simulate_queue(ops):
    q = Queue()
    for op in ops:
        if op[0] == "enqueue":
            q.enqueue(op[1])
        elif op == "dequeue":
            print(q.dequeue())
    print("Queue cuối:", q.arr[q.front_idx :])


ops = [("enqueue", 5), ("enqueue", 7), "dequeue", ("enqueue", 9)]

simulate_queue(ops)
