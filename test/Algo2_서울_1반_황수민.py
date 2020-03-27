from _collections import deque

def BFS(i, j, num):
    global maxv, minsize
    size = 1
    que = deque([[i, j]])
    # que를 돌며 같은 값이면서 방문하지 않은 지점을 확인 후 que에 추가 및 방문 표시
    while que:
        i, j = que.popleft()
        for k in range(8):
            if i + di[k] >= 0 and i + di[k] < N and j + dj[k] >= 0 and j + dj[k] < N:
                if M[i + di[k]][j + dj[k]] == num and visited[i + di[k]][j + dj[k]] == 0:
                    que.append([i + di[k], j + dj[k]])
                    visited[i + di[k]][j + dj[k]] = 1
                    size += 1
    result = size * num

    # 최대값 확인 및 저장
    if maxv < result:
        maxv = result
        minsize = size
    elif maxv == result:
        if minsize > size:
            minsize = size

# 8방향을 확인하기 위한 리스트 생성
di = [1, -1, 0, 0, 1, 1, -1, -1]
dj = [0, 0, 1, -1, 1, -1, 1, -1]

# 테스트 케이스 받아서 해당 횟수만큼 반복
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    maxv = 0
    minsize = 401
    # 0이 아니고 방문하지 않은 지점에서 BFS 시작
    for i in range(N):
        for j in range(N):
            if M[i][j] != 0 and visited[i][j] == 0:
                visited[i][j] = 1
                BFS(i, j, M[i][j])
                
    # 최대 매장량이 0일 경우
    if minsize == 401:
        minsize = 0
    print('#{} {} {}'.format(tc, maxv, minsize))