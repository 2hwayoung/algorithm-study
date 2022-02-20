# https://www.acmicpc.net/problem/8958

n = int(input())
for i in range(n):
    answers = input()
    idx, summ = 0, 0
    for answer in answers:
        if (answer == 'O'):
            idx += 1
        else :
            idx = 0
        summ += idx
    print(summ)
        
        