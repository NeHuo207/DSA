def dijkstra(adj,n,s):
    dist = {}
    for v in adj:
        dist[v] = float('inf')
    dist[s] = 0
    visited = [False] *n
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u==-1 or dist[i]<dist[u]):
                u = i
        if u==-1 or dist[u] == float('inf'): break
        visited[u] = True
        for v,w in adj[u]:
            if dist[u]+w<dist[v]:
                dist[v] = dist[u] + w
    return dist
def count_within_radius(dist,n,D):
    count = 0
    for i in range(n):
        if dist[i]<=D:
            count+=1
    return count
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
D = 3

dist = dijkstra(adj, n, s)

print("dist =", dist)

count = count_within_radius(dist, n, D)

print("Số đỉnh có khoảng cách <=", D, "là:", count)