def calc(now, target):
    n = len(now)
    if n == 1:
        return 0
    elif n == 2:
        return 1
    idx = 0
    temp_now = 0
    temp_tar = 0
    while idx < n:
        temp_now += now[idx]
        temp_tar += target[idx]
        if temp_now == temp_tar:
            break
        idx += 1
    if idx == n-1:
        return n-1

    return calc(now[:idx + 1], target[:idx + 1]) + calc(now[idx + 1:], target[idx + 1:])


def solution(arr, brr):
    answer = calc(arr, brr)

    return answer