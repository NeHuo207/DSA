'''
Câu 3 (Đồ thị & Thuật toán Dijkstra)
Tại sao thuật toán Dijkstra lại cho kết quả sai khi đồ thị có chứa cạnh trọng số âm? Hãy tự thiết kế một đồ thị có hướng nhỏ (gồm 3 đỉnh) làm phản ví dụ chứng minh sự sai lệch của bước "chốt đỉnh". Đề xuất một thuật toán khác có thể thay thế Dijkstra trong trường hợp này.
'''
# Dijkstra dựa vào nguyên lý greedy tại mỗi bước nó chọn đỉnh có khoảng cách tạm thời nhỏ nhất trong tập chưa được chốt, sau đó finalize khoảng cách đó-coi như đã tối ưu, không bao giờ xét lại đỉnh này nữa
# Giả định ngầm của việc chốt: "vì mọi cạnh đều không âm, nên không có đường nào đi qua đỉnh khác rồi quay lại có thể ngắn hơn đường trực tiếp hiện tại
# Khi có cạnh âm, giả định này sụp đổ — một đường đi dài hơn về số cạnh vẫn có thể có tổng trọng số nhỏ hơn nhờ "được giảm" bởi cạnh âm ở sau. Nhưng Dijkstra đã chốt đỉnh đó từ sớm, không quay lại cập nhật nữa → kết quả sai.
def bellman_ford(vertices, edges, source):
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Kiểm tra chu trình âm
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Đồ thị có chu trình âm!")
            return None

    return dist


vertices = ['A', 'B', 'C']
edges = [
    ('A', 'B', 4),
    ('A', 'C', 5),
    ('C', 'B', -3),
]

result = bellman_ford(vertices, edges, 'A')
print(result)