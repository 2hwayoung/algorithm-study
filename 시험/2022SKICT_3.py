
import math

def solution(width, height, diagonals):
    answer = 0
    for diagonal in diagonals:
        left = int(math.factorial(diagonal[0]-1+diagonal[1])/(math.factorial(diagonal[0]-1) * math.factorial(diagonal[1])))% 10000019
        right = int(math.factorial(width-diagonal[0]+height-diagonal[1] + 1)/(math.factorial(width-diagonal[0]) * math.factorial(height-diagonal[1] + 1)))% 10000019
        answer += left * right
        left = int(math.factorial(diagonal[0]+diagonal[1]-1)/(math.factorial(diagonal[0]) * math.factorial(diagonal[1]-1)))% 10000019
        right = int(math.factorial(width-diagonal[0] + 1 + height-diagonal[1])/(math.factorial(width-diagonal[0]+1) * math.factorial(height-diagonal[1])))% 10000019
        answer += left * right
    return answer % 10000019

# print(solution(3, 2, [[1, 1], [2, 2]]))
print(solution(51, 37, [[17, 19]]))