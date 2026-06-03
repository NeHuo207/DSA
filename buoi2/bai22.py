def median_two_arrays(a, b):
    if len(a) > len(b): a, b = b, a   # đảm bảo a là mảng ngắn hơn
    m, n = len(a), len(b)
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2           # cắt a tại i
        j = (m + n + 1) // 2 - i    # cắt b tại j
        maxL_a = float('-inf') if i==0 else a[i-1]
        minR_a = float('inf')  if i==m else a[i]
        maxL_b = float('-inf') if j==0 else b[j-1]
        minR_b = float('inf')  if j==n else b[j]
        if maxL_a <= minR_b and maxL_b <= minR_a:
            if (m+n) % 2: return max(maxL_a, maxL_b)
            return (max(maxL_a,maxL_b)+min(minR_a,minR_b)) / 2
        elif maxL_a > minR_b: hi = i - 1
        else: lo = i + 1
print(median_two_arrays([1,3],[2]))