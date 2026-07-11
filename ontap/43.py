class HashTableWithRehash:
    def __init__(self, m=4, threshold=0.75):
        self.m = m
        self.threshold = threshold
        self.buckets = [[] for _ in range(m)]
        self.n = 0
        self.rehash_count = 0

    def _hash(self, key):
        return hash(key) % self.m

    def load_factor(self):
        return self.n / self.m

    def put(self, key, value):
        if (self.n + 1) / self.m > self.threshold:
            self._rehash()

        idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))
        self.n += 1

    def _rehash(self):
        old = [(k, v) for b in self.buckets for (k, v) in b]
        self.m *= 2
        self.buckets = [[] for _ in range(self.m)]
        self.rehash_count += 1
        for k, v in old:
            self.buckets[self._hash(k)].append((k, v))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return None


if __name__ == "__main__":
    ht = HashTableWithRehash(m=4)
    for i in range(20):
        old_m = ht.m
        ht.put(f"k{i}", i)
        if ht.m != old_m:
            print(f"n={ht.n}: rehash {old_m} -> {ht.m}, load={ht.load_factor():.2f}")

    print(
        f"\ncuoi: m={ht.m}, n={ht.n}, load={ht.load_factor():.2f}, rehash={ht.rehash_count}"
    )
    print(ht.get("k0"), ht.get("k19"))
