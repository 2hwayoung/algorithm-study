# link : https://www.acmicpc.net/problem/9935


# 폭발 문자열은 같은 문자 두 개 이상 포함 X
inputs = input()
bombs = input()
last = bombs[-1]
size = len(bombs)
answer = []
count = 0
for word in inputs:
    answer.append(word)
    count += 1
    if (count < size):
        continue
    # 현재 위치가 폭발 문자열 끝문자랑 같을 때 확인한다
    if (word == last):
        same = True
        for i in range(-1, (-len(bombs))-1, -1):
            if answer[i] != bombs[i]:
                same = False
                break
        
        if same:
            for i in range(size):
                answer.pop()

# 남아 있는 문자가 없는 경우 FRULA 출력
if len(answer) == 0:
    print("FRULA")
else:
    print("".join(answer))  
