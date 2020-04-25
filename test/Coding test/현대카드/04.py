from collections import deque
from pprint import pprint

def check_bomb(M, i, j):
    print(i,j)
    color = M[i][j]
    cnt = 0
    que = deque()
    que.append([i,j])
    temp = []
    while que:
        i, j = que.popleft()
        if len(temp) < 3:
            temp.append([i, j])
            for k in range(4):
                if 0 <= i + di[k] and i + di[k] < 6 and 0 <= j + dj[k] and j + dj[k] < 6:
                    print('여기', i+di[k], j+dj[k], M[i+di[k]][j+dj[k]], color, temp, que)
                    if M[i+di[k]][j+dj[k]] == color and [i+di[k], j+dj[k]] not in temp and [i+di[k], j+dj[k]] not in que:
                        print(que)
                        print(cnt)
                        que.append([i+di[k], j+dj[k]])
        else:
            M[i][j] = 0
            for k in range(4):
                if 0 <= i + di[k] and i + di[k] < 6 and 0 <= j + dj[k] and j + dj[k] < 6:
                    if M[i + di[k]][j + dj[k]] == color:
                        que.append([i + di[k], j + dj[k]])
        if len(temp) == 3:
            for t in temp:
                M[t[0]][t[1]] = 0
            print('여기')
            pprint(M)
            temp = []



def solution(macaron):
    answer = []
    M = [[0]*6 for _ in range(6)]
    for m in macaron:
        if M[5][m[0]-1] == 0:
            M[5][m[0]-1] = m[1]
        else:
            for i in range(6):
                if M[i][m[0]-1]:
                    M[i-1][m[0]-1] = m[1]
                    break
        pprint(M)
        for i in range(6):
            for j in range(6):
                if M[i][j]:
                    check_bomb(M, i, j)
    pprint(M)
    return answer

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

solution([[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4]])