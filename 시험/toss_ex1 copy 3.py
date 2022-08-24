from collections import defaultdict

def solution(k, dungeons):
    dic = defaultdict(int)
    dungeons.sort(key=lambda x: -x[0])
    for i in range(len(dungeons)):
        dic[i] = dungeons[i][0] - dungeons[i][1]
    sorted_list = sorted(dic.items(), key = lambda item: (-item[1], -dungeons[i][0]))

    answer = 0
    for item in sorted_list:
        need = dungeons[item[0]][0]
        use = dungeons[item[0]][1]

        if (k >= need):
            answer = answer + 1
            k = k - use

    return answer