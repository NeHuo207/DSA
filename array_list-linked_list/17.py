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

    def _resize(self, new_cap):
        new_arr = [None] * new_cap
        for i in range(self.n):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_cap

    def to_list(self):
        return [self.arr[i] for i in range(self.n)]

    def append(self, x):
        self.add(x)

    def popBack(self):
        if self.n == 0:
            raise IndexError("danh sách rỗng")
        x = self.arr[self.n - 1]
        self.arr[self.n - 1] = None
        self.n -= 1
        self.modCount += 1
        return x


if __name__ == "__main__":
    lst = ArrayList()
    for x in [1, 2, 3]:
        lst.append(x)
    print(f"sau append 1,2,3 -> {lst.to_list()}")
    x = lst.popBack()
    print(f"popBack() = {x} -> {lst.to_list()}")
