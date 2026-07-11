def next_greater(a):
    n = len(a)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and a[stack[-1]] < a[i]:
            idx = stack.pop()
            result[idx] = a[i]
        stack.append(i)

    return result


if __name__ == "__main__":
    print(next_greater([2, 1, 3]))
    print(next_greater([4, 5, 2, 25]))
    print(next_greater([5, 4, 3, 2, 1]))
