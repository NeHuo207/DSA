def split_array_min_largest_sum(a, k):
    def can_split(max_sum):
        segments = 1
        cur_sum = 0
        for x in a:
            if cur_sum + x > max_sum:
                segments += 1
                cur_sum = x
            else:
                cur_sum += x
        return segments <= k

    lo, hi = max(a), sum(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_split(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    print(split_array_min_largest_sum([7, 2, 5, 10, 8], 2))
    print(split_array_min_largest_sum([1, 2, 3, 4, 5], 2))
    print(split_array_min_largest_sum([1, 4, 4], 3))
