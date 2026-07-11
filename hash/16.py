def hash_modulo(k, m):
    return k % m


if __name__ == "__main__":
    print(hash_modulo(37, 10))

    m = 10
    keys = [12, 25, 37, 48, 55, 63, 71, 89]
    buckets = {}
    for k in keys:
        idx = hash_modulo(k, m)
        buckets.setdefault(idx, []).append(k)

    for i in range(m):
        print(f"bucket {i}: {buckets.get(i, [])}")
