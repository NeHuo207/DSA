import heapq
def dijkstra(adj,n,s,t):
    dist = {}
    for v in adj:
        dist[v] = float('inf')
    dist[s] = 0
    pq = [(0,s)]
    visited = set()
    
    while pq:
        d,u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        if u == t:
            return d
        for v,w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq,(dist[v],v))
    return dist[t]
adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: []
}
dist = dijkstra(adj,6,0,4)
print(dist)