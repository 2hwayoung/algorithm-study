#https://www.acmicpc.net/problem/2438
#분류: for 문

n = int(input())

for i in range(1, n+1):
    print("{0:>{1}s}".format("*"*i, n))