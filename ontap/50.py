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

    print("da them -> luon True (khong am tinh gia):")
    print(f"  item0={bf.might_contain('item0')}  item99={bf.might_contain('item99')}")

    print("\nchua them -> co the True (duong tinh gia):")
    not_added = [f"other{i}" for i in range(1000)]
    fp = sum(1 for x in not_added if bf.might_contain(x))
    print(f"  {fp}/1000 = {fp/10:.1f}% duong tinh gia")
    print(f"  ly thuyet: {bf.false_positive_rate(100)*100:.1f}%")

    print("\nk thay doi (n=100, m=1000):")
    for k in [1, 2, 3, 5, 7, 10]:
        b = BloomFilter(m=1000, k=k)
        print(f"  k={k:>2}: {b.false_positive_rate(100)*100:.2f}%")
