# https://www.acmicpc.net/problem/1546
# 분류 : 1치원 배열

import sys
num = int(input())
lst = [int(n) for n in sys.stdin.readline().split()]

maxi = max(lst)
lst = list(map(lambda x: x/maxi*100, lst))
print(sum(lst)/len(lst))