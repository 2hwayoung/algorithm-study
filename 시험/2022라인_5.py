def solution(abilities, k):
    answer = 0
    if len(abilities) % 2:
        abilities.append(0)
    abilities.sort(reverse=True)
    rnd = (len(abilities) + 1) // 2
    dp = [[0] * (k + 1) for _ in range(rnd + 1)]

    for r in range(1, rnd + 1):
        for c in range(k + 1):
            # 우선권 하나도 사용X
            first = abilities[2 * (r - 1)]
            second = abilities[2 * (r - 1) + 1]
            if c > r:
                continue
            if c == 0:
                dp[r][c] = dp[r - 1][c] + abilities[2 * (r - 1) + 1]
            else:
                dp[r][c] = max(dp[r - 1][c] + second, dp[r - 1][c - 1] + first)

    return dp[rnd][k]

print(solution([2, 8, 3, 6, 1, 9, 1, 9], 2))
print(solution([10, 9, 8, 7, 6], 1))