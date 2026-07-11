import heapq

def second_shortest(adj,n,s):

    dist1={}
    dist2={}

    for i in range(n):
        dist1[i]=float('inf')
        dist2[i]=float('inf')

    dist1[s]=0

    pq=[(0,s)]

    while pq:

        d,u=heapq.heappop(pq)

        if d>dist2[u]:
            continue

        for v,w in adj[u]:

            nd=d+w

            if nd<dist1[v]:

                dist2[v]=dist1[v]
                dist1[v]=nd

                heapq.heappush(pq,(nd,v))

            elif dist1[v]<nd<dist2[v]:

                dist2[v]=nd

                heapq.heappush(pq,(nd,v))

    return dist1,dist2
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
dist1, dist2 = second_shortest(adj, n, s)

print("Shortest:")
print([dist1[i] for i in range(n)])

print("Second shortest:")
print([dist2[i] for i in range(n)])