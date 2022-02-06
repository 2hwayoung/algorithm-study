# https://www.acmicpc.net/problem/1110
# 분류: while 문


import sys

n = sys.stdin.readline().strip()
n = "{0:0>2}".format(n)
cycle = 1
m = "{0:0>2}".format(int(n[0])+int(n[1]))
new = n[1] + m[1]
while (new != n):
    m = "{0:0>2}".format(int(new[0])+int(new[1]))
    new = new[1] + m[1]
    cycle = cycle + 1

print(cycle)