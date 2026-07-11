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


def shortest_via_k(adj, adj_reverse, n, s, t, k):

    dist_from_k = dijkstra_heap(adj, n, k)

    dist_to_k = dijkstra_heap(adj_reverse, n, k)

    return dist_to_k[s] + dist_from_k[t]


adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: [],
}

n = 6
s = 0
t = 5
k = 2
dist = dijkstra_heap(adj, n, k)

answer = dist[s] + dist[t]

print(answer)
