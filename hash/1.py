class HashTableChaining:
    def __init__(self, m=8):
        self.m = m
        self.buckets = [[] for _ in range(m)]
        self.n = 0

    def _hash(self, key):
        return hash(key) % self.m

    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))
        self.n += 1

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return None

    def remove(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                del self.buckets[idx][i]
                self.n -= 1
                return True
        return False


if __name__ == "__main__":
    ht = HashTableChaining()
    ht.put("a", 1)
    ht.put("b", 2)
    print(ht.get("a"))
    print(ht.get("b"))
    ht.remove("a")
    print(ht.get("a"))
