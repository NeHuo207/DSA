def heap_sort(a):
    """
    Selection Sort: mỗi vòng tìm min trong O(n) → tổng O(n²)
    Heap Sort: mỗi vòng lấy min từ heap trong O(log n) → tổng O(n log n)
    Cả hai đều có O(n) "vòng chọn" và O(1) swap mỗi vòng.
    """
    import heapq
    h = a[:]
    heapq.heapify(h)  # O(n)
    return [heapq.heappop(h) for _ in range(len(h))]  # O(n log n)
 
arr = [5, 3, 8, 1, 9, 2]
print(f"Bài 20: heap_sort={heap_sort(arr)}")