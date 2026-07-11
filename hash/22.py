def hash_pair(a, b):
    h1, h2 = hash(a), hash(b)
    return h1 ^ (h2 + 0x9E3779B9 + (h1 << 6) + (h1 >> 2))


def hash_tuple(t):
    h = 0
    for x in t:
        h = h ^ (hash(x) + 0x9E3779B9 + (h << 6) + (h >> 2))
    return h


if __name__ == "__main__":
    print(hash_pair(1, 2))
    print(hash_pair(2, 1))

    print(hash_tuple((1, 2, 3)))
    print(hash_tuple((3, 2, 1)))

    pairs = [(1, 2), (2, 1), (1, 3), (3, 1)]
    buckets = {}
    for p in pairs:
        idx = hash_pair(p[0], p[1]) % 10
        buckets.setdefault(idx, []).append(p)
    print(buckets)
