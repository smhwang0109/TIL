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





