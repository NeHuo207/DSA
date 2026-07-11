def count_frequency(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq


if __name__ == "__main__":
    print(count_frequency(["a", "b", "a", "c", "a"]))
    print(count_frequency([1, 2, 2, 3, 3, 3]))
