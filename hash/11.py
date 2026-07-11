class MyHashSet:
    def __init__(self, m=8):
        self.m = m
        self.buckets = [[] for _ in range(m)]
        self.n = 0

    def _hash(self, x):
        return hash(x) % self.m

    def add(self, x):
        idx = self._hash(x)
        if x not in self.buckets[idx]:
            self.buckets[idx].append(x)
            self.n += 1

    def contains(self, x):
        idx = self._hash(x)
        return x in self.buckets[idx]

    def remove(self, x):
        idx = self._hash(x)
        if x in self.buckets[idx]:
            self.buckets[idx].remove(x)
            self.n -= 1
            return True
        return False

    def size(self):
        return self.n


if __name__ == "__main__":
    hs = MyHashSet()
    hs.add(1)
    hs.add(1)
    hs.add(2)
    print(hs.size())
    print(hs.contains(1), hs.contains(3))
    hs.remove(1)
    print(hs.size(), hs.contains(1))
