
INF = int(1e9)

def dp(cur_alp, cur_cop, available_problems):
    costs = []
    for problem in available_problems:
        print(problem)
    return 1

def solution(alp, cop, problems):
    problems.append([0, 0, 1, 0, 1], [0, 0, 0, 1, 1])
    problems = sorted(problems, key=lambda x : x[0]+x[1], reverse=True)
    max_alp = max([problem[0] for problem in problems])
    max_cop = max([problem[1] for problem in problems])
    dp = [[INF] * (151) for _ in range(151)]
    dp[alp][cop] = 0
    dp[max_alp][max_cop] = max_alp-alp + max_cop-cop
    cur_alp = alp
    cur_cop = cop
    available_problems = []
    while len(available_problems) < len(problems):
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp_req > cur_alp or cop_req > cur_cop:
                continue
            dp[cur_alp][cur_cop] = min(dp(cur_alp, cur_cop, available_problems), dp[max_alp][max_cop])

    answer = 0
    return answer

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]])) # 15
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]	)) # 13

def solution(alp, cop, problems):
    problems = [[alp, cop, 1, 0, 1], [alp, cop, 0, 1, 1]] + problems
    target_alp = max([p[0] for p in problems])
    target_cop = max([p[1] for p in problems])

    dp = [[0] * (target_cop + 31) for _ in range(target_alp + 31)]
    for cur_al in range(alp, target_alp + 31):  # 알고력
        for cur_co in range(cop, target_cop + 31):  # 코딩력
            if cur_al == alp and cur_co == cop:
                continue
            sub = []
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if cur_al - alp_rwd < alp_req or cur_co - cop_rwd < cop_req:  # 해당 문제 풀 수 없는 단계
                    continue
                if cur_al - alp_rwd < alp or cur_co - cop_rwd < cop:  # 초기단계보다 작은 단계에서 점프하는 케이스
                    continue
                sub.append(dp[cur_al - alp_rwd][cur_co - cop_rwd] + cost)
            dp[cur_al][cur_co] = min(sub)

    answer = min([min(dp[row][target_cop:]) for row in range(target_alp, target_alp + 31)])
    return answer