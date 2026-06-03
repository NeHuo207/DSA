def kth_in_matrix(matrix, k):
    n = len(matrix)
    lo, hi = matrix[0][0], matrix[n-1][n-1]
    while lo < hi:
        mid = (lo + hi) // 2
        # Đếm số phần tử ≤ mid (dùng kỹ thuật con trỏ chéo)
        count, j = 0, n - 1
        for i in range(n):
            while j >= 0 and matrix[i][j] > mid: j -= 1
            count += j + 1
        if count < k: lo = mid + 1
        else: hi = mid
    return lo
print(kth_in_matrix([[1,5,9],[10,11,13],[12,13,15]],8))