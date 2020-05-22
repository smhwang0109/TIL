# SWEA 문제들

### 5185. 이진수

```python
T = int(input())
for tc in range(1, T+1):
    L, value = input().split()
    result = ''
    for v in value:
        B = str(format(int(v, 16), 'b'))
        if len(B) < 4:
            for i in range(4-len(B)):
                B = '0' + B
        result += B
    print('#{} {}'.format(tc, result))
```



### 5186. 이진수2

```python
T = int(input())
for tc in range(1, T+1):
    n = float(input())
    result = ''
    while n:
        n = n*2
        result += str(int(n))
        n %= 1
        if len(result) > 12:
            result = 'overflow'
            break
    print('#{} {}'.format(tc, result))
```



### 5188. 최소합

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    D = [[0]*N for _ in range(N)]
    D[0][0] = M[0][0]
    for i in range(N):
        for j in range(N):
            if i-1 >= 0 and j-1 >= 0:
                D[i][j] = min(D[i-1][j], D[i][j-1]) + M[i][j]
            elif i-1 >= 0:
                D[i][j] = D[i-1][j] + M[i][j]
            elif j-1 >= 0:
                D[i][j] = D[i][j-1] + M[i][j]
    print('#{} {}'.format(tc, D[N-1][N-1]))
```



### 5189. 전자카트

```python
from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    L = [n for n in range(2, N+1)]
    result = []
    for c in permutations(L, N-1):
        temp = list(c)
        temp.insert(0, 1)
        temp.append(1)
        result.append(temp)
    minv = 100000
    for r in result:
        sumv = 0
        for i in range(len(r)-1):
            sumv += M[r[i]-1][r[i+1]-1]
            if minv < sumv:
                break
        else:
            if minv >= sumv:
                minv = sumv
    print('#{} {}'.format(tc, minv))
```



### 5201. 컨테이너 운반

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    new_w = list(reversed(sorted(w)))
    new_t = list(reversed(sorted(t)))
    sumv = 0
    temp = 0
    for t in new_t:
        for i in range(temp, len(new_w)):
            if t >= new_w[i]:
                sumv += new_w[i]
                break
        temp = i+1
    print('#{} {}'.format(tc, sumv))
```



### 5202. 화물도크

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    new_L = sorted(L, key=lambda l: l[1])
    cnt = 1
    S = new_L[0]
    for i in range(1, N):
        if new_L[i][0] >= S[1]:
            S = new_L[i]
            cnt += 1

    print('#{} {}'.format(tc, cnt))
```



### 5203. 베이비진 게임

```python
def check():
    for i in range(len(L)):
        if i%2:
            p2[L[i]] += 1
            if i >= 5:
                for j in range(len(p2)):
                    if p2[j] >= 3:
                        return 2
                    if p2[j] >= 1:
                        if j + 1 <= 9 and p2[j+1] >= 1:
                            if j + 2 <= 9 and p2[j+2] >= 1:
                                return 2
        else:
            p1[L[i]] += 1
            if i >= 4:
                for j in range(len(p1)):
                    if p1[j] >= 3:
                        return 1
                    if p1[j] >= 1:
                        if j + 1 <= 9 and p1[j+1] >= 1:
                            if j + 2 <= 9 and p1[j+2] >= 1:
                                return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    L = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    print('#{} {}'.format(tc, check()))
```



### 5207. 이진 탐색

```python
def check(l, r, n, d):
    m = (l+r)//2
    if n == A[m]:
        return True
    elif A[m] > n and d !='left':
        return check(l, m-1, n, 'left')
    elif A[m] < n and d !='right':
        return check(m+1, r, n, 'right')
    return False


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    sumv = 0
    for n in B:
        if check(0, N-1, n, -1):
            sumv += 1
    print('#{} {}'.format(tc, sumv))
```



### 5209. 최소생산비용

```python
def solution(i, visited, sumv):
    global N, minv
    if sumv >= minv:
        return
    if i >= N:
        minv = sumv
        return
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            solution(i+1, visited, sumv+L[i][j])
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minv = 99 * N
    solution(0, visited, 0)
    print('#{} {}'.format(tc, minv))
```



### 5247. 연산

```python
from collections import deque

def BFS(n):
    global M
    visited[n] = 1
    que = deque()
    que.append(n)
    while que:
        n = que.popleft()
        if n == M:
            return visited[n] - 1
        a = n + 1
        b = n - 1
        c = n * 2
        d = n - 10
        for i in [a, b, c, d]:
            if 0 < i <= 1000000 and not visited[i]:
                que.append(i)
                visited[i] = visited[n] +1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    result = BFS(N)
    print('#{} {}'.format(tc, result))

```



### 5248. 그룹 나누기

```python
from collections import deque

def make(n):
    que = deque()
    que.append(n)
    while que:
        n = que.popleft()
        for v in V[n]:
            if not visited[v]:
                que.append(v)
                visited[v] = 1
                
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    V = [[] for _ in range(N+1)]
    L = list(map(int, input().split()))
    visited = [0] * (N+1)
    for i in range(0, 2*M, 2):
        n1 = L[i]
        n2 = L[i+1]
        V[n1].append(n2)
        V[n2].append(n1)

    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            make(i)
            cnt += 1

    print('#{} {}'.format(tc, cnt))

```



### 5249. 최소 신장 트리

```python
import heapq

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    D = {v:[] for v in range(V+1)}
    L = [list(map(int, input().split())) for _ in range(E)]
    key = [float('INF')] * (V+1)
    MST = [0] * (V+1)
    for s,e,c in L:
        D[s].append((e, c))
        D[e].append((s, c))
    pq = []
    heapq.heappush(pq, (0, 0))
    result = 0
    while pq:
        C, node = heapq.heappop(pq)
        if MST[node]: continue
        MST[node] = 1
        result += C
        minv = float('INF')
        for n, c in D[node]:
            if not MST[n] and key[n] > c:
                key[n] = c
                heapq.heappush(pq, (c, n))
    print('#{} {}'.format(tc, result))
```



### 5251. 최소 이동 거리

```python
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    D = {i:[] for i in range(N+1)}
    for i in range(E):
        s, e, c = map(int, input().split())
        D[s].append([e, c])

    dist = [float('inf')] * (N+1)
    visited = [0] * (N+1)
    dist[0] = 0
    cnt = 0
    while cnt < N+1:
        minv = float('inf')
        for i in range(N+1):
            if not visited[i] and dist[i] < minv:
                minv = dist[i]
                u = i
        cnt += 1
        visited[u] = 1
        for w, cost in D[u]:
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost
    print('#{} {}'.format(tc, dist[N]))

```

