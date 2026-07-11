import heapq


def dijkstra_heap(adj, n, s):
    dist = {}
    for i in range(n):
        dist[i] = float("inf")
    dist[s] = 0
    pq = [(0, s)]
    visited = [False] * n
    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist


adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: [],
}
queries = [(0, 5), (0, 4), (2, 5)]

for s, t in queries:

    dist = dijkstra_heap(adj, 6, s)

    print("Từ", s, "đến", t, "=", dist[t])
