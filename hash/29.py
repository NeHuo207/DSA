import random
import math


class BloomFilter:
    def __init__(self, m=1000, k=3):
        self.m = m
        self.k = k
        self.bits = [0] * m
        self.seeds = [random.randint(1, 10**6) for _ in range(k)]

    def _hashes(self, x):
        for seed in self.seeds:
            yield hash(str(x) + str(seed)) % self.m

    def add(self, x):
        for idx in self._hashes(x):
            self.bits[idx] = 1

    def might_contain(self, x):
        for idx in self._hashes(x):
            if self.bits[idx] == 0:
                return False
        return True

    def false_positive_rate(self, n):
        return (1 - math.exp(-self.k * n / self.m)) ** self.k


if __name__ == "__main__":
    bf = BloomFilter(m=1000, k=3)

    added = [f"item{i}" for i in range(100)]
    for x in added:
        bf.add(x)

    print(bf.might_contain("item5"))
    print(bf.might_contain("item50"))
    print(bf.might_contain("item999"))

    not_added = [f"other{i}" for i in range(1000)]
    false_pos = sum(1 for x in not_added if bf.might_contain(x))
    print(f"duong tinh gia thuc te: {false_pos}/1000 = {false_pos/10:.1f}%")
    print(f"ly thuyet: {bf.false_positive_rate(100)*100:.1f}%")

    print(f"\nk khac nhau (n=100, m=1000):")
    for k in [1, 2, 3, 5, 7, 10]:
        bf2 = BloomFilter(m=1000, k=k)
        print(f"  k={k}: {bf2.false_positive_rate(100)*100:.2f}%")
