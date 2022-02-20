# https://www.acmicpc.net/problem/10818
# 분류: 1차원 배열

import sys

n = int(input())
lst = [int(i) for i in sys.stdin.readline().split()]

print(min(lst), max(lst))