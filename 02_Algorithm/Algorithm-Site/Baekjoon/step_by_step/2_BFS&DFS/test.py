import sys
from collections import deque


input = lambda : sys.stdin.readline().strip()

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
hi = [2, -2, 2, -2, 1, -1, 1, -1]
hj = [1, 1, -1, -1, 2, 2, -2, -2]

def bfs(init_K):
    global H, W
    que = deque()
    que.append([0, 0, init_K, 0])
    visited[init_K][0][0] = True
    while que:
        i, j, K, cnt = que.popleft()
        for idx in range(8):
            if idx < 4:
                ni = i + di[idx]
                nj = j + dj[idx]
                if 0 <= ni < H and 0 <= nj < W and not board[ni][nj]:
                    if ni == H - 1 and nj == W - 1:
                        return cnt + 1
                    flag = False
                    for k in range(init_K, K - 1, -1):
                        if visited[k][ni][nj]:
                            flag = True
                            continue
                    if not flag:
                        visited[K][ni][nj] = True
                        que.append([ni, nj, K, cnt + 1])
            if K > 0:
                ni = i + hi[idx]
                nj = j + hj[idx]
                if 0 <= ni < H and 0 <= nj < W and not board[ni][nj]:
                    if ni == H - 1 and nj == W - 1:
                        return cnt + 1
                    flag = False
                    for k in range(init_K, K - 2, -1):
                        if visited[k][ni][nj]:
                            flag = True
                            continue
                    if not flag:
                        visited[K - 1][ni][nj] = True
                        que.append([ni, nj, K - 1, cnt + 1])
    return -1

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
visited = [[[False] * W for _ in range(H)] for __ in range(K + 1)]

if W == 1 and H == 1:
    print(0)
else:
    print(bfs(K))
