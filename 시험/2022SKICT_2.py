

def solution(n, clockwise):
    coords = [[0] * n for _ in range(n)]
    row = n // 2
    value = 0
    # 시계 방향인 경우 
    if clockwise:
        for i in range(row):
            column = n - 1 - i
            for j in range(i, column):
                value += 1
                coords[i][j] = value
                coords[j][n-i-1] = value
                coords[n-i-1][n-j-1] = value
                coords[n-j-1][i] = value
        
        coords[row][row] = value + 1
        if n % 2 == 0:
            coords[row-1][row-1] = value
            coords[row][row] = value
            coords[row][row] = value
            coords[row][row] = value

    else:
        if n % 2 == 0:
            row -= 1

        for i in range(row):
            column = n - 1 - i
            for j in range(i, column):
                value += 1
                coords[j][i] = value
                coords[n-i-1][j] = value
                coords[n-j-1][n-i-1] = value
                coords[i][n-j-1] = value
        
        coords[row][row] = value + 1
        if n % 2 == 0:
            coords[row][row+1] = value + 1
            coords[row+1][row] = value + 1
            coords[row+1][row+1] = value + 1

    return(coords)

# print(solution(8, True))