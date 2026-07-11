import time

EMPTY = object()
DELETED = object()


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

    def remove(self, key):
        idx = hash(key) % self.m
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                del self.buckets[idx][i]
                return True
        return False


class HashTableLinearProbing:
    def __init__(self, m=8):
        self.m = m
        self.table = [EMPTY] * m

    def put(self, key, value):
        idx = hash(key) % self.m
        for _ in range(self.m):
            slot = self.table[idx]
            if slot is EMPTY or slot is DELETED:
                self.table[idx] = (key, value)
                return
            if slot[0] == key:
                self.table[idx] = (key, value)
                return
            idx = (idx + 1) % self.m
        raise Exception("bang day")

    def get(self, key):
        idx = hash(key) % self.m
        for _ in range(self.m):
            slot = self.table[idx]
            if slot is EMPTY:
                return None
            if slot is not DELETED and slot[0] == key:
                return slot[1]
            idx = (idx + 1) % self.m
        return None

    def remove(self, key):
        idx = hash(key) % self.m
        for _ in range(self.m):
            slot = self.table[idx]
            if slot is EMPTY:
                return False
            if slot is not DELETED and slot[0] == key:
                self.table[idx] = DELETED
                return True
            idx = (idx + 1) % self.m
        return False


if __name__ == "__main__":
    hc = HashTableChaining()
    hp = HashTableLinearProbing()

    for k, v in [("a", 1), ("b", 2), ("c", 3)]:
        hc.put(k, v)
        hp.put(k, v)

    print(hc.get("b"), hp.get("b"))
    hc.remove("b")
    hp.remove("b")
    print(hc.get("b"), hp.get("b"))
    print(hc.get("c"), hp.get("c"))

    for num_keys, m in [(500, 1024), (1000, 1024)]:
        keys = [f"key{i}" for i in range(num_keys)]

        t1 = time.time()
        h1 = HashTableChaining(m)
        for k in keys:
            h1.put(k, 1)
        for k in keys:
            h1.get(k)
        tc = time.time() - t1

        t2 = time.time()
        h2 = HashTableLinearProbing(m)
        for k in keys:
            h2.put(k, 1)
        for k in keys:
            h2.get(k)
        tp = time.time() - t2

        print(f"load={num_keys/m:.2f}  chain={tc*1000:.1f}ms  probe={tp*1000:.1f}ms")
