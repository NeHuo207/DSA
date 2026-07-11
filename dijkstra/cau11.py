import heapq


def multi_source_dijkstra(adj, n, sources):
    dist = {}

    for i in range(n):
        dist[i] = float("inf")

    pq = []

    for s in sources:
        dist[s] = 0
        heapq.heappush(pq, (0, s))

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
sources = [0, 3]

dist = multi_source_dijkstra(adj, 6, sources)

print([dist[i] for i in range(6)])
