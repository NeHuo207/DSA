import heapq


def dijkstra_extended_state(adj, s, target, max_fuel):

    dist = {}

    dist[(s, max_fuel)] = 0

    pq = [(0, s, max_fuel)]

    while pq:

        d, u, fuel = heapq.heappop(pq)

        if d > dist[(u, fuel)]:
            continue

        if u == target:
            return d

        for v, w, fuel_cost in adj[u]:

            new_fuel = fuel - fuel_cost

            if new_fuel >= 0:

                nd = d + w

                state = (v, new_fuel)

                if state not in dist or nd < dist[state]:

                    dist[state] = nd

                    heapq.heappush(pq, (nd, v, new_fuel))

    return float("inf")


adj = {0: [(1, 4, 2), (2, 3, 3)], 1: [(3, 5, 2)], 2: [(3, 2, 2)], 3: []}

print(dijkstra_extended_state(adj, 0, 3, 5))
