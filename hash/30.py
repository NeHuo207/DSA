import random


class MinHash:
    def __init__(self, num_hashes=100):
        self.num_hashes = num_hashes
        self.seeds = [random.randint(1, 10**6) for _ in range(num_hashes)]

    def signature(self, s):
        sig = []
        for seed in self.seeds:
            min_val = min(hash(str(x) + str(seed)) for x in s)
            sig.append(min_val)
        return sig

    def estimate_jaccard(self, set_a, set_b):
        sig_a = self.signature(set_a)
        sig_b = self.signature(set_b)
        matches = sum(1 for x, y in zip(sig_a, sig_b) if x == y)
        return matches / self.num_hashes


def true_jaccard(a, b):
    return len(a & b) / len(a | b)


if __name__ == "__main__":
    A = set(range(0, 100))
    B = set(range(50, 150))

    print(f"Jaccard that:  {true_jaccard(A, B):.4f}")

    for num_hashes in [10, 50, 100, 200, 500]:
        mh = MinHash(num_hashes=num_hashes)
        est = mh.estimate_jaccard(A, B)
        err = abs(est - true_jaccard(A, B))
        print(f"  {num_hashes:>3} hash: uoc luong = {est:.4f}, sai so = {err:.4f}")

    C = set(range(0, 100))
    D = set(range(0, 100))
    mh = MinHash(200)
    print(
        f"\n2 tap giong het: that = {true_jaccard(C, D):.2f}, uoc luong = {mh.estimate_jaccard(C, D):.2f}"
    )

    E = set(range(0, 50))
    F = set(range(100, 150))
    print(
        f"2 tap roi nhau:  that = {true_jaccard(E, F):.2f}, uoc luong = {mh.estimate_jaccard(E, F):.2f}"
    )
