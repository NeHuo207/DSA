'''
Câu 4 (Ứng dụng Ngăn xếp - Stack)
Cho mảng biểu diễn nhiệt độ trong các ngày liên tiếp T = [73, 74, 75, 71, 69, 72, 76, 73]. Trình bày cách sử dụng Ngăn xếp đơn điệu (Monotonic Stack) để đếm số ngày ít nhất phải chờ để có một ngày ấm hơn (nhiệt độ cao hơn) cho mỗi ngày. Nếu không có ngày nào trong tương lai thỏa mãn, trả về 0. Cung cấp mảng kết quả cuối cùng.
'''
def daily_temperatures(T):
    n = len(T)
    result = [0] * n
    stack = []  # lưu index

    for i in range(n):
        while stack and T[i] > T[stack[-1]]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)

    return result

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(T))