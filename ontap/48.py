def polynomial_hash(s, p=31, m=10**9 + 9):
    h = 0
    for ch in s:
        h = (h * p + ord(ch)) % m
    return h


def rabin_karp(text, pattern, p=31, mod=10**9 + 9):
    n, m = len(text), len(pattern)
    if m > n:
        return -1

    pattern_hash = polynomial_hash(pattern, p, mod)
    window_hash = polynomial_hash(text[:m], p, mod)
    p_pow = pow(p, m - 1, mod)

    for i in range(n - m + 1):
        if window_hash == pattern_hash:
            if text[i : i + m] == pattern:
                return i
        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * p_pow) % mod
            window_hash = (window_hash * p + ord(text[i + m])) % mod

    return -1


def rabin_karp_all(text, pattern, p=31, mod=10**9 + 9):
    n, m = len(text), len(pattern)
    if m > n:
        return []

    pattern_hash = polynomial_hash(pattern, p, mod)
    window_hash = polynomial_hash(text[:m], p, mod)
    p_pow = pow(p, m - 1, mod)
    result = []

    for i in range(n - m + 1):
        if window_hash == pattern_hash and text[i : i + m] == pattern:
            result.append(i)
        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * p_pow) % mod
            window_hash = (window_hash * p + ord(text[i + m])) % mod

    return result


if __name__ == "__main__":
    print(rabin_karp("zabcd", "abc"))
    print(rabin_karp("hello world", "world"))
    print(rabin_karp("zabcd", "xyz"))
    print(rabin_karp_all("ababab", "ab"))
