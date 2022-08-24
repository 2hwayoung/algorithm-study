
def updateSpot(cur, line, dist):
    need_remove_list = []
    for i in range(len(dist)):
        for cur_dist in line[cur]:
            for other_dist in line[i]:
                if abs(cur_dist - other_dist) != dist[cur][i]:
                    need_remove_list.append(cur_dist)
    need_remove_list = set(need_remove_list)
    for item in need_remove_list:
        line[cur].remove(item)
    
def solution(dist):
    line = [[] for i in range(len(dist))] 
    # 첫번째 점의 좌표값을 0으로 설정
    line[0].append(0)
    for i in range(len(dist)):
        for j in range(len(dist)):
            if i >= j:
                continue
            # j의 좌표값이 정해지지 않은 경우 i와의 거리를 좌표값으로 설정
            if len(line[j]) == 0:
                for i_spot in line[i]:
                    line[j].append(i_spot+dist[i][j])
                    line[j].append(i_spot-dist[i][j])
            # j의 좌표값이 정해진 경우 해당 dist의 거리가 맞는지 확인 -> 틀리다면 정해진 좌표값 제거
            else:
                for i_spot in line[i]:
                    line[j].append(i_spot+dist[i][j])
                    line[j].append(i_spot-dist[i][j])
                updateSpot(j, line, dist)
    d = {}
    for idx in range(len(line)):
        d[idx] = line[idx]
    d = sorted(d.items(), key=lambda x: x[1])
    result = []
    for item in d:
        result.append(item[0])
    if result[0] > result[-1]:
        return [list(reversed(result)), result]
    else:
        return [result, list(reversed(result))]

# print(solution([[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]])) # [[1,2,0,4,3],[3,4,0,2,1]]
print(solution([[0,2,3,1],[2,0,1,1],[3,1,0,2],[1,1,2,0]])) # 	[[0,3,1,2],[2,1,3,0]]