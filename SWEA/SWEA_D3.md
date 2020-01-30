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
    test = []
    C_list = [0]*5001
    for i in range(N):
        start, end = list(map(int, input().split()))
        for l in range(start,end+1):
            C_list[l] += 1.

    P = int(input())
    print('#{}'.format(case),end='')
    for i in range(P):
        c = int(input())
        print(' {}'.format(int(C_list[c])),end='')
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

### 1206. View

```python
T = 10
for case in range(1,T+1):
    N = input()
    buildings = list(map(int,input().split()))
    count = 0
    #인덱싱을 해서 왼쪽 두개 오른쪽 두개에서 기준보다 낮은것 중 가장 큰 숫자 찾아서 차이를 count에 추가
    for idx, b in enumerate(buildings):
        if idx > 1 and idx < len(buildings)-2:
            b_l = [buildings[idx-2],buildings[idx-1],buildings[idx+1],buildings[idx+2]]
            if b > max(b_l):
                count += b - max(b_l)
    print('#{} {}'.format(case, count))

```

### 1208. Flatten

```python
T = 10
for case in range(1,T+1):
    N = int(input())
    N_list = list(map(int,input().split()))
    N_list = sorted(N_list)
    while N != 0:
        N_list[-1] -= 1
        N_list[0] += 1
        N -= 1
        N_list = sorted(N_list)
    result = N_list[-1] - N_list[0]
    print('#{} {}'.format(case,result))
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