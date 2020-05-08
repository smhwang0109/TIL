def check(i,j):
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if  0 <= ni and ni < N and 0 <= nj and nj < M:
            if room[i][nj] and room[ni][j] and room[ni][nj]:
                room[i][j] = 2
                room[i][nj] = 2
                room[ni][j] = 2
                room[ni][nj] = 2
                return

di = [1,1,-1,-1]
dj = [1,-1,1,-1]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if room[i][j] == 1:
                check(i, j)
    result = 'YES'
    for i in range(N):
        if 1 in room[i]:
            result = 'NO'
            break
    print(result)