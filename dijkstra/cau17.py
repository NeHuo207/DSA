import heapq


def minimax_path(adj, n, s):

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

            nd = max(dist[u], w)

            if nd < dist[v]:

                dist[v] = nd

                heapq.heappush(pq, (nd, v))

    return dist


adj = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}

dist = minimax_path(adj, 4, 0)

print([dist[i] for i in range(4)])
