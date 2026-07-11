import heapq
def dijkstra(adj,s):
    dist = {}
    for v in adj:
        dist[v] = float('inf')
    dist[s] = 0
    visited = set()
    pq = [(0,s)]
    while pq:
        d,u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for (v,w) in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v],v))
    return dist
def undirected(edges):
    adj = {}
    for u,v,w in edges:
        adj.setdefault(u,[]).append((v,w))
        adj.setdefault(v,[]).append((u,w))
    return adj
edges = [
    ('A', 'B', 5),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 2),
    ('C', 'D', 6),
    ('D', 'E', 4),
]

adj = undirected(edges)
dist = dijkstra(adj, 'A')

for city, d in sorted(dist.items()):
    print(f"{city}: {d}")