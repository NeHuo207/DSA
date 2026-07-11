import heapq
def dijkstra(source,n, graph):
    dist = [float('inf')]*n
    dist[source] = 0
    pq = [(0,source)]
    while pq:
        d,u = heapq.heappop(pq)
        if d>dist[u]:
            continue
        for v,w in graph[u]:
            if dist[u] + w<dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq,(dist[v],v))
    for v in range(n):
        print(f"dist[{v}] = {dist[v]}")