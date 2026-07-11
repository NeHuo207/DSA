class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.n = 0
        self.modCount = 0

    def add(self, x):
        if self.n == self.capacity:
            self._resize(self.capacity * 2)
        self.arr[self.n] = x
        self.n += 1
        self.modCount += 1

    def get(self, i):
        if not (0 <= i < self.n):
            raise IndexError("chỉ số ngoài phạm vi")
        return self.arr[i]

    def set(self, i, x):
        if not (0 <= i < self.n):
            raise IndexError("chỉ số ngoài phạm vi")
        self.arr[i] = x

    def size(self):
        return self.n

    def count_matching(self, condition):
        count = 0
        for i in range(self.n):
            print(self.arr[i], end=" ")
            if condition(self.arr[i]):
                count += 1
        print()
        return count

    def to_list(self):
        return [self.arr[i] for i in range(self.n)]


lst4 = ArrayList()
for x in [1, 2, 3, 4]:
    lst4.add(x)
print(f"  số chẵn = {lst4.count_matching(lambda v: v % 2 == 0)}")
