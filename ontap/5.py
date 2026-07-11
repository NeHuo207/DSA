import math


def min_eating_speed(piles, h):
    def hours_needed(speed):
        return sum(math.ceil(p / speed) for p in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    print(min_eating_speed([3, 6, 7, 11], 8))
    print(min_eating_speed([30, 11, 23, 4, 20], 5))
    print(min_eating_speed([30, 11, 23, 4, 20], 6))
