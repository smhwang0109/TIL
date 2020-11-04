# SW Expert Academy Algorithm D5

### 1247. 최적 경로

```python
def route(cur, s, cnt):
    global N, sumv
    if s >= sumv:
        return
    if cnt == N:
        s += abs(cur[0] - end[0]) + abs(cur[1] - end[1])
        if sumv > s:
            sumv = s
        return
    for i in range(len(L)):
        if visited[i]: continue
        visited[i] = 1
        route(L[i], s + abs(cur[0] - L[i][0]) + abs(cur[1] - L[i][1]), cnt + 1)
        visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    L = []
    l = list(map(int, input().split()))
    sumv = float('inf')
    for i in range(N + 2):
        if i == 0:
            start = (l[i], l[i + 1])
        elif i == 1:
            end = (l[2 * i], l[2 * i + 1])
        else:
            L.append((l[2 * i], l[2 * i + 1]))
    visited = [0] * len(L)
    route(start, 0, 0)
    print('#{} {}'.format(tc, sumv))
```

### 1248. 공통 조상

```python
def find_parent(n, parent_list):
    parent = tree[n][2]
    if parent:
        parent_list.append(parent)
        return find_parent(parent, parent_list)
    else:
        return parent_list

def count_sun(n):
    global cnt
    if tree[n][0]:
        if tree[n][1]:
            cnt += 1
            count_sun(tree[n][1])
        cnt += 1
        count_sun(tree[n][0])
    else:
        return



T = int(input())
for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    L = list(map(int, input().split()))
    #   왼쪽 오른쪽 부모
    # 1
    # 2
    # 3
    tree = [[0]*3 for _ in range(V+1)]
    for i in range(E):
        parent = L[2*i]
        sun = L[2*i + 1]
        if not tree[parent][0]:
            tree[parent][0] = sun
        else:
            tree[parent][1] = sun
        tree[sun][2] = parent

    parent_list1 = find_parent(n1, [])
    parent_list2 = find_parent(n2, [])
    minv = min(len(parent_list1), len(parent_list2))
    for k in range(1, minv+1):
        if parent_list1[-k] != parent_list2[-k]:
            result = parent_list1[-k+1]
            break
    else:
        result = minv
    cnt = 1
    count_sun(result)
    print('#{} {} {}'.format(tc, result, cnt))
```

### 5521. 상원이의 생일파티

```python
from collections import deque

def find():
    q = deque()
    q.append([1, 0])
    visited[1] = 1
    cnt = 0
    while q:
        n, bridge = q.popleft()
        if bridge == 2:
            continue
        for i in F[n]:
            if not visited[i]:
                visited[i] = 1
                q.append([i, bridge + 1])
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    F = [0]
    for n in range(N):
        F.append([])
    visited = [0] * (N+1)
    for m in range(M):
        a, b = map(int, input().split())
        F[a].append(b)
        F[b].append(a)
    print("#{} {}".format(tc, find()))
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





