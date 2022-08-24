def solution(levels):
    size = len(levels)
    top = size // 4

    if top == 0:
        return -1
    
    levels.sort(reverse=True)
    
    answer = levels[top-1]
    return answer