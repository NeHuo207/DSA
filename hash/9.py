def two_sum(a, target):
    seen = {}
    for i, x in enumerate(a):
        complement = target - x
        if complement in seen:
            return (seen[complement], i)
        seen[x] = i
    return None


if __name__ == "__main__":
    print(two_sum([2, 7, 11], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([1, 2, 3], 100))
