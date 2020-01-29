# SW Expert Academy Algorithm D3

### 7675. 통역사 성경이

```python

T = int(input())
for case in range(1,T+1):
    N = int(input())
    sentence = input()
    count = []
    sen = []
    s = ''
    for letter in sentence:
        s += letter
        if letter == '.' or letter == '?' or letter == '!':
            sen.append(s)
            s = ''
    for i in sen:
        sen_count = 0
        keyword = i.split()
        for k in keyword:
            if k.isalpha() and k[0].isupper() and k[1:].islower():
                sen_count += 1
            elif k[0:len(k)-1].isalpha() and k[0].isupper() and k[1:].islower() and (k[len(k)-1]== '.' or k[len(k)-1]== '!' or k[len(k)-1]== '?' ):
                sen_count += 1
            elif len(k)==1 and k.isalpha() and k.isupper():
                sen_count += 1
        count.append(sen_count)
    print('#{}'.format(case),end='')
    for j in range(N):
        print(' {}'.format(count[j]),end='')
    print()


```

### 6692. 다솔이의 월급 상자
```python

T = int(input())
for case in range(1,T+1):
    N = int(input())
    case_list = []
    for _ in range(N):
        test = list(map(float, input().split()))
        case_list.append(test[0] * test[1])
    s = sum(case_list)
    print('#{} {}'.format(case, s))


```

### 6485. 삼성시의 버스 노선

```python

T = int(input())
for case in range(1,T+1):
    N = int(input())
    C_list = []
    test_list = []
    test = []
    for i in range(N):
        test = list(map(int, input().split()))
        test_list.append(test)
    P = int(input())
    for _ in range(P):
        c = int(input())
        C_list.append(0)
    for k in test_list:
        for l in range(k[0]-1,k[1]):
            C_list[l] += 1
    print('#{}'.format(case),end='')
    for C in C_list:
        print(' {}'.format(C),end='')
    print()



```

### 6190. 정곤이의 단조 증가하는 수

```python

T = int(input())
for case in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))
    # result = [num1 * num2  for num1 in A for num2 in A  if num1 != num2 for i in range(len(str(num1 * num2))-1) if int(str(num1 * num2)[i])<= int(str(num1 * num2)[i+1])]
    for num1 in A:
        for num2 in A:
            if num1 != num2:
                s = str(num1 * num2)
                for i in range(len(s)-1):
                    if int(s[i]) <= int(s[i+1]):
                        result.append(num1 * num2)
    print('#{} {}'.format(case, max(result)))

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