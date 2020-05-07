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

