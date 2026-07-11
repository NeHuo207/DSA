def hash_2d_search(matrix, pattern):
    m, n = len(matrix), len(matrix[0])
    p, q = len(pattern), len(pattern[0])
    if p > m or q > n:
        return None

    P1, P2, MOD = 31, 53, 10**9 + 9

    def hash_row_window(row, start, width):
        h = 0
        for j in range(start, start + width):
            h = (h * P1 + row[j]) % MOD
        return h

    def hash_col(values):
        h = 0
        for v in values:
            h = (h * P2 + v) % MOD
        return h

    pattern_row_hashes = [hash_row_window(r, 0, q) for r in pattern]
    pattern_hash = hash_col(pattern_row_hashes)

    for j in range(n - q + 1):
        row_hashes = [hash_row_window(matrix[i], j, q) for i in range(m)]
        for i in range(m - p + 1):
            window_hash = hash_col(row_hashes[i : i + p])
            if window_hash == pattern_hash:
                match = all(
                    matrix[i + di][j + dj] == pattern[di][dj]
                    for di in range(p)
                    for dj in range(q)
                )
                if match:
                    return (i, j)
    return None


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 1, 2, 3],
    ]

    pattern1 = [
        [6, 7],
        [1, 2],
    ]
    print(hash_2d_search(matrix, pattern1))

    pattern2 = [
        [2, 3],
        [6, 7],
    ]
    print(hash_2d_search(matrix, pattern2))

    pattern3 = [
        [99, 99],
        [99, 99],
    ]
    print(hash_2d_search(matrix, pattern3))
