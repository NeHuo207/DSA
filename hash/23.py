def hash_sum(s, m):
    total = 0
    for ch in s:
        total += ord(ch)
    return total % m


def polynomial_hash(s, p=31, m=10**9 + 9):
    h = 0
    for ch in s:
        h = (h * p + ord(ch)) % m
    return h


def chi_square_test(keys, hash_func, m):
    observed = [0] * m
    for k in keys:
        observed[hash_func(k) % m] += 1

    expected = len(keys) / m
    chi2 = sum((obs - expected) ** 2 / expected for obs in observed)
    return chi2, observed


if __name__ == "__main__":
    keys = [f"key{i}" for i in range(100)]
    m = 50

    chi1, obs1 = chi_square_test(keys, lambda k: hash_sum(k, 10**9), m)
    chi2, obs2 = chi_square_test(keys, lambda k: polynomial_hash(k), m)

    print(f"hash_sum:   chi2 = {chi1:.1f}")
    print(f"polynomial: chi2 = {chi2:.1f}")
    print(f"ly tuong:   chi2 ~ {m}")
