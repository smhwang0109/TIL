# Graph

## SWEA

### 1267. 작업순서

```python
def DFS(s):
    p = 1
    for i in rev[s]:
        if visited[i] == 0:
            p = 0
    if p == 1:
        if visited[s] == 0:
            visited[s] = 1
            print('',s, end= '')
        for i in D[s]:
            DFS(i)



T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # D는 1부터 시작
    D = [[] for _ in range(V+1)]
    rev = [[] for _ in range(V+1)]
    L = list(map(int, input().split()))
    visited = [0]*(V+1)
    for i in range(0, len(L), 2):
        D[L[i]].append(L[i+1])
        rev[L[i+1]].append(L[i])
    start = []
    for i in range(1, V+1):
        if not rev[i]:
            start.append(i)
    print('#{}'.format(tc),end='')
    for a in start:
        DFS(a)
    print()
```

## Baekjoon

### 1260. DFS와 BFS

```python
from collections import deque

def DFS(s):
    stack = deque()
    visited = [0] * (N+1)
    stack.append(s)
    visited[s] = 1
    print(s,end='')
    while True:
        for i in D[s]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                s = i
                print('', s, end='')
                break
        else:
            stack.pop()
            if stack:
                s = stack[-1]
            else:
                break
def BFS(s):
    stack = deque()
    visited = [0] * (N + 1)
    stack.append(s)
    visited[s] = 1
    print(s, end='')
    while True:
        for i in D[s]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                s = i
                print('', s, end='')
        else:
            stack.popleft()
            if stack:
                s = stack[0]
            else:
                break

N, M, V = map(int, input().split())
D = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    D[n1].append(n2)
    D[n2].append(n1)
for i in range(1, N+1):
    D[i].sort()
DFS(V)
print()
BFS(V)
```

### 2606. 바이러스

```python
def DFS(s):
    stack = []
    visited = [0]*(N+1)
    visited[s] = 1
    stack.append(s)
    cnt = 0
    while True:
        for i in D[s]:
            if visited[i] == 0:
                visited[i] = 1
                stack.append(i)
                cnt += 1
                s = i
                break
        else:
            stack.pop()
            if stack:
                s = stack[-1]
            else:
                break
    return cnt


N = int(input())
V = int(input())
D = [[] for _ in range(N+1)]

for _ in range(V):
    n1, n2 = map(int, input().split())
    D[n1].append(n2)
    D[n2].append(n1)
print(DFS(1))

```

```python
def BFS(s):
    stack = deque()
    visited = [0]*(N+1)
    visited[s] = 1
    stack.append(s)
    cnt = 0
    while True:
        for i in D[s]:
            if visited[i] == 0:
                visited[i] = 1
                stack.append(i)
                cnt += 1
                s = i
        else:
            stack.popleft()
            if stack:
                s = stack[0]
            else:
                break
    return cnt

from _collections import deque

N = int(input())
V = int(input())
D = [[] for _ in range(N+1)]

for _ in range(V):
    n1, n2 = map(int, input().split())
    D[n1].append(n2)
    D[n2].append(n1)
print(BFS(1))

```

### 2667. 단지번호붙이기

```python
from _collections import deque

def BFS(i,j):
    M[i][j] = 2
    stack = deque()
    h_cnt = 1
    while True:
        for k in range(4):
            if M[i+di[k]][j+dj[k]] == 1:
                h_cnt += 1
                stack.append([i+di[k], j+dj[k]])
                M[i+di[k]][j+dj[k]] = 2
        if stack:
            s = stack.popleft()
            i = s[0]
            j = s[1]
        else:
            break

    return h_cnt

di = [1,-1,0,0]
dj = [0,0,1,-1]
N = int(input())
M = [[0]*(N+2)]
for i in range(N):
    m = list(map(int,list(input())))
    M.append([0] + m + [0])
M.append([0]*(N+2))
cnt = 0
result = []
for i in range(1,N+1):
    for j in range(1,N+1):
        if M[i][j] == 1:
            cnt += 1
            result.append(BFS(i,j))
result = sorted(result)
print(cnt)
for r in result:
    print(r)
```

### 1012. 유기농 배추

```python
from _collections import deque

def BFS(i,j):
    A[i][j] = 2
    stack = deque()
    while True:
        for k in range(4):
            if A[i+di[k]][j+dj[k]] == 1:
                stack.append([i+di[k], j+dj[k]])
                A[i+di[k]][j+dj[k]] = 2
        if stack:
            s = stack.popleft()
            i = s[0]
            j = s[1]
        else:
            break


di = [1,-1,0,0]
dj = [0,0,1,-1]

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int,input().split())
    A = [[0]*(M+2) for _ in range(N+2)]
    for _ in range(K):
        j, i = map(int, input().split())
        A[i+1][j+1] = 1
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if A[i][j] == 1:
                cnt += 1
                BFS(i,j)
    print(cnt)
```

### 2178. 미로 탐색

```python
from _collections import deque
import sys

def search(i, j, cnt):
    global N, M
    for k in range(4):
        if 0 <= i+di[k] < N and 0 <= j+dj[k] < M:
            if maze[i+di[k]][j+dj[k]] == 1 and visited[i+di[k]][j+dj[k]] == 0:
                visited[i + di[k]][j + dj[k]] = 1
                que.append([i+di[k], j+dj[k], cnt+1])

que = deque()
di = [1,-1,0,0]
dj = [0,0,1,-1]

input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, list(input())[:-1])))
que.append([0,0,1])
visited = [[0]*M for _ in range(N)]
while que:
    i, j, cnt = que.popleft()
    if i == N - 1 and j == M - 1:
        result = cnt
        break
    search(i, j, cnt)
print(result)
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

