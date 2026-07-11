EMPTY = object()
DELETED = object()


class HashTableLazyDelete:
    def __init__(self, m=8):
        self.m = m
        self.table = [EMPTY] * m
        self.n = 0

    def _hash(self, key):
        return hash(key) % self.m

    def put(self, key, value):
        idx = self._hash(key)
        for _ in range(self.m):
            slot = self.table[idx]
            if slot is EMPTY or slot is DELETED:
                self.table[idx] = (key, value)
                self.n += 1
                return
            if slot[0] == key:
                self.table[idx] = (key, value)
                return
            idx = (idx + 1) % self.m
        raise Exception("bang day")

    def get(self, key):
        idx = self._hash(key)
        for _ in range(self.m):
            slot = self.table[idx]
            if slot is EMPTY:
                return None
            if slot is not DELETED and slot[0] == key:
                return slot[1]
            idx = (idx + 1) % self.m
        return None

    def remove(self, key):
        idx = self._hash(key)
        for _ in range(self.m):
            slot = self.table[idx]
            if slot is EMPTY:
                return False
            if slot is not DELETED and slot[0] == key:
                self.table[idx] = DELETED
                self.n -= 1
                return True
            idx = (idx + 1) % self.m
        return False

    def count_tombstones(self):
        return sum(1 for slot in self.table if slot is DELETED)

    def compact(self):
        entries = [s for s in self.table if s is not EMPTY and s is not DELETED]
        self.table = [EMPTY] * self.m
        self.n = 0
        for k, v in entries:
            self.put(k, v)


if __name__ == "__main__":
    ht = HashTableLazyDelete(8)
    for k in ["a", "b", "c", "d"]:
        ht.put(k, k.upper())

    ht.remove("b")
    print(ht.get("b"))
    print(ht.get("c"))
    print(ht.count_tombstones())

    ht.compact()
    print(ht.count_tombstones())
    print(ht.get("c"))
