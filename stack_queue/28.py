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


class QueueFromTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        self.total_real_ops = 0

    def enqueue(self, x):
        self.in_stack.append(x)
        self.total_real_ops += 1

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
                self.total_real_ops += 1
        self.total_real_ops += 1
        return self.out_stack.pop()

q13 = QueueFromTwoStacks()
for i in range(1, 6):
        q13.enqueue(i)
for _ in range(5):
        print(f"  dequeue -> {q13.dequeue()}")
print(f"  tổng thao tác thực tế cho 5 enqueue + 5 dequeue: {q13.total_real_ops} "
          f"(so với 10 thao tác logic -> vẫn là O(n), trung bình O(1)/thao tác)")