import random
def is_stats(a):
    b = a[:]; cmps = shifts = 0
    for i in range(1, len(b)):
        key = b[i]; j = i - 1
        while j >= 0:
            cmps += 1
            if b[j] > key:
                b[j + 1] = b[j]; j -= 1; shifts += 1
            else:
                break
        b[j + 1] = key
    return cmps, shifts
 
n = 8
best  = list(range(1, n + 1))
worst = list(range(n, 0, -1))
avg   = random.sample(range(1, n + 1), n)
 
bc, bs = is_stats(best)
wc, ws = is_stats(worst)
ac, as_ = is_stats(avg)
 
print("Bài 23:")
print(f"  {'Case':<10} {'Comparisons':<14} {'Shifts'}")
print(f"  {'Best':<10} {bc:<14} {bs}")
print(f"  {'Average':<10} {ac:<14} {as_}")
print(f"  {'Worst':<10} {wc:<14} {ws}")
# Best: O(n)-1 cmp, 0 shift | Worst: n(n-1)/2 cmp & shift