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

    def indexOf(self, target):
        for i in range(self.n):
            if self.arr[i] == target:
                return i
        return -1


lst3 = ArrayList()
for x in [5, 3, 7]:
    lst3.add(x)
print(f"  [5,3,7] tìm 7 -> idx {lst3.indexOf(7)}")
print(f"  tìm 100 -> {lst3.indexOf(100)}")
