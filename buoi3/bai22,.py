def insertion_sort_k_offset(a, k):
    """
    Khi mỗi phần tử cách đúng vị trí ≤ k,
    vòng while trong chạy tối đa k lần → O(n·k)
    """
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            shifts += 1
        a[j + 1] = key
    return a, shifts
 
# Tạo mảng k-bounded đúng cách: hoán đổi ngẫu nhiên trong phạm vi k
import random
k = 3
base = list(range(20))
nearly = base[:]
for _ in range(15):  # Một số swap nhỏ, mỗi cái trong khoảng k
    i = random.randint(0, len(nearly) - k - 1)
    j = i + random.randint(1, k)
    nearly[i], nearly[j] = nearly[j], nearly[i]
 
arr, sh = insertion_sort_k_offset(nearly[:], k)
print(f"Bài 22: sorted={arr == sorted(nearly)}, shifts={sh} (expected ≤ {len(nearly)*k})")