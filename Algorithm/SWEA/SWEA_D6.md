# SW Expert Academy Algorithm D6

### 1267. 작업순서

```python
T = 10
for case in range(1,T+1):
    V, E = map(int,input().split())
    L = list(map(int,input().split()))
    original = {}
    rev = {}
    for i in range(1,V+1):
        original[i] = []
        rev[i] = []
    for i in range(0,len(L),2):
        original[L[i]].append(L[i+1])
        rev[L[i+1]].append(L[i])
    result = []
    inp = []
    for r in range(1,V+1):
        if rev[r] == []:
            result.append(r)
    for r in result:
        for ori_val in original[r]:
            p = 1
            for rev_val in rev[ori_val]:
                if rev_val not in result:
                    p = 0
                    break
            if p == 1:
                if ori_val not in result:
                    result.append(ori_val)
    print('#{} {}'.format(case, ' '.join(map(str, result))))

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





