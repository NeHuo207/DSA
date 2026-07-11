import time
import random


def dedup_slow(arr):
    result = []
    for x in arr:
        if x not in result:
            result.append(x)
    return result


def dedup_fast(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


if __name__ == "__main__":
    a = [3, 1, 3, 2, 1]
    print(dedup_slow(a))
    print(dedup_fast(a))

    big = [random.randint(0, 500) for _ in range(5000)]

    t1 = time.time()
    dedup_slow(big)
    t_slow = time.time() - t1

    t2 = time.time()
    dedup_fast(big)
    t_fast = time.time() - t2

    print(f"\nn=5000: slow={t_slow*1000:.1f}ms  fast={t_fast*1000:.1f}ms")
