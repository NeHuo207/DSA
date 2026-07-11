import time

EMPTY = object()


class HashTableChaining:
    def __init__(self, m=8):
        self.m = m
        self.buckets = [[] for _ in range(m)]

    def put(self, key, value):
        idx = hash(key) % self.m
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))

    def get(self, key):
        idx = hash(key) % self.m
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return None


class HashTableLinearProbing:
    def __init__(self, m=8):
        self.m = m
        self.table = [EMPTY] * m

    def put(self, key, value):
        idx = hash(key) % self.m
        for _ in range(self.m):
            if self.table[idx] is EMPTY or self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
            idx = (idx + 1) % self.m
        raise Exception("bang day")

    def get(self, key):
        idx = hash(key) % self.m
        for _ in range(self.m):
            if self.table[idx] is EMPTY:
                return None
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.m
        return None


def compare_performance(num_keys, m):
    keys = [f"key{i}" for i in range(num_keys)]

    t1 = time.time()
    ht_chain = HashTableChaining(m)
    for k in keys:
        ht_chain.put(k, 1)
    for k in keys:
        ht_chain.get(k)
    time_chain = time.time() - t1

    t2 = time.time()
    ht_probe = HashTableLinearProbing(m)
    for k in keys:
        ht_probe.put(k, 1)
    for k in keys:
        ht_probe.get(k)
    time_probe = time.time() - t2

    return time_chain, time_probe, num_keys / m


if __name__ == "__main__":
    for num_keys, m in [(500, 1024), (900, 1024), (1000, 1024)]:
        tc, tp, load = compare_performance(num_keys, m)
        print(f"load={load:.2f}  chaining={tc*1000:.2f}ms  probing={tp*1000:.2f}ms")
