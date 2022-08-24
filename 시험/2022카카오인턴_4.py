import heapq
INF = int(1e9)

def dijkstra(start, end, graph):
    q = []
    heapq.heappush(q, (0, start))
    min_distance = 0
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            if i[1] < min_distance:
                min_distance = i[1]
                heapq.heappush(q, (i[1], i[0]))

def solution(n, paths, gates, summits):
    graph = [[] for i in range(n+1)]
    for start, end, w in paths:
        graph[start].append((end, w))
    for gate in gates:
        for summit in summit:
            start = gate
            end = summit
            dijkstra(start, end, graph)

    answer = []
    return answer


print(solution(6, 	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3], [5])) # [5,3]
print(solution(7, 	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2,3,4])) # [3,4]