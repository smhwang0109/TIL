# SW Expert Academy Algorithm D4

### 1210. Ladder1

```python
T = 10
for case in range(1, T+1):
    tc = input()
    L = []
    for i in range(100):
        l = list(map(int, input().split()))
        L.append([0] + l + [0])
    L.append([0]*102)

    for j in range(1,101):
        if L[0][j] == 1:
            initial = j
            i = 0
            while i < 99:
                if L[i][j+1] == 1:
                    for k in range(j+1,102):
                        if L[i][k] == 0:
                            break
                    j = k-1
                    i += 1
                elif L[i][j-1] == 1:
                    for k in range(j-1,-1,-1):
                        if L[i][k] == 0:
                            break
                    j = k+1
                    i += 1
                elif L[i+1][j] == 1:
                    i += 1
                elif L[i+1][j] == 2:
                    i += 1
                    result = initial
    print('#{} {}'.format(case, result-1))
```

### 1211. Ladder2

```python
T = 10
for case in range(1, T+1):
    tc = input()
    L = []
    for i in range(100):
        l = list(map(int, input().split()))
        L.append([0] + l + [0])
    L.append([0]*102)
    min0 = 1000000
    for j in range(1,102):
        if L[0][j] == 1:
            initial = j
            i = 0
            cnt = 0
            while i < 99:
                if L[i][j+1] == 1:
                    for k in range(j+1,102):
                        if L[i][k] == 0:
                            break
                    cnt += k - j
                    j = k-1
                    i += 1
                elif L[i][j-1] == 1:
                    for k in range(j-1,-1,-1):
                        if L[i][k] == 0:
                            break
                    cnt += j - k
                    j = k+1
                    i += 1
                elif L[i+1][j] == 1:
                    i += 1
                    cnt += 1
            if min0 >= cnt:
                min0 = cnt
                result = initial
    print('#{} {}'.format(case, result-1))
```

### 1258. 행렬찾기

```python
T = int(input())
for case in range(1, T+1):
    n = int(input())
    M = []
    M.append([0]*(n+2))
    for i in range(n):
        m = list(map(int, input().split()))
        M.append([0]+m+[0])
    M.append([0]*(n+2))
    all_cnt = {}
    for i in range(1,n+1):
        for j in range(1,n+1):
            if M[i][j] != 0 and M[i][j-1] == 0 and M[i-1][j] == 0:
                c_i = i
                c_j = j
                while True:
                    if M[i][c_j] == 0:
                        j_cnt = c_j-j
                        break
                    else:
                        c_j += 1
                while True:
                    if M[c_i][j] == 0:
                        i_cnt = c_i-i
                        break
                    else:
                        c_i += 1
                all_cnt[i_cnt] = j_cnt
    result = {}
    for key,value in all_cnt.items():
        if key*value not in result:
            result[key*value] = [[key,value]]
        else:
            result[key*value].append([key,value])
    temp = []
    for key in result.keys():
        if temp == []:
            temp.append(key)
        else:
            for i in range(len(temp)):
                if temp[i] > key:
                    temp.insert(i,key)
                    break
            if key not in temp:
                temp.append(key)
    print('#{} {}'.format(case,len(all_cnt)),end='')
    for i in temp:
        if len(result[i]) > 1:
            temp2 = []
            for j in result[i]:
                if temp2 == []:
                    temp2.append(j)
                else:
                    for i2 in range(len(temp2)):
                        if temp2[i2][0] > j[0]:
                            temp2.insert(i2, j)
                    if j not in temp2:
                        temp2.append(j)
            for t in temp2:
                print(' {} {}'.format(t[0],t[1]),end='')
        else:
            print(' {} {}'.format(result[i][0][0],result[i][0][1]),end='')
    print()

```

### 1486. 장훈이의 높은 선반

```python
from itertools import combinations

T = int(input())
for case in range(1, T+1):
    N, B = map(int,input().split())
    l = list(map(int,input().split()))
    minv = 1000000
    for n in range(1, N+1):
        for k in combinations(l,n):
            s = sum(k)
            if s >= B and minv > s:
                minv = s
    print('#{} {}'.format(case, minv-B))


```

### 1861. 정사각형 방

