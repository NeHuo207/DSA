import random


class UniversalHash:
    def __init__(self, m, p=(1 << 31) - 1):
        self.m = m
        self.p = p
        self.a = random.randint(1, p - 1)
        self.b = random.randint(0, p - 1)

    def hash(self, k):
        return ((self.a * k + self.b) % self.p) % self.m


def fixed_hash(k, m):
    return k % m


if __name__ == "__main__":
    m = 10

    print("hash co dinh h(k) = k mod 10:")
    evil_keys = [i * m for i in range(20)]
    buckets = {}
    for k in evil_keys:
        idx = fixed_hash(k, m)
        buckets[idx] = buckets.get(idx, 0) + 1
    print(f"  khoa tan cong -> bucket lon nhat: {max(buckets.values())}/20")

    print("\nuniversal hashing (a,b ngau nhien):")
    uh = UniversalHash(m)
    buckets2 = {}
    for k in evil_keys:
        idx = uh.hash(k)
        buckets2[idx] = buckets2.get(idx, 0) + 1
    print(f"  cung khoa do -> bucket lon nhat: {max(buckets2.values())}/20")

    print("\n2 instance khac nhau, cung khoa k=42:")
    for i in range(3):
        u = UniversalHash(100)
        print(
            f"  instance {i+1}: a={u.a % 10000}, b={u.b % 10000} -> h(42)={u.hash(42)}"
        )
