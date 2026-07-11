import random
import time


def generate_colliding_keys(m, num_keys, target_bucket=0):
    return [target_bucket + i * m for i in range(num_keys)]


def build_table(keys, m):
    buckets = {}
    start = time.time()
    for k in keys:
        idx = k % m
        buckets.setdefault(idx, []).append(k)
    elapsed = time.time() - start
    max_bucket = max(len(v) for v in buckets.values())
    return max_bucket, len(buckets), elapsed


if __name__ == "__main__":
    m = 1024
    num_keys = 2000

    normal_keys = [random.randint(0, 10**6) for _ in range(num_keys)]
    mx1, used1, t1 = build_table(normal_keys, m)
    print(f"khoa ngau nhien: bucket lon nhat = {mx1}, dung {used1}/{m} bucket")

    evil_keys = generate_colliding_keys(m, num_keys)
    mx2, used2, t2 = build_table(evil_keys, m)
    print(f"khoa tan cong:   bucket lon nhat = {mx2}, dung {used2}/{m} bucket")
