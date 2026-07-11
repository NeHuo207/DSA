import random
import heapq
import time
 
def partial_selection_k(a, k):
    b = a[:]
    n = len(b)
    for i in range(k):
        mi = i
        for j in range(i + 1, n):
            if b[j] < b[mi]: mi = j
        b[i], b[mi] = b[mi], b[i]
    return b[:k]
 
def heap_k_smallest(a, k):
    return heapq.nsmallest(k, a)  # O(n + k log n)
 
# Thử với n lớn
n = 10000
a = random.sample(range(n * 10), n)
 
k_small = 5
t0 = time.time()
r1 = partial_selection_k(a, k_small)
t1 = time.time()
r2 = heap_k_smallest(a, k_small)
t2 = time.time()
 
print(f"Bài 24 (k={k_small}, n={n}):")
print(f"  partial selection : {(t1-t0)*1000:.2f} ms, result={sorted(r1)}")
print(f"  heap nsmallest    : {(t2-t1)*1000:.2f} ms, result={r2}")
 
k_large = 5000
t0 = time.time()
r1 = partial_selection_k(a, k_large)
t1 = time.time()
r2 = heap_k_smallest(a, k_large)
t2 = time.time()
print(f"  (k={k_large}): partial={( t1-t0)*1000:.1f}ms, heap={(t2-t1)*1000:.1f}ms → heap thắng khi k lớn")