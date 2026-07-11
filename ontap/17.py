import heapq


def dijkstra_heap(adj, n, s):
    INF = float("inf")
    dist = [INF] * n
    dist[s] = 0
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
                heapq.heappush(pq, (dist[v], v))

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
    print(dijkstra_heap(adj, 6, 0))
