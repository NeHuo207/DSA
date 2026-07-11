class LRUNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = LRUNode(None, None)
        self.tail = LRUNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.map) == self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.map[lru.key]
            node = LRUNode(key, value)
            self._add_to_front(node)
            self.map[key] = node


cache = LRUCache(2)
cache.put(1, 100)
cache.put(2, 200)
print(f"  get(1) = {cache.get(1)}")
cache.put(3, 300)
print(f"  put(3) xong, get(2) = {cache.get(2)}")
print(f"  get(3) = {cache.get(3)}")
