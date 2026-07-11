import heapq


def shortest_at_most_k_edges(adj, n, s, t, k):

    dist = [[float("inf")] * (k + 1) for _ in range(n)]

    dist[s][0] = 0

    pq = [(0, s, 0)]

    while pq:

        d, u, edges = heapq.heappop(pq)

        if d > dist[u][edges]:
            continue

        if edges == k:
            continue

        for v, w in adj[u]:

            nd = d + w

            if nd < dist[v][edges + 1]:

                dist[v][edges + 1] = nd

                heapq.heappush(pq, (nd, v, edges + 1))

    return min(dist[t])


adj = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(3, 5)], 3: []}

print(shortest_at_most_k_edges(adj, 4, 0, 3, 2))
