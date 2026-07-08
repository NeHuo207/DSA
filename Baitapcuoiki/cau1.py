'''
Câu 1 (Chia mảng - Ứng dụng Tìm kiếm Nhị phân)
Một công ty vận tải cần giao các kiện hàng có khối lượng lần lượt là W = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Công ty chỉ có K = 5 xe tải, và mỗi xe chỉ được chở các kiện hàng xếp liên tiếp nhau trong danh sách. Hãy dùng thuật toán tìm kiếm nhị phân để xác định tải trọng tối thiểu của một chiếc xe sao cho có thể chở hết tất cả kiện hàng trong một lượt. Giải thích cách chia kiện hàng cho 5 xe với tải trọng tìm được.
'''
w = [1,2,3,4,5,6,7,8,9,10]
k = 5
def BinarySearch():
    def canDeliver(W, capacity,K):
        needed = 1
        currentload = 0
        for w in W:
            if currentload + w > capacity:
                needed += 1
                currentload = w
                if needed > K:
                    return False
            else:
                currentload += w
        return True
    def minCapacity(W,K):
        low = max(W)
        high = sum(W)
        while low < high:
            mid = (low+high)//2
            if canDeliver(W,mid,K):
                high = mid
            else:
                low = mid+1
        return low
    return minCapacity(w,k)

print(BinarySearch())