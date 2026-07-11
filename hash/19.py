def hash_sum(s, m):
    total = 0
    for ch in s:
        total += ord(ch)
    return total % m


def polynomial_hash(s, p=31, m=10**9 + 9):
    h = 0
    for ch in s:
        h = (h * p + ord(ch)) % m
    return h


def count_collisions(keys, hash_func, m):
    buckets = {}
    for k in keys:
        idx = hash_func(k) % m
        buckets[idx] = buckets.get(idx, 0) + 1

    collisions = sum(cnt - 1 for cnt in buckets.values() if cnt > 1)
    used_buckets = len(buckets)
    return collisions, used_buckets


if __name__ == "__main__":
    keys = [f"key{i}" for i in range(100)]
    m = 50

    c1, b1 = count_collisions(keys, lambda k: hash_sum(k, 10**9), m)
    print(f"hash_sum: {c1} va cham, dung {b1}/{m} bucket")

    c2, b2 = count_collisions(keys, lambda k: polynomial_hash(k), m)
    print(f"polynomial: {c2} va cham, dung {b2}/{m} bucket")
