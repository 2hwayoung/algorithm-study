from collections import defaultdict

def solution(s):
    answer = -1
    for num in range(10):
        item = str(num) * 3
        if item in s and num > answer:
            answer = num
    if answer > 0:
        answer = 100 * answer + 10 * answer + answer
    return answer