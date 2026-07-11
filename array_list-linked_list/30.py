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


class ArrayListIterator:
    def __init__(self, lst: ArrayList):
        self.lst = lst
        self.idx = 0
        self.expected_modCount = lst.modCount

    def hasNext(self):
        return self.idx < self.lst.n

    def next(self):
        if self.lst.modCount != self.expected_modCount:
            raise RuntimeError(
                "ConcurrentModificationException: "
                "danh sách bị sửa đổi trong khi đang duyệt!"
            )
        if not self.hasNext():
            raise StopIteration
        x = self.lst.arr[self.idx]
        self.idx += 1
        return x


lst5 = ArrayList()
for x in [10, 20, 30]:
    lst5.add(x)
it = ArrayListIterator(lst5)
print(f"  next() = {it.next()}")
lst5.add(40)
try:
    it.next()
except RuntimeError as e:
    print(f"  lỗi bắt được: {e}")
