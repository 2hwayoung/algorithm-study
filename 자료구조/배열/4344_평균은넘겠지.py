# https://www.acmicpc.net/problem/4344

import sys
n = int(input())

for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    num = lst[0]
    scores = lst[1:]
    mean = sum(scores) / len(scores)
    cnt = 0
    for score in scores:
        if score > mean:
            cnt += 1
    print("{:.3f}%".format(cnt/len(scores)*100))