def dedup_slow(arr):
    result = []
    for x in arr:
        if x not in result:
            result.append(x)
    return result


def dedup_fast(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


a = [3, 1, 3, 2, 1]
print(f"  {a} -> slow: {dedup_slow(a)}, fast: {dedup_fast(a)}")
