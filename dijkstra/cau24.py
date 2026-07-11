import heapq


def a_star(adj, n, s, t, heuristic):

    dist = {}

    for i in range(n):
        dist[i] = float("inf")

    dist[s] = 0

    pq = [(heuristic[s], s)]

    visited = [False] * n

    visited_count = 0

    while pq:

        f, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        visited_count += 1

        if u == t:
            return dist[t], visited_count

        for v, w in adj[u]:

            nd = dist[u] + w

            if nd < dist[v]:

                dist[v] = nd

                heapq.heappush(pq, (nd + heuristic[v], v))

    return float("inf"), visited_count


adj = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(3, 5)], 3: []}

heuristic = [3, 1, 2, 0]

print(a_star(adj, 4, 0, 3, heuristic))
