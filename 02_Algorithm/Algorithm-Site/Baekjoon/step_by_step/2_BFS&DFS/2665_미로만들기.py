import sys

input = sys.stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(i, j, cnt):
    global N, min_v
    for c in range(cnt + 1):
        if visited[c][i][j]:
            return
    visited[cnt][i][j] = 1
    for k in range(4):
        n_i = i + di[k]
        n_j = j + dj[k]
        if n_i == N - 1 and n_j == N - 1:
            min_v = cnt
            return
        if 0 <= n_i < N and 0 <= n_j < N:
            if maze[n_i][n_j]:
                if min_v <= cnt:
                    continue
                if not visited[cnt][n_i][n_j]:
                    dfs(n_i, n_j, cnt)
            else:
                if min_v <= cnt + 1:
                    continue
                for c in range(cnt + 1):
                    if visited[c][n_i][n_j]:
                        continue
                if len(visited) == cnt + 1:
                    visited.append([[0]*N for _ in range(N)])
                    dfs(n_i, n_j, cnt + 1)
                elif len(visited) > cnt + 1:
                    if not visited[cnt + 1][n_i][n_j]:
                        dfs(n_i, n_j, cnt + 1)
    return



N = int(input())

maze = [list(map(int, list(input())[:-1])) for _ in range(N)]

visited = [[[0] * N for _ in range(N)]]

min_v = 10000000000000

if maze[0][0]:
    dfs(0, 0, 0)
else:
    visited.append([[0] * N for _ in range(N)])
    dfs(0, 0, 1)

print(min_v)