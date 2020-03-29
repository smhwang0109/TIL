# BaekJoon IM

### 17144. 미세먼지 안녕!

```python
R, C, T = map(int,input().split())
room = []
room.append([-1]*(C+2))
for i in range(R):
    r = list(map(int, input().split()))
    room.append([-1]+r+[-1])
room.append([-1]*(C+2))
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for idx in range(1, R + 1):
    if room[idx][1] == -1:
        break


up_wind = []
for j in range(1, C + 1):
    up_wind.append([idx, j])
for i in range(1, idx):
    up_wind.append([idx - i, j])
for j in range(C - 1, 0, -1):
    up_wind.append([idx - i, j])
for i in range(2, idx + 1):
    up_wind.append([i, j])

idx += 1
down_wind = []
for j in range(1, C + 1):
    down_wind.append([idx, j])
for i in range(1, idx):
    down_wind.append([idx + i, j])
for j in range(C - 1, 0, -1):
    down_wind.append([idx + i, j])
for i in range(R-1, idx-1,-1):
    down_wind.append([i, j])


for s in range(T):
    # 확산
    temp_room = []
    for i in range(R+2):
        r = []
        for j in range(C+2):
            r.append(room[i][j])
        temp_room.append(r)
    for i in range(1,R+1):
        for j in range(1,C+1):
            if room[i][j] != 0 and room[i][j] != -1:
                p_count = 0
                for k in range(4):
                    if room[i+dx[k]][j+dy[k]] != -1:
                        temp_room[i + dx[k]][j + dy[k]] += int(room[i][j]/5)
                        p_count += 1
                temp_room[i][j] -= int(room[i][j]/5)*p_count
    room = []
    for i in range(R + 2):
        r = []
        for j in range(C + 2):
            r.append(temp_room[i][j])
        room.append(r)
    # 공기 청정기
    for i in range(1, len(up_wind)-1):
        if room[up_wind[i][0]][up_wind[i][1]] != 0:
            if i != len(up_wind)-2:
                temp_room[up_wind[i+1][0]][up_wind[i+1][1]] = room[up_wind[i][0]][up_wind[i][1]]
            if temp_room[up_wind[i][0]][up_wind[i][1]] != room[up_wind[i-1][0]][up_wind[i-1][1]]:
                    temp_room[up_wind[i][0]][up_wind[i][1]] = 0
    for i in range(1, len(down_wind)-1):
        if room[down_wind[i][0]][down_wind[i][1]] != 0:
            if i != len(down_wind) - 2:
                temp_room[down_wind[i + 1][0]][down_wind[i + 1][1]] = room[down_wind[i][0]][down_wind[i][1]]
            if temp_room[down_wind[i][0]][down_wind[i][1]] != room[down_wind[i-1][0]][down_wind[i-1][1]]:
                temp_room[down_wind[i][0]][down_wind[i][1]] = 0
    room = []
    for i in range(R + 2):
        r = []
        for j in range(C + 2):
            r.append(temp_room[i][j])
        room.append(r)


count = 0

for i in range(1,R+1):
    for j in range(1,C+1):
        if room[i][j] > 0:
            count += room[i][j]

print(count)
```

### 17135. 캐슬 디펜스

```python
from pprint import pprint
from copy import deepcopy

#공격
def attack(k, l):
    result = 0
    nearest = 1000000
    n_list = []
    for j in range(M):
        for i in range(N):
            if new_A[i][j] == 1:
                if abs(k-i) + abs(l-j) <= D and abs(k-i) + abs(l-j) < nearest:
                    nearest = abs(k-i) + abs(l-j)
                    n_list = []
                    n_list.append([i,j])
                elif abs(k-i) + abs(l-j) <= D and abs(k-i) + abs(l-j) < nearest:
                    n_list.append([i, j])
    min_j = 1000000
    for n in n_list:
        if n[1] < min_j:
            min_j = n[1]
            result = n
    if result:
        return  result

def down():
    for i in range(N-1,-1,-1):
        for j in range(M):
            if new_A[i][j] == 1:
                if i != N:
                    new_A[i+1][j] = new_A[i][j]
                new_A[i][j] = 0




N, M, D = map(int, input().split())

A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)
A.append([0]*M)
max_cnt = 0
# 궁수 [N,a], [N,b], [N,c]
for a in range(M-2):
    for b in range(a, M-1):
        for c in range(b, M):
            new_A = deepcopy(A)
            A_cnt = 0
            while True:
                att1 = attack(N, a)
                att2 = attack(N, b)
                att3 = attack(N, c)
                if att1:
                    new_A[att1[0]][att1[1]] = 0
                    A_cnt += 1
                if att2:
                    new_A[att2[0]][att2[1]] = 0
                    if att1 != att2:
                        A_cnt += 1
                if att3:
                    new_A[att3[0]][att3[1]] = 0
                    if att1 != att3 and att2 != att3:
                        A_cnt += 1
                down()
                cnt = 0
                for i in range(N):
                    if new_A[i].count(1):
                        cnt = 1
                        break
                if cnt == 0:
                    break
            if max_cnt < A_cnt:
                max_cnt = A_cnt
print(max_cnt)
```

