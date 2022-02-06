# https://www.acmicpc.net/problem/10871
# 분류: for 문

import sys

n, x = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
result = []
for i in lst:
    if (i < x):
        result.append(i)

for index, value in enumerate(result):
    if index == len(result) - 1:
        print(value)
    else:
        print(value, end=" ")
