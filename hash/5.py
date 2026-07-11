def group_by(items, key_func):
    groups = {}
    for x in items:
        k = key_func(x)
        if k not in groups:
            groups[k] = []
        groups[k].append(x)
    return groups


if __name__ == "__main__":
    words = ["apple", "avocado", "banana", "blueberry", "cherry"]
    print(group_by(words, lambda w: w[0]))

    nums = [1, 2, 3, 4, 5, 6]
    print(group_by(nums, lambda x: "chan" if x % 2 == 0 else "le"))