### 15684. 사다리 조작

```python
import sys

def check(i,j, new_A):
    initial_j = j
    while i < 2*H+1:
        if new_A[i][j+1] == 1:
            j += 2
            i += 1
        elif new_A[i][j-1] == 1:
            j -= 2
            i += 1
        else:
            i += 1
    if initial_j == j:
        return 1
    else:
        return -1

def cnt_up1():
    for n in range(len(ladder_possible)):
        A[ladder_possible[n][0]][ladder_possible[n][1]] = 1
        for j in range(1,N*2,2):
            if check(1,j, A) == -1:
                A[ladder_possible[n][0]][ladder_possible[n][1]] = 0
                break
        else:
            return 1
    return -1

def cnt_up2():
    for n1 in range(len(ladder_possible)-1):
        for n2 in range(n1+1, len(ladder_possible)):
            if n1 != n2:
                A[ladder_possible[n1][0]][ladder_possible[n1][1]] = 1
                A[ladder_possible[n2][0]][ladder_possible[n2][1]] = 1
                for j in range(1,N*2,2):
                    if check(1,j, A) == -1:
                        A[ladder_possible[n2][0]][ladder_possible[n2][1]] = 0
                        break
                else:
                    return 2
        A[ladder_possible[n1][0]][ladder_possible[n1][1]] = 0
    return -1

def cnt_up3():
    for n1 in range(len(ladder_possible)-2):
        for n2 in range(n1+1,len(ladder_possible)-1):
            for n3 in range(n2+1,len(ladder_possible)):
                if n1 != n2 and n1 != n3 and n2 != n3:
                    A[ladder_possible[n1][0]][ladder_possible[n1][1]] = 1
                    A[ladder_possible[n2][0]][ladder_possible[n2][1]] = 1
                    A[ladder_possible[n3][0]][ladder_possible[n3][1]] = 1
                    for j in range(1,N*2,2):
                        if check(1,j, A) == -1:
                            A[ladder_possible[n3][0]][ladder_possible[n3][1]] = 0
                            break
                    else:
                        return 3
            A[ladder_possible[n2][0]][ladder_possible[n2][1]] = 0
        A[ladder_possible[n1][0]][ladder_possible[n1][1]] = 0
    return -1

N, M, H = map(int, sys.stdin.readline().split())
A = []

for i in range(H*2+2):
    A.append([0] + [1, 0]*N)

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    A[a*2][b*2] = 1
ladder_possible = []
for i in range(2,2*H+1,2):
    for j in range(2,2*N,2):
        if A[i][j] == 0 and A[i][j+2] == 0 and A[i][j-2] == 0:
            ladder_possible.append([i,j])
i = 1
result = -1
for j in range(1, N * 2, 2):
    if check(i, j, A) == -1:
        break
else:
    result = 0

if result != 0:
    result = cnt_up1()
    if result == -1:
        result = cnt_up2()
        if result == -1:
            result = cnt_up3()
print(result)
```

### 17070. 파이프 옮기기 1

