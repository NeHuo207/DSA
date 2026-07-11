def transform_vertex_weighted(adj, n, cost):
    new_adj = {}

    for i in range(2 * n):
        new_adj[i] = []

    for v in range(n):
        vin = 2 * v
        vout = 2 * v + 1

        new_adj[vin].append((vout, cost[v]))

    for u in adj:
        uout = 2 * u + 1

        for v, w in adj[u]:
            vin = 2 * v
            new_adj[uout].append((vin, w))

    return new_adj


adj = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2)], 3: []}

cost = [1, 2, 3, 4]

new_adj = transform_vertex_weighted(adj, 4, cost)

for i in new_adj:
    print(i, "->", new_adj[i])
