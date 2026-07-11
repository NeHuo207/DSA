def merge_intervals(intervals):
    if not intervals:
        return []

    intervals = sorted(intervals, key=lambda iv: iv[0])
    result = [list(intervals[0])]

    for start, end in intervals[1:]:
        last = result[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            result.append([start, end])

    return result


if __name__ == "__main__":
    print(merge_intervals([[1, 3], [2, 6], [8, 10]]))
    print(merge_intervals([[1, 4], [4, 5]]))
    print(merge_intervals([[1, 2], [3, 4]]))