```python
from _collections import deque
import sys

def check(s):
    temp = deque()
    if s[1] == '가로':
        if A[s[0][0]][s[0][1]+1] == 0:
            temp.append([[s[0][0],s[0][1]+1],'가로',s[2]])
        if A[s[0][0]][s[0][1]+1] == 0 and A[s[0][0]+1][s[0][1]] == 0 and A[s[0][0]+1][s[0][1]+1] == 0:
            temp.append([[s[0][0]+1, s[0][1] + 1], '대각선',s[2]])
    elif s[1] == '세로':
        if A[s[0][0]+1][s[0][1]] == 0:
            temp.append([[s[0][0]+1,s[0][1]],'세로',s[2]])
        if A[s[0][0]][s[0][1]+1] == 0 and A[s[0][0]+1][s[0][1]] == 0 and A[s[0][0]+1][s[0][1]+1] == 0:
            temp.append([[s[0][0]+1, s[0][1] + 1], '대각선',s[2]])
    elif s[1] == '대각선':
        if A[s[0][0]][s[0][1]+1] == 0:
            temp.append([[s[0][0],s[0][1]+1],'가로',s[2]])
        if A[s[0][0]+1][s[0][1]] == 0:
            temp.append([[s[0][0]+1,s[0][1]],'세로',s[2]])
        if A[s[0][0]][s[0][1]+1] == 0 and A[s[0][0]+1][s[0][1]] == 0 and A[s[0][0]+1][s[0][1]+1] == 0:
            temp.append([[s[0][0]+1, s[0][1] + 1], '대각선',s[2]])
    return temp

def BFS(s):
    cnt = 0
    stack = []
    stack.append(s)
    visited = []
    while True:
        check_list = check(s)
        for c in check_list:
            if c[0] == [N-1,N-1]:
                cnt += c[2]
            for v in stack:
                if v[:2] == c[:2]:
                    v[2] += c[2]
                    break
            else:
                stack.append(c)
                s = c
        stack.pop(0)
        if stack:
            s = stack[0]
        else:
            break
    return cnt



N = int(sys.stdin.readline())
A = deque()
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    A.append(a + [-1])
A.append([-1]*(N+1))
S = [[0,1],'가로',1]
print(BFS(S))

```

### 16637. 괄호 추가하기

```python
from copy import deepcopy

def Calculate(a,c,b):
    if c == '+':
        return int(a)+int(b)
    elif c == '-':
        return int(a)-int(b)
    elif c == '*':
        return int(a)*int(b)

def recursion(X):
    for i in range(0,len(X)-1):
        if i == 0:
            temp_sum = int(X[i])
        elif X[i] == '+':
            temp_sum += int(X[i+1])
        elif X[i] == '-':
            temp_sum -= int(X[i+1])
        elif X[i] == '*':
            temp_sum *= int(X[i+1])
    global max0
    if max0 < temp_sum:
        max0 = temp_sum
    for i in range(2,len(X)-1,2):
        temp = deepcopy(X)
        if type(temp[i+2]) == str and type(temp[i]) == str:
            temp[i] = Calculate(temp[i],temp[i+1],temp[i+2])
            temp.pop(i+1)
            temp.pop(i+1)
            recursion(temp)


N = int(input())
A = list(input())
result = []
max0 = -(2**31+1)
if len(A) == 1:
    print(A[0])
else:
    recursion(A)
    print(max0)


```

### 14499. 주사위 굴리기

```python
N, M, x, y, K = map(int, input().split())
m = []
D = {}
under = 6
over = 1
side = [5,3,2,4]
for i in range(1,7):
    D[i] = 0
for i in range(N):
    t = list(map(int, input().split()))
    m.append(t)
order = list(map(int, input().split()))
for o in order:
    #동
    if o == 1:
        if y+1 < M:
            temp_u = under
            temp_o = over
            under = side[1]
            over = side[3]
            side = [side[0], temp_o, side[2], temp_u]
            y += 1
            if m[x][y] != 0:
                D[under] = m[x][y]
                m[x][y] = 0
            else:
                m[x][y] = D[under]
            print(D[over])
    #서
    elif o == 2:
        if y-1 >= 0:
            temp_u = under
            temp_o = over
            under = side[3]
            over = side[1]
            side = [side[0], temp_u, side[2], temp_o]
            y -= 1
            if m[x][y] != 0:
                D[under] = m[x][y]
                m[x][y] = 0
            else:
                m[x][y] = D[under]
            print(D[over])
    #북
    elif o == 3:
        if x-1 >= 0:
            temp_u = under
            temp_o = over
            under = side[0]
            over = side[2]
            side = [temp_o, side[1], temp_u, side[3]]
            x -= 1
            if m[x][y] != 0:
                D[under] = m[x][y]
                m[x][y] = 0
            else:
                m[x][y] = D[under]
            print(D[over])
    #남
    elif o == 4:
        if x+1 < N:
            temp_u = under
            temp_o = over
            under = side[2]
            over = side[0]
            side = [temp_u, side[1], temp_o, side[3]]
            x += 1
            if m[x][y] != 0:
                D[under] = m[x][y]
                m[x][y] = 0
            else:
                m[x][y] = D[under]
            print(D[over])
```

