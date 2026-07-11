import heapq


def max_probability_path(adj, n, s, t):

    prob = {}

    for i in range(n):
        prob[i] = 0

    prob[s] = 1

    pq = [(-1, s)]

    visited = [False] * n

    while pq:

        p, u = heapq.heappop(pq)

        p = -p

        if visited[u]:
            continue

        visited[u] = True

        if u == t:
            return p

        for v, edge_p in adj[u]:

            np = p * edge_p

            if np > prob[v]:

                prob[v] = np

                heapq.heappush(pq, (-np, v))

    return prob[t]


adj = {0: [(1, 0.5), (2, 0.8)], 1: [(3, 0.9)], 2: [(3, 0.7)], 3: []}

print(max_probability_path(adj, 4, 0, 3))
