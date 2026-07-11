EMPTY = object()
DELETED = object()


class HashTableLinearProbing:
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


if __name__ == "__main__":
    ht = HashTableLinearProbing(8)
    ht.put("x", 10)
    ht.put("y", 20)
    ht.put("z", 30)
    print(ht.get("x"))
    print(ht.get("y"))
    print(ht.get("w"))
