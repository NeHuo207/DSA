import bisect


class ConsistentHashRing:
    def __init__(self, num_virtual_nodes=100):
        self.num_vnodes = num_virtual_nodes
        self.ring = []
        self.node_map = {}

    def _hash(self, s):
        return hash(s) % (2**32)

    def add_server(self, server):
        for i in range(self.num_vnodes):
            pos = self._hash(f"{server}#{i}")
            bisect.insort(self.ring, pos)
            self.node_map[pos] = server

    def remove_server(self, server):
        for i in range(self.num_vnodes):
            pos = self._hash(f"{server}#{i}")
            if pos in self.node_map:
                self.ring.remove(pos)
                del self.node_map[pos]

    def get_server(self, key):
        if not self.ring:
            return None
        pos = self._hash(key)
        i = bisect.bisect_right(self.ring, pos)
        if i == len(self.ring):
            i = 0
        return self.node_map[self.ring[i]]


if __name__ == "__main__":
    ring = ConsistentHashRing(num_virtual_nodes=100)
    for s in ["server1", "server2", "server3"]:
        ring.add_server(s)

    keys = [f"user{i}" for i in range(1000)]
    before = {k: ring.get_server(k) for k in keys}

    ring.add_server("server4")
    after = {k: ring.get_server(k) for k in keys}

    moved = sum(1 for k in keys if before[k] != after[k])
    print(f"them server4: {moved}/1000 key di chuyen = {moved/10:.1f}%")

    ring.remove_server("server4")
    after2 = {k: ring.get_server(k) for k in keys}
    moved2 = sum(1 for k in keys if after[k] != after2[k])
    print(f"xoa server4: {moved2}/1000 key di chuyen = {moved2/10:.1f}%")
