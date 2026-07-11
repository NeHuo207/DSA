import math


def distribution(keys, m):
    buckets = [0] * m
    for k in keys:
        buckets[k % m] += 1
    return buckets


def std_dev(d):
    mean = sum(d) / len(d)
    return math.sqrt(sum((x - mean) ** 2 for x in d) / len(d))


if __name__ == "__main__":
    keys = [i * 4 for i in range(100)]

    d16 = distribution(keys, 16)
    d17 = distribution(keys, 17)

    print(f"m=16 (2^4):      std={std_dev(d16):.2f}")
    print(f"  {d16}")
    print(f"m=17 (nguyen to): std={std_dev(d17):.2f}")
    print(f"  {d17}")
