# Programmers Lv.3~4

### 종이접기

```python
def solution(n):
    answer = [0] * (2**n - 1)
    l = 2**n - 1
    for i in range(1, n+1):
        idx = 2**(n-i) -1
        interval = 2**(n-i+1)
        val = 0
        while True:
            if idx < l:
                if val:
                    answer[idx] = 1
                    val = 0
                else:
                    answer[idx] = 0
                    val = 1
                idx += interval
            else:
                break

    return answer


print(solution(20))
```

```python
# 다른 사람 풀이
def solution(n):
    fold = 0
    arr = [fold]

    for i in range(n - 1):
        arr = arr + [fold] + [bit ^ 1 for bit in arr[::-1]]

    return arr
```



### 추석 트래픽

```python
def solution(lines):
    global answer
    answer = 1
    L = []
    for line in lines:
        # [시작초, 끝초]
        l = []
        new = line.split()
        s = int(new[1][:2]) * 3600 + int(new[1][3:5]) * 60 + int(new[1][6:8])
        s = 1000*s + int(new[1][9:])
        T = new[2][0:-1].split('.')
        if len(T) == 2:
            T = 1000*int(T[0]) + int(T[1])
        else:
            T = 1000*int(T[0])
        start = s - T + 1
        l.append(start)
        end = s + 1000
        l.append(end)
        L.append(l)
    for i in range(len(L)):
        cnt = 1
        for j in range(i+1, len(L)):
            if L[j][0] < L[i][1]:
                cnt += 1
        if answer < cnt:
            answer = cnt

    return answer

print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))
```



### 지형 이동 (아직)

```python
from collections import deque
import heapq

def BFS(i, j):
    global answer, l, N, M, h, heap
    q = deque()
    q.append([i, j])
    while q:
        i, j = q.popleft()
        M[i][j] = -1
        for k in range(4):
            new_i = i + di[k]
            new_j = j + dj[k]
            if 0 <= new_i < N and 0 <= new_j < N:
                if M[new_i][new_j] != -1:
                    val = abs(l[new_i][new_j] - l[i][j])
                    if val <= h:
                        q.append([new_i, new_j])
                    else:
                        if M[new_i][new_j] == 0 or M[new_i][new_j] > val:
                            M[new_i][new_j] = val
                            heapq.heappush(heap, [val, new_i, new_j])
    print(M)
    while heap:
        val, i, j = heapq.heappop(heap)
        if M[i][j] != -1:
            answer += M[i][j]
            BFS(i, j)
            return


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def solution(land, height):
    global answer, l, N, M, h, heap
    answer = 0
    l = land
    h = height
    heap = [] # [옆칸과의 차이, i, j]
    N = len(land)
    M = [[0] * N for _ in range(N)]
    BFS(0, 0)
    return answer

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))
```

```python
from collections import deque
import heapq

def BFS(i, j, group):
    global l, N, M, h
    q = deque()
    q.append([i, j])
    while q:
        i, j = q.popleft()
        M[i][j] = group
        for k in range(4):
            new_i = i + di[k]
            new_j = j + dj[k]
            if 0 <= new_i < N and 0 <= new_j < N:
                if not M[new_i][new_j]:
                    val = abs(l[new_i][new_j] - l[i][j])
                    if val <= h:
                        q.append([new_i, new_j])

def check():
    global l, N, M, D
    for i in range(N):
        for j in range(N):
            for k in range(4):
                new_i = i + di[k]
                new_j = j + dj[k]
                if 0 <= new_i < N and 0 <= new_j < N:
                    if M[new_i][new_j] != M[i][j]:
                        D[M[i][j]].append([abs(l[new_i][new_j] - l[i][j]), M[new_i][new_j]])
                        D[M[new_i][new_j]].append([abs(l[new_i][new_j] - l[i][j]), M[i][j]])


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def solution(land, height):
    global l, N, M, h, D
    answer = 0
    l = land
    h = height
    heap = [] # [옆칸과의 차이, i, j]
    N = len(land)
    M = [[0] * N for _ in range(N)]
    group = 1
    for i in range(N):
        for j in range(N):
            if not M[i][j]:
                BFS(i, j, group)
                group += 1
    D = {k:[] for k in range(1, group)}
    check()
    heap = D[1]
    visited = [0] * group
    visited[1] = 1
    while heap:
        val, node = heapq.heappop(heap)
        if not visited[node]:
            answer += val
            visited[node] = 1
            for n in D[node]:
                heapq.heappush(heap, n)

    return answer

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))
```



### N으로 표현

```python
def solution(N, number):
    s = str(N)
    if N == number:
        return 1
    L = [0, {N}]
    for i in range(2, 9):
        temp_set = {int(s*i)}
        for j in range(1, i//2 + 1):
            for k in L[j]:
                for l in L[i - j]:
                    temp_set.add(k+l)
                    temp_set.add(k-l)
                    temp_set.add(l-k)
                    temp_set.add(k*l)
                    if k:
                        temp_set.add(l//k)
                    if l:
                        temp_set.add(k//l)
        if number in temp_set:
            return i
        L.append(temp_set)
    return -1

print(solution(5 ,12))
print(solution(2 ,11))
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





