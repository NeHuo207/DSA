def count_subarrays_sum_k(a, k):
    prefix_count = {0: 1}
    prefix_sum = 0
    count = 0

    for x in a:
        prefix_sum += x
        if (prefix_sum - k) in prefix_count:
            count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count


if __name__ == "__main__":
    print(count_subarrays_sum_k([1, 1, 1], 2))
    print(count_subarrays_sum_k([1, 2, 3], 3))
    print(count_subarrays_sum_k([1, -1, 0], 0))
