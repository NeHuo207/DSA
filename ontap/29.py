from collections import deque


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
    print(max_sliding_window([1, 3, -1, -3, 5, 3], 3))
    print(max_sliding_window([1, 2, 3, 4, 5], 2))
    print(max_sliding_window([9, 8, 7], 2))
