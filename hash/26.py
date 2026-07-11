def hash_set_xor(elements):
    total = 0
    for x in elements:
        total ^= hash(x)
    return total


def hash_multiset_sum(elements):
    MOD = 10**9 + 7
    total = 0
    for x in elements:
        total = (total + hash(x)) % MOD
    return total


if __name__ == "__main__":
    print(hash_set_xor(["a", "b", "c"]))
    print(hash_set_xor(["c", "a", "b"]))
    print(hash_set_xor(["b", "c", "a"]))

    print(hash_multiset_sum(["a", "a", "b"]))
    print(hash_multiset_sum(["a", "b", "a"]))

    print(hash_set_xor(["a", "a", "b"]))
    print(hash_set_xor(["b"]))
