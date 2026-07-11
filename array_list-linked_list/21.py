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


if __name__ == "__main__":
    lst = ArrayList()
    print(f"khởi tạo: size = {lst.size()}, capacity = {lst.capacity}")

    for x in [1, 2, 3, 4]:
        lst.add(x)
    print(f"sau 4 phần tử: size = {lst.size()}, capacity = {lst.capacity}")

    lst.add(5)
    print(f"sau 5 phần tử: size = {lst.size()}, capacity = {lst.capacity}")
    print(f"list = {lst.to_list()}")

    for x in [6, 7, 8, 9]:
        lst.add(x)
    print(f"sau 9 phần tử: size = {lst.size()}, capacity = {lst.capacity}")
