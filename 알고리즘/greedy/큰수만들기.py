# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
    for num in number:
        if len(answer) == 0:
            answer += num
            continue
        while len(answer) > 0 and answer[-1] < num and k > 0:
            answer = answer[:-1]
            k -= 1
        answer += num
    if k != 0:
        answer = answer[:-k]
    return answer

# print(solution("1231234", 3))