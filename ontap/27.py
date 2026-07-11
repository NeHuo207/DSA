class QueueFromTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        self.total_ops = 0

    def enqueue(self, x):
        self.in_stack.append(x)
        self.total_ops += 1

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
                self.total_ops += 1
        if not self.out_stack:
            raise IndexError("rong")
        self.total_ops += 1
        return self.out_stack.pop()

    def isEmpty(self):
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    q = QueueFromTwoStacks()
    for i in [1, 2, 3]:
        q.enqueue(i)
    print(q.dequeue(), q.dequeue())
    q.enqueue(4)
    print(q.dequeue(), q.dequeue())

    q2 = QueueFromTwoStacks()
    n = 1000
    for i in range(n):
        q2.enqueue(i)
    for i in range(n):
        q2.dequeue()
    print(f"{2*n} thao tac -> {q2.total_ops} op thuc te = {q2.total_ops/(2*n):.2f}/op")
