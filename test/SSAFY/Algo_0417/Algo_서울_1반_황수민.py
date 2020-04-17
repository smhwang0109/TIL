from _collections import deque

# BFS 방식으로 주변확인하며 0으로 만든다.
def BFS(i,j):
    que = deque()
    que.append([i, j])
    while que:
        i, j = que.popleft()
        M[i][j] = 0
        for k in range(8):
            if i+di[k] >= 0 and i+di[k] < 10 and j+dj[k] >= 0 and j+dj[k] < 10:
                if M[i+di[k]][j+dj[k]] == 1:
                    que.append([i+di[k], j+dj[k]])
    return


# 주변 8방향 확인을 위한 배열
di = [1, -1, 0, 0, 1, -1, 1, -1]
dj = [0, 0, 1, -1, 1, -1, -1, 1]

# 테스트 케이스 input
T = int(input())
for tc in range(1, T+1):
    # input 받기
    M = [list(map(int, input().split())) for _ in range(10)]
    cnt = 0
    # 2차원 배열 M을 돌면서 1이 있으면 인접하게 이어지는 요소는 BFS 방식으로 전부 0으로 만들고 카운트를 하나 올린다.
    for i in range(10):
        for j in range(10):
            if M[i][j] == 1:
                cnt += 1
                BFS(i,j)
    # 출력
    print('#{} {}'.format(tc, cnt))