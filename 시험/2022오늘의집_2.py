def solution(call):
    call_lower = call.lower()
    alpha_set = ''.join(set(call_lower))
    count_dic = {}
    for alpha in alpha_set:
        count_dic[alpha] = call_lower.count(alpha)
    count_dic = sorted(count_dic.items(), key = lambda x : x[1], reverse=True)
    max_count = count_dic[0][1]
    erase_list = []
    for item in count_dic:
        if item[1] == max_count:
            call = call.replace(item[0], "")
            call = call.replace(item[0].upper(), "")
        else:
            break

    return call