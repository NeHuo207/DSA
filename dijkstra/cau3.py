INF =  float('inf')         # Biến vô cực để thêm vào dist vì không biết biến là bao nhiêu
def dijkstra(adj,s):
    n = len(adj)            # số đỉnh
    dist = [INF]*n          # Cho tất cả các đỉnh bằng vô cực
    visited = [False]*n     # Các đỉnh đã chốt bằng False
    dist[s] = 0             # Đỉnh xuất phát s=0
    for _ in range(n):      # Lặp V vòng
        # Tìm u chưa visited có dist nhỏ nhất
        u = -1
        min_dist = INF
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:     # Đang so sánh tìm min
                min_dist = dist[i]
                u = i           # Ứng viên tạm thời
        '''
        Hiểu nôm na dòng for i là như này:
        "Trong tất cả các đỉnh chưa chốt,
        thằng nào có dist nhỏ hơn thằng đang nhỏ nhất hiện tại
        → ghi nhớ thằng đó vào u"<
        ''' 
        if u == -1:         # Nếu không tìm được cạnh nào thì hủy
            break
        visited[u] = True       # Sau khi tìm xong ứng viên thì chốt đỉnh
        for v, w in adj[u]:
            if not visited[v] and dist[v] > dist[u] + w:            # "Nếu đi  0 → ... → u → v mà ngắn hơn đường đang biết tới v thì cập nhật!"
                dist[v] = dist[u] + w                               # Nếu đi vòng qua u mà tới v ngắn hơn → cập nhật đường mới!
    return dist
G1 = [
    [(2,1)],
    # ↑ ↑
    # v w → v là đỉnh kề, w là trọng số cạnh
    [(2,2),(4,4)],
    [(0,1),(1,2),(3,3)],
    [(2,3),(5,5)],
    [(1,4),(5,2)],
    [(3,5),(4,2)]
]
print(dijkstra(G1,0))