### 17136. 색종이 붙이기

```python
import sys

def check(n, i, j,p):
    if i+n-1 < 10 and j+n-1 < 10:
        for k in range(n):
            if 0 in p[i+k][j:j+n]:
                return 0
        return 1
    return 0

def cover(n ,i, j, p):
    for k in range(n):
        for l in range(n):
            p[i + k][j + l] = 0

def recover(n ,i, j, p):
    for k in range(n):
        for l in range(n):
            p[i + k][j + l] = 1

def recursion(cnt, P, D, L):
    global result
    if L == 0:
        for i in range(10):
            if 1 in P[i]:
                return
        if result > cnt:
            result = cnt
            return
    else:
        for i in range(10):
            if 1 in P[i]:
                break
        else:
            if result > cnt:
                result = cnt
                return
    if cnt >= result:
        return
    for i in range(10):
        for j in range(10):
            if P[i][j] == 1:
                for l in range(5,0,-1):
                    if D[l] > 0:
                        if check(l, i, j, P) == 1:
                            cover(l, i, j, P)
                            D[l] -= 1
                            recursion(cnt + 1, P, D,l)
                            D[l] += 1
                            recover(l, i, j, P)
                return



P = []

for i in range(10):
    p = list(map(int, sys.stdin.readline().split()))
    P.append(p)

D = {}
for i in range(1,6):
    D[i] = 5

cnt = 0
result = 26
recursion(cnt, P, D, 5)
if result == 26:
    result = -1
print(result)
```

### 17281. ⚾

```python
from itertools import permutations
import sys

def play_game(o, n):
    e = 0
    player = 0
    out = 0
    cnt = 0
    score = 0
    i = 0
    while True:
        if N_list[e][o[i]] != 0 and N_list[e][o[i]] != 4:
            cnt += N_list[e][o[i]]
            player += 1
            if cnt >= 4:
                score += player-1
                cnt = N_list[e][o[i]]
                player = 1
        elif N_list[e][o[i]] == 4:
            player += 1
            score += player
            cnt = 0
            player = 0
        else:
            out += 1
            if out == 3:
                out = 0
                cnt = 0
                player = 0
                e += 1
                if e == n:
                    return score
        i += 1
        if i == 9:
            i = 0



N = int(sys.stdin.readline())
N_list = []
for n in range(N):
    N_list.append(list(map(int, sys.stdin.readline().split())))
order = []
for p in permutations(range(1, 9), 8):
    order.append(list(p)[:3] + [0] + list(p)[3:])
max0 = 0
for o in order:
    s = play_game(o,N)
    if max0 < s:
        max0 = s

print(max0)
```

### 17406. 배열 돌리기 4

```python
from itertools import permutations
from copy import deepcopy
import sys

def rotation(r,c,s):
    for n in range(1,s+1):
        for i in range(2*n):
            new_A[r - n - 1][c - n + i] = temp_A[r - n - 1][c - n - 1 + i]
            new_A[r - n + i][c + n - 1] = temp_A[r - n - 1 + i][c + n - 1]
            new_A[r + n - 1][c + n - i - 2] = temp_A[r + n - 1][c + n - 1 - i]
            new_A[r + n - i - 2][c - n - 1] = temp_A[r + n - 1 - i][c - n - 1]


N, M, K = map(int, sys.stdin.readline().split())

A = []
order = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
for _ in range(K):
    order.append(list(map(int, sys.stdin.readline().split())))

min0 = 1000000
for P in permutations(order, K):
    new_A = deepcopy(A)
    for p in P:
        temp_A = deepcopy(new_A)
        rotation(p[0], p[1], p[2])
    for a in new_A:
        s = sum(a)
        if min0 > s:
            min0 = s

print(min0)
```

### 17471. 게리맨더링

