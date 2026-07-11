import heapq

def count_shortest_paths(adj, n, s):

    dist = {}
    ways = {}

    for i in range(n):
        dist[i] = float('inf')
        ways[i] = 0

    dist[s] = 0
    ways[s] = 1

    pq = [(0,s)]

    visited = [False]*n

    while pq:

        d,u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        for v,w in adj[u]:

            if dist[u]+w < dist[v]:

                dist[v]=dist[u]+w
                ways[v]=ways[u]

                heapq.heappush(pq,(dist[v],v))

            elif dist[u]+w == dist[v]:

                ways[v]+=ways[u]

    return ways
adj = {
    0: [(1,4), (2,1)],
    1: [(3,1)],
    2: [(1,2), (3,5), (4,8)],
    3: [(4,3), (5,6)],
    4: [(5,2)],
    5: []
}

n = 6
s = 0
ways = count_shortest_paths(adj, n, s)

print("ways =", ways)
print([ways[i] for i in range(n)])