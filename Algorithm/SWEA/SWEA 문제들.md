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

