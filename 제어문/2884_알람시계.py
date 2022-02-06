# https://www.acmicpc.net/problem/2884
# 분류: if문

h, m = map(int, input().split())

if (m < 45):
    m = m + 60 - 45
    if (h == 0) :
        h = 23
    else :
        h = h - 1
else :
    m = m - 45

print(h, m)