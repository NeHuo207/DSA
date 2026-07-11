def polynomial_hash(s, p=31, m=10**9 + 9):
    h = 0
    for ch in s:
        h = (h * p + ord(ch)) % m
    return h


def hash_sum(s, m):
    total = 0
    for ch in s:
        total += ord(ch)
    return total % m


if __name__ == "__main__":
    print(polynomial_hash("abc"))
    print(polynomial_hash("cba"))

    print(f"\nhash_sum (nhuoc diem):")
    print(f"  abc={hash_sum('abc', 10**9)}  cba={hash_sum('cba', 10**9)}")

    print(f"\npolynomial (khac phuc):")
    print(f"  abc={polynomial_hash('abc')}  cba={polynomial_hash('cba')}")

    print(f"\np khac nhau:")
    for p in [2, 31, 53]:
        print(f"  p={p}: abc={polynomial_hash('abc', p)}")
