import sys
from collections import deque


def solution():

    def bfs(R, C):
        fire_que = deque(fire_list)
        J_que = deque([J])
        cnt = 0
        while J_que:
            temp_fire_que = deque()
            while fire_que:
                i, j = fire_que.popleft()
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < R and 0 <= nj < C and maze[ni][nj] != '#' and maze[ni][nj] != 'F':
                        temp_fire_que.append([ni, nj])
                        maze[ni][nj] = 'F'
            fire_que = temp_fire_que

            temp_J_que = deque()
            while J_que:
                i, j = J_que.popleft()
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if ni < 0 or ni >= R or nj < 0 or nj >= C:
                        return cnt + 1
                    elif 0 <= ni < R and 0 <= nj < C and maze[ni][nj] == '.':
                        temp_J_que.append([ni, nj])
                        maze[ni][nj] = 'F'
            J_que = temp_J_que
            cnt += 1
        return "IMPOSSIBLE"

    R, C = map(int, input().split())
    maze = [list(input()) for _ in range(R)]
    fire_list = []
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
                J = [i, j]
            elif maze[i][j] == 'F':
                fire_list.append([i, j])
    return bfs(R, C)




input = lambda : sys.stdin.readline().rstrip()

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

print(solution())