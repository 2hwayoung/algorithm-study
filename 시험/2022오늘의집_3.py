def solution(tstring, variables):
    dic_var = dict(variables)
    last_dic_var = {}
    visited = []
    last_v = ''
    for k, v in dic_var.items():
        last_dic_var[k] = v
        visited.append(k)
        cur_k, cur_v = k, v
        while True:
            # 값이 "변수"인 경우
            if cur_v[0] == '{' and cur_v[-1] == '}':
                next_k = cur_v[1:-1]
                # 변수가 실제 "변수" 중 하나인 경우
                if next_k in dic_var.keys():
                    # 원형 연결인 경우
                    if next_k in visited:
                        last_dic_var[k] = cur_v
                        visited = []
                        break
                    # 원형 연결이 아닌 경우
                    else:
                        visited.append(next_k)
                        last_dic_var[k] = cur_v
                        cur_k = next_k
                        cur_v = dic_var[cur_k]
                # "변수"가 그냥 값일 경우
                else:
                    visited = []
                    last_dic_var[k] = cur_v
                    break
            # 값이 "값"인 경우
            else: 
                visited = []
                last_dic_var[k] = cur_v
                break

    for k, v in last_dic_var.items():
        k = '{' + k + '}'
        tstring = tstring.replace(k, v)

    return tstring