```python
def check(cnt, i, j):
    for k in range(4):
        if i + di[k] >= 0 and i + di[k] < N and j + dj[k] >= 0 and j + dj[k] < N:
            if rooms[i][j] + 1 == rooms[i+di[k]][j+dj[k]]:
                return check(cnt+1, i+di[k], j+dj[k])
    return cnt


T = int(input())
for case in range(1, T+1):
    N = int(input())
    rooms = []
    for _ in range(N):
        rooms.append(list(map(int,input().split())))
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            cnt = check(1, i, j)
            if max_cnt < cnt:
                minv = rooms[i][j]
                max_cnt = cnt
            elif max_cnt == cnt:
                if minv > rooms[i][j]:
                    minv = rooms[i][j]
    print('#{} {} {}'.format(case, minv, max_cnt))
```

### 1865. 동철이의 일 분배

```python
def recursion(i, N, S):
    global  maxv
    if maxv >= S*100:
        return
    if i == N:
        if maxv < S*100:
            maxv = S*100
        return
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            recursion(i+1, N, S*P[i][j]*10**-2)
            v[j] = 0

T = int(input())
for case in range(1, T+1):
    N = int(input())
    P = []
    for _ in range(N):
        P.append(list(map(int, input().split())))
    v = [0]*N
    S = 1
    maxv = 0
    recursion(0, N, S)
    print('#{} %.6f'.format(case) %round(maxv, 6))

```

### 2819. 격자판의 숫자 이어 붙이기

```python
def check(i, j, n, S):
    if n == 7:
        result.add(S)
        final.add(S)
        return
    for k in range(4):
        if i + di[k] >= 0 and i + di[k] < 4 and j + dj[k] >= 0 and j + dj[k] < 4:
            S = S[:n]
            if type(M[i+di[k]][j+dj[k]]) == set:
                for m in M[i+di[k]][j+dj[k]]:
                    S = S[:n] + m[:7-n]
                    result.add(S)
                    final.add(S)
            else:
                check(i + di[k], j + dj[k], n+1, S + M[i+di[k]][j+dj[k]])

di = [1,-1,0,0]
dj = [0,0,1,-1]

T = int(input())
for case in range(1, T+1):
    M = []
    for _ in range(4):
        M.append(input().split())
    final = set()
    for i in range(4):
        for j in range(4):
            S = M[i][j]
            result = set()
            check(i, j, 1, S)
            M[i][j] = result
    print('#{} {}'.format(case, len(final)))
```

### 3752. 가능한 시험 점수

```python
from copy import deepcopy

def use(D, S):
    print(D)
    print(S)
    score.add(S)
    if sum(D.values()) != 0:
        for n in D.keys():
            temp = deepcopy(D)
            while temp[n]:
                temp[n] -= 1
                print('S =', S)
                print('n =', n)
                use(temp, S+n)
                use(temp, S)




T = int(input())
for case in range(1, T+1):
    D = {}
    N = int(input())
    for n in map(int, input().split()):
        if n not in D:
            D[n] = 1
        else:
            D[n] += 1
    score = {0}
    S = 0
    use(D, S)
    print(score)

```

### 1249. 보급로

```python
import heapq

def BFS():
    q = []
    heapq.heappush(q, [0, 0, 0])
    visited[0][0] = 1
    while q:
        cnt, i, j = heapq.heappop(q)
        if M[i][j] == 0:
            for k in range(4):
                n_i = i + di[k]
                n_j = j + dj[k]
                if n_i == N - 1 and n_j == N - 1:
                    return cnt
                if 0 <= n_i < N and 0 <= n_j < N:
                    if not visited[n_i][n_j]:
                        visited[n_i][n_j] = 1
                        heapq.heappush(q, [cnt, n_i, n_j])
        else:
            M[i][j] -= 1
            heapq.heappush(q, [cnt+1, i, j])




di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    print("#{} {}".format(tc, BFS()))

```

### 1251. 하나로

```python
import heapq

def prim(i):
    global N
    q = []
    dist = 0
    for n in range(1, N):
        heapq.heappush(q, [D[i][n], n])
    i = 0
    while q:
        temp_dist, n = heapq.heappop(q)
        if visited[n] == -1:
            visited[n] = i
            dist += temp_dist
            i = n
            for n in range(1, N):
                if i == n and visited[n] != -1: continue
                heapq.heappush(q, [D[min(i, n)][max(i, n)], n])
    return dist

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    D = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            D[i][j] = (X[i] - X[j])**2 + (Y[i] - Y[j])**2
    visited = [-1] * N
    visited[0] = 0
    E = float(input())
    print('#{} {}'.format(tc, round(E * prim(0))))
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





