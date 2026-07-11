import random


class UniversalHash:
    def __init__(self, m, p=(1 << 31) - 1):
        self.m = m
        self.p = p
        self.a = random.randint(1, p - 1)
        self.b = random.randint(0, p - 1)

    def hash(self, k):
        return ((self.a * k + self.b) % self.p) % self.m


if __name__ == "__main__":
    uh1 = UniversalHash(m=100)
    uh2 = UniversalHash(m=100)

    print(f"instance 1: a={uh1.a}, b={uh1.b}")
    print(f"instance 2: a={uh2.a}, b={uh2.b}")

    for k in [42, 100, 7]:
        print(f"k={k}: instance1 -> {uh1.hash(k)}, instance2 -> {uh2.hash(k)}")

    uh = UniversalHash(m=10)
    buckets = {}
    for k in range(1000):
        idx = uh.hash(k)
        buckets[idx] = buckets.get(idx, 0) + 1
    print(f"phan bo 1000 khoa vao 10 bucket: {sorted(buckets.values())}")
