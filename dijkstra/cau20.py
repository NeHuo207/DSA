import heapq


def k_shortest_paths(adj, n, s, t, K):

    count = [0] * n

    result = []

    pq = [(0, s)]

    while pq and len(result) < K:

        d, u = heapq.heappop(pq)

        if count[u] >= K:
            continue

        count[u] += 1

        if u == t:
            result.append(d)

        for v, w in adj[u]:

            heapq.heappush(pq, (d + w, v))

    return result


adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: [],
}

print(k_shortest_paths(adj, 6, 0, 5, 3))
