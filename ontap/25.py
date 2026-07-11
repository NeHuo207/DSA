def largest_rectangle(h):
    stack = []
    max_area = 0
    n = len(h)

    for i in range(n + 1):
        cur = 0 if i == n else h[i]

        while stack and h[stack[-1]] >= cur:
            height = h[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area


if __name__ == "__main__":
    print(largest_rectangle([2, 1, 5, 6, 2, 3]))
    print(largest_rectangle([2, 4]))
    print(largest_rectangle([1, 1, 1, 1]))
