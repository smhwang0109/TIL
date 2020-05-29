from copy import deepcopy
from collections import deque

def define_start(case):
    if len(case) == 2:
        start_case.append(deepcopy(case))
        return
    for i in range(3):
        if not start_visited[i]:
            start_visited[i] = 1
            case.append(start_points[i])
            define_start(case)
            start_visited[i] = 0
            case.pop()

# 최단거리 구하고 2로 나눈 몫으로 결정
def check(start, end):
    global N, minv
    q = deque()
    q.append((start[0], start[1], 0))
    while q:
        i, j, cnt = q.popleft()
        if cnt >= minv:
            return
        visited[i][j] = 1
        for k in range(4):
            n_i = i + di[k]
            n_j = j + dj[k]
            if end[0] == n_i and end[1] == n_j:
                minv = cnt + 1
                return
            if 0 <= n_i < N and 0 <= n_j < N:
                if not visited[n_i][n_j] and not A[n_i][n_j]:
                    q.append((n_i, n_j, cnt + 1))


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
start_points = []
start_visited = [0] * 3
start_case = []
for i in range(N):
    for j in range(N):
        if A[i][j] == 2:
            start_points.append((i,j))
define_start([])
minv = float('inf')
for case in start_case:
    visited = [[0]*N for _ in range(N)]
    check(case[0], case[1])

print((minv+1) // 2)
