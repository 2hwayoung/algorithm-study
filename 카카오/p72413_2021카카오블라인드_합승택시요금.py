# https://programmers.co.kr/learn/courses/30/lessons/72413


INF = int(1e9)

def solution(n, s, a, b, fares):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n+1):
        graph[i][i] = 0

    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])
    
    # for j in range(1, n + 1):
    #     for k in range(1, n + 1):
    #         # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    #         if graph[j][k] == INF:
    #             print("INFINITY", end=" ")
    #         # 도달할 수 있는 경우 거리를 출력
    #         else:
    #             print(graph[j][k], end=" ")
    #     print()

    a_min_direct = graph[s][a]
    b_min_direct = graph[s][b]
    print(a_min_direct, b_min_direct)
    # s-a-b, s-b-a 경로와 따로 갔을 때의 거리를 비교해서 최저 요금을 갱신한다.
    min_taxi = min(a_min_direct + b_min_direct,
                    graph[s][a] + graph[a][b],
                    graph[s][b] + graph[b][a])

    # 각 노드k마다 s-k-a + s-k-b 거리와 위의 최저 요금 거리와 비교해서 최저 요금을 갱신한다.
    for k in range(1, n+1):
            min_taxi = min(min_taxi, 
                            graph[s][k] + graph[k][a] + graph[k][b])

    return min_taxi


# print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))