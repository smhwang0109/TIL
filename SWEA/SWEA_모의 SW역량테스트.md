# SW Expert Academy Algorithm 모의

### 1952. 수영장

```python
from copy import deepcopy

def check(i, temp):
    final_price = deepcopy(temp)
    if i == 10:
        global minv
        s = sum(final_price)
        if minv > s:
            minv = s
        return
    if type(final_price[i]) == list:
        final_price[i] = month_3
        if type(final_price[i+1]) == list:
            final_price[i+1] = 0
            if type(final_price[i+2]) == list:
                final_price[i+2] = 0
                check(i+1, final_price)
                final_price[i+1] = [month_3]
                check(i+1, final_price)
                final_price[i+2] = [month_3]
                check(i+1, final_price)
            else:
                final_price[i + 2] = 0
                check(i+1, final_price)
                final_price[i+1] = [month_3]
                check(i+1, final_price)
        elif type(final_price[i+2]) == list:
            final_price[i+1] = 0
            final_price[i+2] = 0
            check(i+1, final_price)
            final_price[i+2] = [month_3]
            check(i+1, final_price)
        else:
            final_price[i+1] = 0
            final_price[i+2] = 0
            check(i+1, final_price)
        if final_price[i+1] == 0:
            final_price[i+1] = price[i+1]
        if final_price[i+2] == 0:
            final_price[i+2] = price[i+2]
        final_price[i] = price[i]
    check(i+1, final_price)



T = int(input())
for case in range(1, T+1):
    day, month, month_3, year = map(int, input().split())
    plan = list(map(int, input().split()))
    minv = year
    m = month//day+1
    price = [0]*12
    for i in range(12):
        if plan[i] >= m:
            if month >= month_3:
                price[i] = month_3
            else:
                price[i] = month
        else:
            if plan[i]*day >= month_3:
                price[i] = month_3
            else:
                price[i] = plan[i]*day
    final_price = [0]*12
    for i in range(10):
        sum3 = price[i] + price[i + 1] + price[i + 2]
        if sum3 >= month_3:
            final_price[i] = [month_3]
        else:
            final_price[i] = price[i]
    final_price[10] = price[10]
    final_price[11] = price[11]
    check(0, final_price)
    print('#{} {}'.format(case, minv))
```

### 4008. 숫자 만들기

```python
def ins(a,b,c,d,k):
    if k == (2*N-3):
        if 0 not in num_list:
            calc(num_list)
            return
    if a != 0:
        for i in range(1, 2 * N - 1, 2):
            if num_list[i] == 0:
                num_list[i] = '+'
                ins(a - 1, b, c, d, i)
                num_list[i] = 0
                break
    if b != 0:
        for i in range(1, 2 * N - 1, 2):
            if num_list[i] == 0:
                num_list[i] = '-'
                ins(a,b-1,c,d,i)
                num_list[i] = 0
                break
    if c != 0:
        for i in range(1, 2 * N - 1, 2):
            if num_list[i] == 0:
                num_list[i] = '*'
                ins(a,b,c-1,d,i)
                num_list[i] = 0
                break
    if d != 0:
        for i in range(1, 2 * N - 1, 2):
            if num_list[i] == 0:
                num_list[i] = '/'
                ins(a,b,c,d-1,i)
                num_list[i] = 0
                break

def calc(L):
    global minv
    global maxv
    result = num_list[0]
    for i in range(1, 2*N-1, 2):
        if L[i] == '+':
            result += num_list[i+1]
        elif L[i] == '-':
            result -= num_list[i+1]
        elif L[i] == '*':
            result *= num_list[i+1]
        elif L[i] == '/':
            result /= num_list[i+1]
            result = int(result)
    if maxv < result:
        maxv = result
    if minv > result:
        minv = result


T = int(input())
for case in range(1, T+1):
    N = int(input())
    a,b,c,d = map(int, input().split())
    maxv = -100000000
    minv = 100000000
    sign = []
    for i in range(a):
        sign.append('+')
    for i in range(b):
        sign.append('-')
    for i in range(c):
        sign.append('*')
    for i in range(d):
        sign.append('/')
    num = list(map(int, input().split()))
    num_list = []
    for i in range(N):
        num_list.append(num[i])
        num_list.append(0)
    num_list.pop()
    ins(a,b,c,d,0)
    print('#{} {}'.format(case, maxv-minv))

```

### 5658. 보물상자 비밀번호

```python
T = int(input())
for case in range(1, T+1):
    N, K = map(int, input().split())
    n = N // 4
    num = list(input())
    result = set()
    for k in range(n):
        for i in range(0, N, n):
            result.add(''.join(num[i:i+n]))
        num.insert(0, num.pop())
    result = list(result)
    for i in range(len(result)):
        result[i] = int(result[i], 16)
    result = sorted(result)
    print('#{} {}'.format(case, result[-K]))

```

### 1953. 탈주범 검거

```python
from pprint import pprint

def check(i, j, t, T):
    global N, M
    if t > T:
        return
    else:
        if type(root[i][j]) == list:
            root[i][j] = root[i][j][0]
        if root[i][j] == 1:
            order = [0, 1, 2, 3]
        elif root[i][j] == 2:
            order = [0, 1]
        elif root[i][j] == 3:
            order = [2, 3]
        elif root[i][j] == 4:
            order = [1, 2]
        elif root[i][j] == 5:
            order = [0, 2]
        elif root[i][j] == 6:
            order = [0, 3]
        elif root[i][j] == 7:
            order = [1, 3]
        root[i][j] = [root[i][j], t]
        p = 0
        for k in order:
            if i + di[k] >= 0 and i + di[k] < N and j + dj[k] >= 0 and j + dj[k] < M:
                if k == 0:
                    res = [1, 2, 4, 7]
                elif k == 1:
                    res = [1, 2, 5, 6]
                elif k == 2:
                    res = [1, 3, 6, 7]
                elif k == 3:
                    res = [1, 3, 4, 5]
                if type(root[i + di[k]][j + dj[k]]) == list:
                    if root[i + di[k]][j + dj[k]][1] > t and root[i + di[k]][j + dj[k]][0] in res:
                        p += 1
                        check(i + di[k], j + dj[k], t + 1, T)
                else:
                    if root[i + di[k]][j + dj[k]] in res:
                        p += 1
                        check(i + di[k], j + dj[k], t + 1, T)

        if p == 0:
            return


di = [1,-1,0,0]
dj = [0,0,1,-1]
T = int(input())
for case in range(1, T+1):
    N, M, i, j, L = map(int, input().split())
    root = []
    for _ in range(N):
        root.append(list(map(int, input().split())))
    check(i, j, 1, L)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if type(root[i][j]) == list:
                cnt += 1
    print('#{} {}'.format(case, cnt))
```

### 4012. 요리사

```python
from itertools import combinations

def combi():
    result = []
    for i in range(N//2):
        for c in combinations(range(i+1,N), N//2-1):
            temp = [i]
            for j in c:
                temp.append(j)
            result.append(temp)
    return result

def sum_f(L):
    result = 0
    for c in combinations(L, 2):
        result += S[c[0]][c[1]] + S[c[1]][c[0]]
    return result

T = int(input())
for case in range(1, T+1):
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(map(int, input().split())))
    num_list = combi()
    res = list(range(N))
    minv = 1000000
    for num in num_list:
        for n in num:
            res.remove(n)
        a = abs(sum_f(num) - sum_f(res))
        if minv > a:
            minv = a
        for n in num:
            res.append(n)

    print('#{} {}'.format(case, minv))

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





