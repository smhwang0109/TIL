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

### 1215. 회문1

```python
for case in range(1,11):
    N = int(input())
    All = []
    count = 0
    for i in range(8):
        s = input()
        # 1. 이중 for 문
        # 2. 구문 다 합친 후
        All.append(s)
    for i in range(8):
        for j in range(8-N+1):
            k = All[i][j:j+N]
            if k == ''.join(list(reversed(k))):
                count += 1
            l = []
            for g in range(N):
                l.append(All[j+g][i])
            if l == list(reversed(l)):
                count += 1
    print('#{} {}'.format(case,count))

```

### 1230. 암호문3

```python
T = 10
for case in range(1,T+1):
    N = int(input())
    original = list(map(int,input().split()))
    C = int(input())
    change = input().split()
    for idx, ch in enumerate(change):
        if ch == 'I':
            for n in range(int(change[idx+2])):
                original.insert(int(change[idx+1])+n, int(change[idx+3+n]))
        if ch == 'D':
            for n in range(int(change[idx+2])):
                original.remove(original[int(change[idx+1])])
        if ch == 'A':
            for n in range(int(change[idx+1])):
                original.append(int(change[idx+2+n]))
    print('#{}'.format(case),end='')
    for i in range(10):
        print(' {}'.format(original[i]),end='')
    print()


```

### 3431. 준환이의 운동관리

```python
T = int(input())
for case in range(1,T+1):
    L, U, X = list(map(int,input().split()))
    if X < L:
        result = L-X
    elif X > U:
        result = -1
    else:
        result = 0
    print('#{} {}'.format(case, result))

```

### 1217. 거듭 제곱

```python
def my_pow(M, new = 1):
    new *= N
    if M == 1:
        return new
    return my_pow(M-1, new)

T = 10
for case in range(1,T+1):
    test = input()
    N, M = list(map(int,input().split()))
    new = 1
    print('#{} {}'.format(case,my_pow(M)))

```

### 1220. Magnetic

```python
def X_90(L):
    t = []
    for i in range(100):
        k = []
        t.append(k)
        for j in range(100):
            k.append(0)
    for i in range(100):
        for j in range(100):
            t[i][99-j] = L[j][i]
    return t

T = 10
for case in range(1,T+1):
    N = input()
    table = []
    for _ in range(100):
        table.append(list(map(int,input().split())))
    table = X_90(table)
    for i in range(100):
        for j in range(100):
            if table[i][j] == 2:
                table[i][:j] = [0]*j
                break
        for k in range(100):
            if table[i][99-k] == 1:
                table[i][99-k+1:] = [0]*k
                break
    search = [0, 1]
    count = 0
    for i in range(100):
        for j in range(100):
            if table[i][j] not in search:
                search[1] = table[i][j]
                if table[i][j] == 1:
                    count+=1
    print('#{} {}'.format(case,count))    
```

### 1289. 원재의 메모리 복구하기

```python
T = int(input())
for case in range(1,T+1):
    N = input()
    search = '0'
    count = 0
    for n in N:
        if n != search:
            search = n
            count += 1


    print('#{} {}'.format(case,count))

```

### 4406. 모음이 보이지 않는 사람

```python
T = int(input())
for case in range(1,T+1):
    word = input()
    s = ''
    for w in word:
        if w not in 'aeiou':
            s += w
    print('#{} {}'.format(case,s))
```

### 1225. 암호생성기

```python
T = 10
for case in range(1,T+1):
    test = input()
    num = list(map(int, input().split()))
    while True:
        for count in range(1,6):
            if num[0] - count > 0:
                num.append(num.pop(0)-count)
            else:
                n = num.pop(0)
                num.append(0)
                break
        if num[7] == 0:
            break
    result = list(map(str,num))

    print('#{} {}'.format(case,' '.join(result)))
```

### 1216. 회문2

```python
def X_90(L):
    t = []
    for i in range(100):
        k = []
        t.append(k)
        for j in range(100):
            k.append(0)
    for i in range(100):
        for j in range(100):
            t[i][99-j] = L[j][i]
    return t

T = 10
for case in range(1,T+1):
    test = input()
    num_list = []
    for i in range(100):
        num = input()
        num_list.append(num)
    result = 0
    # 가로 검사
    for i in range(100):
        for j in range(100):
            for k in range(100-j-1):
                a = num_list[i][j:100-k]
                if result < len(a):
                    if a == ''.join(list(reversed(a))):
                        result = len(a)
                        break
    num_list = X_90(num_list)

    #세로 검사
    for i in range(100):
        for j in range(100):
            for k in range(100-j-1):
                a = num_list[i][j:100-k]
                if result < len(a):
                    if a == list(reversed(a)):
                        result = len(a)
                        break


    print('#{} {}'.format(case,result))

```

### 5601. 쥬스 나누기

```python
T = int(input())
for case in range(1,T+1):
    people = input()
    result = ['1/'+people]*int(people)
    print('#{} {}'.format(case,' '.join(result)))

```

### 4751. 다솔이의 다이아몬드 장식

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