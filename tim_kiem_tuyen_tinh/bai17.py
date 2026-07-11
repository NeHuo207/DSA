def linear_search_sentinel(a, x):
    n = len(a)
    # Tạm thời thêm x vào cuối mảng làm lính canh
    a.append(x)
    
    i = 0
    while a[i] != x:
        i += 1
        
    # Xóa lính canh đi để trả lại mảng ban đầu
    a.pop()
    
    # Nếu i dừng trước n, nghĩa là tìm thấy phần tử thực sự trong mảng
    if i < n:
        return i
    return -1