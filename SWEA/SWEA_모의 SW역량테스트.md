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





