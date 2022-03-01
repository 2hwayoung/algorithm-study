# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3
    
def solution(numbers, hand):
    for i in range(len(numbers)) :
        if numbers[i] == 0:
            numbers[i] = 11

    current_left = 10
    current_right = 12
    answer = ''

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            current_left = number
            continue
        elif number in [3, 6, 9]:
            answer += 'R'
            current_right = number
            continue
        else:
            dist_left = divmod(abs(current_left-number),3)[0] + divmod(abs(current_left-number),3)[1]
            dist_right = divmod(abs(current_right-number),3)[0] + divmod(abs(current_right-number),3)[1]
            if dist_left < dist_right:
                answer += 'L'
                current_left = number
            elif dist_right < dist_left:
                answer += 'R'
                current_right = number
            else:
                if hand == 'left':
                    answer += 'L'
                    current_left = number
                else:
                    answer += 'R'
                    current_right = number
            
    return answer

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))