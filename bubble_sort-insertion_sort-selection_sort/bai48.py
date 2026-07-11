import random
def ss_stats(a):
    b = a[:]; cmps = swaps = 0
    n = len(b)
    for i in range(n):
        mi = i
        for j in range(i + 1, n):
            cmps += 1
            if b[j] < b[mi]: mi = j
        if mi != i:
            b[i], b[mi] = b[mi], b[i]
            swaps += 1
    return cmps, swaps
 
n = 8
best  = list(range(1, n + 1))
worst = list(range(n, 0, -1))
avg   = random.sample(range(1, n + 1), n)
 
bc, bs = ss_stats(best)
wc, ws = ss_stats(worst)
ac, as_ = ss_stats(avg)
 
print("Bài 23:")
print(f"  {'Case':<10} {'Comparisons':<14} {'Swaps'}")
print(f"  {'Best':<10} {bc:<14} {bs}")
print(f"  {'Average':<10} {ac:<14} {as_}")
print(f"  {'Worst':<10} {wc:<14} {ws}")
# So sánh luôn n(n-1)/2; swap: 0 (best) đến n-1 (worst)