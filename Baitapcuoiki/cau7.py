'''
Câu 7 (Bảng băm & Mảng cộng dồn)
Cho mảng số nguyên A = [3, 4, 7, 2, -3, 1, 4, 2] và mục tiêu S = 7. Việc dùng 2 vòng lặp lồng nhau để đếm mảng con có tổng bằng S sẽ tốn O(N^2). Hãy trình bày phương pháp tối ưu hơn sử dụng Bảng băm (Hash Map) kết hợp Mảng cộng dồn (Prefix Sum) để giải quyết trong O(N). Có bao nhiêu mảng con thỏa mãn trong mảng A đã cho?
'''
def count_subarray_sum(A, S):
    prefix_count = {0: 1}
    prefix_sum = 0
    count = 0

    for x in A:
        prefix_sum += x
        if (prefix_sum - S) in prefix_count:
            count += prefix_count[prefix_sum - S]
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count

A7 = [3, 4, 7, 2, -3, 1, 4, 2]
S = 7
print(count_subarray_sum(A7,S))