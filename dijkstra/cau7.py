import heapq
def dijkstra(adj,n,s):
    dist = {}
    parent = {}
    for v in adj:
        dist[v] = float('inf')
        parent[v]=-1
    dist[s] = 0
    pq = [(0,s)]
    visited = set()
    while pq:
        d,u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v,w in adj[u]:
            if dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
                parent[v]=u
                heapq.heappush(pq,(dist[v],v))
    return dist,parent
def reconstruct_path(parent,s,t):
    path = []
    cur = t
    while cur !=-1:
        path.append(cur)
        if cur==s: break
        cur = parent[cur]
    path.reverse()
    return path
adj = {
    0: [(1,4),(2,1)],
    1: [(3,1)],
    2: [(1,2),(3,5),(4,8)],
    3: [(4,3),(5,6)],
    4: [(5,2)],
    5: []
}

dist, parent = dijkstra(adj, 6, 0)

path = reconstruct_path(parent, 0, 4)

print(path)
print(dist[4])