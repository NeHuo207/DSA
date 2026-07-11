from collections import deque


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


def round_robin(processes, quantum):
    q = deque(processes)
    time = 0
    completion = {}

    while q:
        pid, remaining = q.popleft()
        run = min(quantum, remaining)
        time += run
        remaining -= run

        if remaining == 0:
            completion[pid] = time
        else:
            q.append((pid, remaining))

    return completion
processes = [(1, 5), (2, 3), (3, 8)]
result = round_robin(processes, quantum=2)
for pid in sorted(result):
        print(f"  Process {pid} hoàn thành lúc: {result[pid]}")