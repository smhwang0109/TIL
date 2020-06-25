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





