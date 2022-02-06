# https://www.acmicpc.net/problem/11021
# 분류: for 문

import sys

n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #",i+1,": ",a+b, sep="")