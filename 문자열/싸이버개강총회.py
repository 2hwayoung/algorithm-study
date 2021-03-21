# https://www.acmicpc.net/problem/19583

from sys import stdin

beforeStarted = {}
line = stdin.readline()
t1, t2, t3 = map(str, line.split())
t1 = int("".join(t1.split(":")))
t2 = int("".join(t2.split(":")))
t3 = int("".join(t3.split(":")))

answer = 0

while (True) :
    line = stdin.readline()
    if len(line) < 5 : break
    time, nickname = map(str, line.split())
    time = int("".join(time.split(':')))
    if time <= t1 :
        beforeStarted[nickname] = True
    elif t2 <= time <= t3:
        if beforeStarted.get(nickname) :
            beforeStarted[nickname] = False
            answer += 1

print(answer)