```python
from itertools import combinations
import sys

def check2(a, j, v):
    if a[0] in D[j]:
        return 1
    else:
        for k in D[j]:
            if k in a and k not in v:
                v.append(j)
                if check2(a, k, v) == 1:
                    return 1
        return -1

def check(a):
    for j in range(1, len(a)):
        visited = []
        if check2(a, a[j], visited) == -1:
            return -1
    return 1


input = sys.stdin.readline
D = {}

N = int(input())
population = [0] + list(map(int, input().split()))
S = sum(population)
for i in range(N):
    D[i+1] = list(map(int, input().split()))[1:]


min0 = 1000000
for n in range(1, N//2+1):
    for C in combinations(range(1,N+1), n):
        rest = list(range(1, N + 1))
        for c in C:
            rest.remove(c)
        if check(C) == 1 and check(rest) == 1:
            cnt = 0
            for i in C:
                cnt += population[i]
            sub = abs((S - cnt) - cnt)
            if min0 > sub:
                min0 = sub
if min0 == 1000000:
    min0 = -1
print(min0)

```

### 17492. 다리만들기 2

```python
import sys
from pprint import pprint
from copy import deepcopy

def find(initial_i,initial_j,cnt):
    m[initial_i][initial_j] = cnt
    for k in range(4):
        i = initial_i + di[k]
        j = initial_j + dj[k]
        if i >= 0 and i < N and j >= 0 and j < M:
            if m[i][j] == 1:
                find(i,j,cnt)

def find_spot(initial_i,initial_j, cnt):
    r = []
    for k in range(4):
        i = initial_i + di[k]
        j = initial_j + dj[k]
        if i >= 0 and i < N and j >= 0 and j < M:
            if m[i][j] == 0:
                b = make_bridge(i, j, k)
                if b:
                    r = [i,j,k,b[0],b[1]]
        if r:
            r.append(cnt)
            D_bridge[cnt].append(r)

def make_bridge(i,j,k):
    cnt = 0
    while True:
        if i >= 0 and i < N and j >= 0 and j < M:
            if m[i][j] == 0:
                i += di[k]
                j += dj[k]
                cnt += 1
            else:
                if cnt >= 2:
                    return [cnt, m[i][j]]
                return
        else:
            return

def BFS(cnt, final):
    if cnt >= final:
        result_check(result)
        return
    for d in D_bridge[cnt]:
        D[d[4]].append(d[5])
        D[d[5]].append(d[4])
        result.append(d)
        BFS(cnt+1, final)
        result.remove(d)
        D[d[4]].remove(d[5])
        D[d[5]].remove(d[4])

def result_check(result):
    global minv
    for j in range(3, cnt):
        v = []
        if not check(j, v):
            return
    else:
        for i in range(len(result)):
            D[result[i][5]].remove(result[i][4])
            D[result[i][4]].remove(result[i][5])
            for j in range(3, cnt):
                v = []
                if not check(j, v):
                    break
            else:
                D[result[i][5]].append(result[i][4])
                D[result[i][4]].append(result[i][5])
                d = result.pop(i)
                r_cnt = 0
                for k in result:
                    r_cnt += k[3]
                if minv > r_cnt:
                    minv = r_cnt
                result.insert(i,d)
                return
            D[result[i][5]].append(result[i][4])
            D[result[i][4]].append(result[i][5])
        r_cnt = 0
        for k in result:
            r_cnt += k[3]
        if minv > r_cnt:
            minv = r_cnt
        return

def check(j, v):
    if 2 in D[j]:
        return True
    else:
        for i in D[j]:
            if i not in v:
                v.append(j)
                if check(i,v):
                    return True
        return False


input = sys.stdin.readline

N, M = map(int, input().split())
m = []

for _ in range(N):
    m.append(list(map(int, input().split())))

di = [1,-1,0,0]
dj = [0,0,1,-1]
D = {}
D_bridge = {}
cnt = 2
for i in range(N):
    for j in range(M):
        if m[i][j] == 1:
            find(i,j,cnt)
            D[cnt] = []
            D_bridge[cnt] = []
            cnt += 1
final = cnt
R = []
for i in range(N):
    for j in range(M):
        if m[i][j] != 0:
            find_spot(i,j, m[i][j])

minv = 100000
for d in D_bridge:
    if not d:
        minv = -1
        break
else:
    result = []
    f_result = []
    BFS(2, final)
if minv == 100000:
    minv = -1
print(minv)
```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```

### 

```python

```







