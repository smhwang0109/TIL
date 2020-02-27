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

```

### 4008. 숫자 만들기

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





