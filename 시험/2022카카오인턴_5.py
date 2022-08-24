
from collections import deque

def rotate(rc, row, col):
    edges = deque(list(rc[0]) + [items[-1] for items in list(rc)[1:-1]]
            +list(reversed(rc[-1]))+list(reversed([items[0] for items in list(rc)[1:-1]])))
    edges.appendleft(edges.pop())
    for i in range(1, row-1):
        rc[i][0] = edges[-i]
        rc[i][-1] = edges[col + i - 1]
    for j in range(col):
        rc[0][j] = edges[j]
        rc[-1][j] = edges[col*2 + row -3 -j]
    return rc

def shiftRow(rc, row, col):
    rc.appendleft(rc.pop())
    return rc

def solution(rc, operations):
    row, col = len(rc), len(rc[0])
    rc = deque(rc)
    for operation in operations:
        if operation == 'Rotate':
            rc = rotate(rc, row, col)
        else:
            rc = shiftRow(rc, row, col)

    return list(rc)

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", 'ShiftRow']))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
