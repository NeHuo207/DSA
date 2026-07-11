def polynomial_hash(s, p=31, m=10**9 + 9):
    h = 0
    for ch in s:
        h = (h * p + ord(ch)) % m
    return h


if __name__ == "__main__":
    print(polynomial_hash("abc"))
    print(polynomial_hash("cba"))
    print(polynomial_hash("bac"))

    words = ["listen", "silent", "enlist"]
    for w in words:
        print(f"{w}: {polynomial_hash(w)}")
