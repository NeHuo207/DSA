class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.n = 0

    def _resize(self, new_cap):
        new_arr = [None] * new_cap
        for i in range(self.n):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_cap

    def append(self, x):
        if self.n == self.capacity:
            self._resize(self.capacity * 2)
        self.arr[self.n] = x
        self.n += 1

    def get(self, i):
        if not (0 <= i < self.n):
            raise IndexError("ngoai pham vi")
        return self.arr[i]

    def size(self):
        return self.n

    def to_list(self):
        return [self.arr[i] for i in range(self.n)]


def count_copies(num_appends):
    lst = ArrayList()
    total = 0
    for i in range(num_appends):
        if lst.n == lst.capacity:
            total += lst.n
        lst.append(i)
    return total


if __name__ == "__main__":
    lst = ArrayList()
    for x in [1, 2, 3, 4, 5]:
        lst.append(x)
    print(lst.to_list(), lst.size(), lst.capacity)

    print("\nkiem chung amortized O(1):")
    for n in [10, 100, 1000, 10000]:
        c = count_copies(n)
        print(f"n={n:>5}: {c:>6} copy  (< 2n={2*n})  = {c/n:.2f} copy/append")
