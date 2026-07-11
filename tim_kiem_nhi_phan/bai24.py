import math

def min_max_gap(x, k):
    def feasible(d):
        # Số trạm cần thêm để mọi gap ≤ d
        return sum(math.ceil((x[i]-x[i-1])/d)-1
                    for i in range(1,len(x))) <= k

    lo, hi = 0.0, x[-1] - x[0]
    for _ in range(100):    # 100 vòng → độ chính xác ~10⁻³⁰
        mid = (lo + hi) / 2
        if feasible(mid): hi = mid
        else:             lo = mid
    return round(lo, 6)
print(min_max_gap([1,2,3,4,5,6,7,8,9,10],9))