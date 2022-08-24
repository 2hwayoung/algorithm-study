def solution(queue1, queue2):
    # 원소 합이 같도록 히는 필요한 작업의 최소 횟수, 불가능한 경우 -1
    # 전체 원소 합 구하기
    single_length = len(queue1)
    total_length = single_length + len(queue2)
    total_sum = sum(queue1)+sum(queue2)
    if total_sum % 2:
        return -1
    
    half_sum = total_sum // 2
    print('sum:',half_sum)
    total_queue = queue1 + queue2 + queue1
    left_index = 0
    right_index = 1
    interval_sum = sum(total_queue[left_index:right_index])
    answers = []
    while left_index < right_index:
        if interval_sum == half_sum:
            answers.append([left_index, right_index])
            print('same:', total_queue[left_index:right_index])
            left_index += 1
            right_index += 1
            if right_index < total_length + single_length and left_index < total_length:
                interval_sum = interval_sum + total_queue[right_index-1] - total_queue[left_index-1]
            else:
                break
        elif interval_sum < half_sum:
            right_index += 1
            if right_index < total_length + single_length:
                interval_sum += total_queue[right_index-1]
            else:
                break
        else:
            left_index += 1
            if left_index < total_length:
                interval_sum -= total_queue[left_index-1]
            else:
                break
    len_answers = []
    for item in answers:
        # 안 겹치는 경우
        if item[0] < single_length and item[1] < single_length:
            left_index = item[0]
            right_index = item[1]
            # 뒤에 남아있는 경우
            if right_index < single_length:
                print('a', left_index, right_index)
                len_answers.append(right_index+single_length+left_index)
            # 뒤에 남아있는 게 없는 경우
            else:
                print('b', left_index, right_index)
                len_answers.append(right_index-1)
        # 안 겹치는 경우
        elif single_length <= item[0] < total_length and single_length <= item[1] < total_length:
            left_index = item[0] - single_length
            right_index = item[1] - single_length
            # 뒤에 남아있는 경우
            if right_index < single_length:
                print('c', left_index, right_index)
                len_answers.append(right_index+single_length+left_index)
            # 뒤에 남아있는 게 없는 경우
            else:
                print('d', left_index, right_index)
                len_answers.append(right_index-1)
        # 겹치는 경우
        else:
            left_index = item[0]
            right_index = item[1]
            if item[0] >= single_length:
                left_index -= single_length
                right_index -= single_length
            print('e', left_index, right_index)
            len_answers.append(left_index+right_index-single_length)

    len_answers.sort()
    if len(len_answers):
        return len_answers[0]
    else: 
        return -1

print(solution([3,2,7,2], [4,6,5,1])) # 2
print(solution([1, 2, 1, 2], [1,10,1,2])) # 7
print(solution([1,1], [1,5])) # -1