import heapq


def grid_dijkstra(cost):
    R, C = len(cost), len(cost[0])
    INF = float("inf")
    dist = [[INF] * C for _ in range(R)]
    dist[0][0] = cost[0][0]
    pq = [(cost[0][0], 0, 0)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        d, r, c = heapq.heappop(pq)
        if d > dist[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                nd = d + cost[nr][nc]
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(pq, (nd, nr, nc))

    return dist[R - 1][C - 1]


if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1],
    ]
    print(grid_dijkstra(grid))

    grid2 = [
        [1, 2],
        [3, 4],
    ]
    print(grid_dijkstra(grid2))
