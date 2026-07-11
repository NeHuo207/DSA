def dijkstra(adj, n, s):
    INF = float("inf")
    dist = [INF] * n
    dist[s] = 0
    visited = [False] * n
    order = []

    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if dist[u] == INF:
            break
        visited[u] = True
        order.append((u, dist[u]))

        for v, w in adj[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist, order


def bellman_ford(edges, n, s):
    INF = float("inf")
    dist = [INF] * n
    dist[s] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None

    return dist


if __name__ == "__main__":
    adj = {
        0: [(1, 2), (2, 5)],
        1: [],
        2: [(1, -4)],
    }
    edges = [(0, 1, 2), (0, 2, 5), (2, 1, -4)]

    dist_dij, order = dijkstra(adj, 3, 0)

    print("thu tu chot dinh:")
    for u, d in order:
        print(f"  chot dinh {u} voi dist={d}")

    print(f"\nDijkstra:     {dist_dij}")
    print(f"Bellman-Ford: {bellman_ford(edges, 3, 0)}")
    print(f"\ndist[1]: Dijkstra={dist_dij[1]} (SAI)  thuc te 0->2->1 = 5+(-4) = 1")
