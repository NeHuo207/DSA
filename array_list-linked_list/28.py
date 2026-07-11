def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda iv: iv[0])
    result = [intervals[0][:]]
    for start, end in intervals[1:]:
        last = result[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            result.append([start, end])
    return result


iv = [[1, 3], [2, 6], [8, 10]]
print(f"  {iv} -> {merge_intervals(iv)}")
