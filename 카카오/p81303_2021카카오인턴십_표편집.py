# https://programmers.co.kr/learn/courses/30/lessons/81303


def solution(n, k, cmd):
    total_list = [1 for i in range(n)]
    deleted_list = []
    length = len(total_list)
    current_index = k
    last_index = length - 1

    for cmd_item in cmd:
        if cmd_item == 'C':
            deleted_list.append(current_index)
            total_list[current_index] = -1
            if current_index == last_index:
                while total_list[current_index] < 0:
                    current_index -= 1
                last_index = current_index
            else :
                while total_list[current_index] < 0:
                    current_index += 1

        elif cmd_item == 'Z':
            deleted_index = deleted_list.pop()
            total_list[deleted_index] = 1

        elif cmd_item[0] == 'U':
            up_cnt = int(cmd_item[2:])
            while up_cnt > 0:
                current_index -= 1
                if total_list[current_index] > 0:
                    up_cnt -= 1
        else:
            down_cnt = int(cmd_item[2:])
            while down_cnt > 0:
                current_index += 1
                if total_list[current_index] > 0:
                    down_cnt -= 1
    answer = ''
    for item in total_list:
        if item == -1:
            answer += 'X'
        else:
            answer += 'O'
    return answer
