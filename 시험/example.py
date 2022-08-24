
# # 초기 연료량 배열 v
# # 선두 트럭의 시간당 연료 소비량 a, 후위 b

# import heapq

# def solution(v, a, b):
#     heap = []
    
#     for value in v:
#         heapq.heappush(heap, (-value,value))
    
#     min_cost = a
#     count = 0
#     while True:
#         if heap[-1][1] < min_cost: 
#             print(True)
#             break
#         item = heapq.heappop(heap)[1]
#         item = item - (a-b)
#         heapq.heappush(heap, (-item, item))
#         min_cost += b
#         print(heap, min_cost)
#         count += 1
    
#     return count

# print(solution([4,5, 5], 2, 1))


# Calendar = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# def solution(masks, dates):
#     # 하루당 필요한 가격이 적은 순으로 정렬
#     masks = sorted(masks, key=lambda x : x[0]/x[1])
#     date_list = []
#     for date in dates:
#         date = date
#     return 0

# print(solution([[600,2], [500,1], [1015,4]], ["2023/01/01~2023/01/02", "2021/12/31"]))


def bomb(board,pending):
    print('bomb----',board, pending)
    for i,j in reversed(sorted(pending)):
        board[i].pop(j)
    pending = set()
    return board, pending

def traverse(board, pending, i, j):
    if i != 0 and len(board[i-1])>j+1 and len(board[i]) > j+1 and board[i][j] == board[i-1][j+1] == board[i][j+1]:
        for a, b in [(i,j), (i-1, j+1), (i, j+1)]:
            pending.add((a,b))
    if i < 5 and len(board[i])> j+1 and len(board[i+1])> j+1 and board[i][j] == board[i][j+1] == board[i+1][j+1]:
        for a, b in [(i,j), (i, j+1), (i+1, j+1)]:
            pending.add((a,b))
    if i < 5 and len(board[i])>j+1 and len(board[i+1])>j and board[i][j] == board[i][j+1] == board[i+1][j]:
        for a, b in [(i,j), (i,j+1), (i+1,j)]:
            pending.add((a,b))

    if i < 5 and len(board[i+1])> j+1 and board[i][j] == board[i+1][j] == board[i+1][j+1]:
        for a, b in [(i,j), (i+1, j), (i+1, j+1)]:
            pending.add((a,b))

    if i < 4 and len(board[i+1])> j and len(board[i+2])>j and board[i][j] == board[i+1][j] == board[i+2][j]:
        for a, b in [(i,j), (i+1, j), (i+2,j)]:
            pending.add((a,b))
    
    if len(board[i])>j+2 and board[i][j] == board[i][j+1] == board[i][j+2]:
        for a, b in [(i,j), (i, j+1), (i, j+2)]:
            pending.add((a,b))
    return board, pending

def solution(macaron):
    board =[[] for i in range(6)]
    pending=set()
    for line, color in macaron:
        print(board)
        board[line-1].append(color)
        while True:
            for i in range(6):
                for j in range(len(board[i])-1):
                    board, pending = traverse(board,pending, i, j)
            if not pending:
                break
            board, pending = bomb(board,pending)
    print(board)
    for i in range(6):
        for j in range(6-len(board[i])):
            board[i].append(0)

    result = ["" for i in range(6)]
    for j in range(5, -1, -1):
        for i in range(6):
            result[j] += str(board[i][j])
    result.reverse()
    return result

print(solution([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]))

