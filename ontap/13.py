def count_inversions(a):
    def merge_and_count(left, right):
        result = []
        i = j = 0
        inv = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                inv += len(left) - i
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inv

    def sort_count(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, inv_l = sort_count(a[:mid])
        right, inv_r = sort_count(a[mid:])
        merged, inv_split = merge_and_count(left, right)
        return merged, inv_l + inv_r + inv_split

    _, total = sort_count(a)
    return total


def count_inversions_brute(a):
    inv = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                inv += 1
    return inv


if __name__ == "__main__":
    import random

    for a in [[2, 3, 1], [5, 4, 3, 2, 1], [1, 2, 3]]:
        print(f"{a}: merge={count_inversions(a)}  brute={count_inversions_brute(a)}")

    big = [random.randint(0, 1000) for _ in range(500)]
    print(f"n=500: merge={count_inversions(big)}  brute={count_inversions_brute(big)}")
