def search_matrix(matrix, x):
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]
        if   val == x: return True
        elif val < x:  lo = mid + 1
        else: hi = mid - 1
    return False
print(search_matrix([[1,3,5],[7,9,11]],9))