# p.147

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    #큐(Queue) 구현을 위해 deque 라이브러리 이용
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑기
        v = queue.popleft()

        # 헤당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[v]:
                queue.append(i[0])
                graph[v][1] = True
                visited[i] = True

def solution(n, edges, k, a, b):
    graph = [[0, False] for i in range(n)]
    # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
    for edge in edges:
        graph[edge[0]][0] = edge[1]

    # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
    visited = [False] * n

    bfs(graph, a, visited)
    num = 0
    for edge in graph:
        if edge[1]:
            num += 1
    return num


print(solution(9, [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]], 4, 0, 3))
