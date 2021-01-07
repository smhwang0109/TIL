from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

# field = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]

field = []

que = deque()
cnt = 0

for h in range(H):
    temp_field = []
    for n in range(N):
        temp_field.append(list(map(int, input().split())))
        for m in range(M):
            if temp_field[n][m] == 1:
                que.append([h, n, m])
    field.append(temp_field)

dh = [1, -1, 0, 0, 0, 0]
dn = [0, 0, 1, -1, 0, 0]
dm = [0, 0, 0, 0, 1, -1]


# for h in range(H):
#     for n in range(N):
#         for m in range(M):
#             if field[h][n][m] == 1:
#                 que.append([h, n, m, 0])

while que:
    h, n, m = que.popleft()
    cnt = field[h][n][m]
    for d_idx in range(6):
        nh = h + dh[d_idx]
        nn = n + dn[d_idx]
        nm = m + dm[d_idx]
        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and not field[nh][nn][nm]:
            que.append([nh, nn, nm])
            field[nh][nn][nm] = cnt + 1

if cnt:
    cnt -= 1

for h in range(H):
    for n in range(N):
        for m in range(M):
            if not field[h][n][m]:
                cnt = -1
                break
        if cnt == -1:
            break
    if cnt == -1:
        break

print(cnt)
