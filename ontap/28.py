from collections import deque


def bfs(adj, start):
    visited = set([start])
    q = deque([start])
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)

    return order


def bfs_levels(adj, start):
    visited = set([start])
    q = deque([(start, 0)])
    levels = {}

    while q:
        u, lv = q.popleft()
        levels.setdefault(lv, []).append(u)
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                q.append((v, lv + 1))

    return levels


if __name__ == "__main__":
    adj = {
        0: [1, 2],
        1: [3, 4],
        2: [5],
        3: [],
        4: [5],
        5: [],
    }
    print(bfs(adj, 0))
    for lv, nodes in bfs_levels(adj, 0).items():
        print(f"tang {lv}: {nodes}")
