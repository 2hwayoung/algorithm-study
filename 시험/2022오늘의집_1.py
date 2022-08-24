def getLength(left_path):
    first_di = left_path[0]
    length = 0
    next_di = ''
    for di in left_path:
        if di == first_di:
            length +=1
        else:
            next_di = di
            break
    return length, next_di

way = {'N' : {'W' : 'left', 'E' : 'right'}, 
        'W' : {'S' : 'left', 'N' : 'right'},
        'S' : {'E' : 'left', 'W' : 'right'},
        'E' : {'N' : 'left', 'S' : 'right'}
}

def getMsg(time, length, di, next_di):
    return "Time "+str(time)+": Go straight "+str(length)+"00m and turn "+way[di][next_di]

def solution(path):
    answer = []
    left_path = path
    time = 0
    while len(left_path) > 0:
        length, next_di = getLength(left_path)
        if len(next_di) > 0:
            say_length = 5 if length > 5 else length
            say_time = time + length - 5 if length > 5 else time
            answer.append(getMsg(say_time, say_length, left_path[0], next_di))
            time += length
            left_path = left_path[length:]
        else:
            break

    return answer