def hash_sum(s, m):
    total = 0
    for ch in s:
        total += ord(ch)
    return total % m


if __name__ == "__main__":
    m = 100
    print(hash_sum("abc", m))
    print(hash_sum("cba", m))
    print(hash_sum("bac", m))

    words = ["listen", "silent", "enlist"]
    for w in words:
        print(f"{w}: {hash_sum(w, m)}")
