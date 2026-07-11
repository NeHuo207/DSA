import heapq


def dijkstra_grid(grid, start, goal):
    R, C = len(grid), len(grid[0])
    INF = float("inf")
    dist = {start: grid[start[0]][start[1]]}
    pq = [(grid[start[0]][start[1]], start)]
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        if u == goal:
            return d, len(visited)

        r, c = u
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                nd = d + grid[nr][nc]
                if nd < dist.get((nr, nc), INF):
                    dist[(nr, nc)] = nd
                    heapq.heappush(pq, (nd, (nr, nc)))

    return INF, len(visited)


def a_star_grid(grid, start, goal):
    R, C = len(grid), len(grid[0])
    INF = float("inf")

    def heuristic(pos):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    dist = {start: grid[start[0]][start[1]]}
    pq = [(dist[start] + heuristic(start), start)]
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        f, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        if u == goal:
            return dist[u], len(visited)

        r, c = u
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                nd = dist[u] + grid[nr][nc]
                if nd < dist.get((nr, nc), INF):
                    dist[(nr, nc)] = nd
                    heapq.heappush(pq, (nd + heuristic((nr, nc)), (nr, nc)))

    return INF, len(visited)


if __name__ == "__main__":
    grid = [[1] * 10 for _ in range(10)]
    start, goal = (0, 0), (9, 9)

    d1, v1 = dijkstra_grid(grid, start, goal)
    d2, v2 = a_star_grid(grid, start, goal)

    print(f"Dijkstra: dist={d1}  duyet {v1} dinh")
    print(f"A*:       dist={d2}  duyet {v2} dinh")
