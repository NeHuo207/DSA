def dijkstra(adj, n, s):
    INF = float("inf")
    dist = [INF] * n
    dist[s] = 0
    visited = [False] * n

    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        if dist[u] == INF:
            break
        visited[u] = True

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist


if __name__ == "__main__":
    adj = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5), (4, 8)],
        3: [(4, 3), (5, 6)],
        4: [(5, 2)],
        5: [],
    }
    print(dijkstra(adj, 6, 0))
