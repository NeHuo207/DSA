def online_insertion_sort(stream):
    result = []
    for x in stream:
        result.append(x)
        i = len(result) - 1
        while i > 0 and result[i - 1] > result[i]:
            result[i - 1], result[i] = result[i], result[i - 1]
            i -= 1
        print(f"  Thêm {x}: {result[:]}")
    return result
 
print("Bài 16:")
online_insertion_sort([5, 2, 8, 1])