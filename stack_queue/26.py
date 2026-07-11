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


def max_sliding_window(a, k):
    dq = deque()
    result = []

    for i in range(len(a)):
        while dq and a[dq[-1]] < a[i]:
            dq.pop()
        dq.append(i)

        if dq[0] <= i - k:
            dq.popleft()

        if i >= k - 1:
            result.append(a[dq[0]])

    return result


if __name__ == "__main__":
    a = [1, 3, -1, -3, 5, 3]
    print(f"  a={a}, k=3 -> {max_sliding_window(a, 3)}") 