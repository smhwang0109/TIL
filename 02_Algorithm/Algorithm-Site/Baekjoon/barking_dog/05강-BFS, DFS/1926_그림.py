import sys
from collections import deque


def solution():
    def bfs(i, j):
        que = deque()
        que.append([i, j])
        paper[i][j] = 0
        size = 1
        while que:
            i, j = que.popleft()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m and paper[ni][nj]:
                    que.append([ni, nj])
                    paper[ni][nj] = 0
                    size += 1
        return size

    n, m = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(n)]
    paint_cnt = 0
    max_size = 0
    for i in range(n):
        for j in range(m):
            if paper[i][j]:
                paint_cnt += 1
                temp_size = bfs(i, j)
                if max_size < temp_size:
                    max_size = temp_size
    print(paint_cnt)
    print(max_size)
    return


input = lambda : sys.stdin.readline().rstrip()

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

solution()