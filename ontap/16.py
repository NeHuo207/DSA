import heapq


def dijkstra_with_parent(adj, n, s):
    INF = float("inf")
    dist = [INF] * n
    dist[s] = 0
    parent = [-1] * n
    visited = [False] * n
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, parent


def reconstruct_path(parent, s, t):
    path = []
    cur = t
    while cur != -1:
        path.append(cur)
        if cur == s:
            break
        cur = parent[cur]
    path.reverse()
    return path


if __name__ == "__main__":
    adj = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5), (4, 8)],
        3: [(4, 3), (5, 6)],
        4: [(5, 2)],
        5: [],
    }
    dist, parent = dijkstra_with_parent(adj, 6, 0)
    print(dist)
    print(reconstruct_path(parent, 0, 4))
    print(reconstruct_path(parent, 0, 5))
