def check_color_cnt(start_i, start_j):
    global min_v
    change_cnt = 0
    start_color = board[start_i][start_j]
    for i in range(8):
        for j in range(8):
            temp_color = board[start_i + i][start_j + j]
            if j % 2:
                if temp_color == start_color:
                    change_cnt += 1
            else:
                if temp_color != start_color:
                    change_cnt += 1

        if start_color == 'W':
            start_color = 'B'
        else:
            start_color = 'W'
    if change_cnt > 32:
        change_cnt = 64 - change_cnt
    return change_cnt


N, M = map(int, input().split())

board = []

for n in range(N):
    board.append(list(input()))

i_cnt = N - 8
j_cnt = M - 8

min_v = 1000000000000000000

for i in range(i_cnt + 1):
    for j in range(j_cnt + 1):
        temp_cnt = check_color_cnt(i, j)
        if min_v > temp_cnt:
            min_v = temp_cnt

print(min_v)