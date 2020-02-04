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
T = int(input())
for case in range(1,T+1):
    word = input()
    for idx in range(len(word)):
        if idx != len(word)-1:
            print('..#.',end = '')
        else:
            print('..#..')
    for idx in range(len(word)):
        if idx != len(word)-1:
            print('.#.#',end = '')
        else:
            print('.#.#.')
    for idx, w in enumerate(word):
        if idx != len(word) - 1:
            print('#.'+w+'.', end='')
        else:
            print('#.'+w+'.#')
    for idx in range(len(word)):
        if idx != len(word)-1:
            print('.#.#',end = '')
        else:
            print('.#.#.')
    for idx in range(len(word)):
        if idx != len(word)-1:
            print('..#.',end = '')
        else:
            print('..#..')

```

```python
# 참고. 제일짧은 코드 길이
for t in range(int(input())):
    a=input()
    b=len(a)-1
    c=[f"..#{'...#'*b}..",f".#{'.#.#'*b}.#.",f"#.{'.#.'.join(a)}.#"]
    for i in [0,1,2,1,0]:
        print(c[i])
```

### 1234. 비밀번호

```python
for case in range(1, 11):
    N, numbers = input().split()
    result = []
    for n in numbers:
        result.append(n)
    while True:
        count = 0
        for i in range(len(result)-1):
            if result[i] == result[i+1]:
                result.pop(i)
                result.pop(i)
                count += 1
                break
        if count == 0:
            break
    print('#{} {}'.format(case, ''.join(result)))

```

### 1213. String

```python
for case in range(1, 11):
    T = input()
    s = input()
    Str = input()
    count = 0
    for i in range(len(Str)-len(s)+1):
        if Str[i:].startswith(s):
            count += 1
    print('#{} {}'.format(case, count))
    
```

### 1240. 단순 2진 암호코드

```python
T = int(input())
for case in range(1, T + 1):

    v, h = map(int, input().split())
    d = {'0001101': 0,
         '0011001': 1,
         '0010011': 2,
         '0111101': 3,
         '0100011': 4,
         '0110001': 5,
         '0101111': 6,
         '0111011': 7,
         '0110111': 8,
         '0001011': 9,}
    for i in range(v):
        l = input()
        if '1' in l:
            L = l
    code = []
    for i in range(len(L)):
        for key in d.keys():
            if L[i:].startswith(key):
                if d[key] != 0 and d[key] != 9:
                    code = L[i:i+56]
                    break
                else:
                    for key2 in d.keys():
                        if L[i+49:].startswith(key2):
                            code = L[i:i+56]
                            break
        if code:
            break
    numbers = []
    for i in range(0,56,7):
        numbers.append(d[code[i:i+7]])
    sum1 = sum2 = 0
    for idx,n in enumerate(numbers):
        if idx%2:
            sum2 += n
        else:
            sum1 += n
    if (sum1*3+sum2)%10 == 0:
        result = sum1 + sum2
    else:
        result = 0

    print('#{} {}'.format(case, result))


```

### 3314. 보충학습과 평균

```python
T = int(input())
for case in range(1, T + 1):
    scores = list(map(int,input().split()))
    for idx in range(len(scores)):
        if scores[idx] < 40:
            scores[idx] = 40
    result = int(sum(scores) / 5)

    print('#{} {}'.format(case, result))


```

### 1228. 암호문1

```python
T = 10
for case in range(1, T + 1):
    N = int(input())
    original = list(map(int,input().split()))
    M = int(input())
    change = input().split()
    for idx, c in enumerate(change):
        if c == 'I':
            for i in range(int(change[idx+2])-1,-1,-1):
                original.insert(int(change[idx+1]), int(change[idx+3+i]))
    print('#{} {}'.format(case, ' '.join(map(str,original[0:10]))))

```

### 2805. 농작물 수확하기

```python
T = int(input())
for case in range(1, T + 1):
    N = int(input())
    sum0 = 0
    for i in range(N):
        values = []
        for n in input():
            values.append(int(n))
        if i <= N // 2:
            sum0 += sum(values[N // 2 - i : N // 2 + i + 1])
        else:
            sum0 += sum(values[N // 2 - (N-i-1): N // 2 + (N-i-1) + 1])

    print('#{} {}'.format(case, sum0))

```

### 3456. 직사각형 길이 찾기

```python
T = int(input())
for case in range(1, T + 1):
    numbers = list(map(int,input().split()))
    for n in numbers:
        if numbers.count(n) == 1 or numbers.count(n) == 3:
            result = n
    print('#{} {}'.format(case, result))

```

### 1209. Sum

```python
T = 10
for case in range(1, T + 1):
    test = input()
    numbers = []
    Sum_list = []
    for i in range(100):
        number = list(map(int,input().split()))
        Sum_list.append(sum(number))
        numbers.append(number)
    for i in range(100):
        sum0 = 0
        for j in range(100):
            sum0 += numbers[j][i]
        Sum_list.append(sum0)
    sum1 = 0
    for i in range(100):
        sum1 += numbers[i][i]
    Sum_list.append(sum1)

    print('#{} {}'.format(case, max(Sum_list)))

```

### 1229. 암호문2

```python
T = 10
for case in range(1, T + 1):
    N = int(input())
    original = list(map(int,input().split()))
    M = int(input())
    change = input().split()
    for idx, c in enumerate(change):
        if c == 'I':
            for i in range(int(change[idx+2])-1,-1,-1):
                original.insert(int(change[idx+1]), int(change[idx+3+i]))
        if c == 'D':
            for i in range(int(change[idx+2])):
                p = original.pop(int(change[idx+1]))


    print('#{} {}'.format(case, ' '.join(map(str,original[0:10]))))

```

### 5431. 민석이의 과제 체크하기

```python
T = int(input())
for case in range(1, T + 1):
    N, K = map(int,input().split())
    check = list(map(int, input().split()))
    b = []
    for n in range(1,N+1):
        if n not in check:
            b.append(n)

    print('#{} {}'.format(case, ' '.join(list(map(str,sorted(b))))))

```

### 4466. 최대 성적표 만들기

```python
T = int(input())
for case in range(1, T + 1):
    N, K = map(int,input().split())
    scores = list(map(int, input().split()))
    scores = list(reversed(sorted(scores)))
    S = []
    for k in range(K):
        S.append(scores[k])

    print('#{} {}'.format(case, sum(S)))

```

### 영준이의 신비한 뿔의 숲

```python
T = int(input())
for case in range(1, T + 1):
    N, M = map(int,input().split())
    for m in range(M+1):
        if N== m*2+(M-m):
            break

    print('#{} {} {}'.format(case, M-m, m))

```

```python
T = int(input())
for case in range(1, T + 1):
    N, M = map(int,input().split())
    m = N-M

    print('#{} {} {}'.format(case, M-m, m))

```

### 5162. 두가지 빵의 딜레마

```python
T = int(input())
for case in range(1, T + 1):
    A,B,C = map(int,input().split())
    print('#{} {}'.format(case, C//min(A,B)))
```

### 5515. 2016년 요일 맞추기

```python
T = int(input())
for case in range(1, T + 1):
    m,d = map(int,input().split())
    y = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    sum_d = 0
    if m == 1:
        result = ((d - 1) % 7 + 4) % 7
    else:
        for i in range(1,m):
            sum_d += y[i]
        sum_d += d
        result = ((sum_d - 1) % 7 + 4) % 7


    print('#{} {}'.format(case, result))
```

### 5549. 홀수일까 짝수일까

```python
T = int(input())
for case in range(1, T + 1):
    n = int(input())
    if n % 2:
        result = 'Odd'
    else:
        result = 'Even'
    print('#{} {}'.format(case, result))

```

### GNS

```python
d = {'ZRO':0,'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9,}
dd = {}
for key, value in d.items():
    dd[value] = key

T = int(input())
for case in range(1, T + 1):
    N = input()
    K = input().split()
    for i in range(len(K)):
        K[i] = d[K[i]]
    K = sorted(K)
    for i in range(len(K)):
        K[i] = dd[K[i]]

    print('#{} {}'.format(case, ' '.join(K)))

```

### 5789. 현주의 상자 바꾸기

```python
T = int(input())
for case in range(1,T+1):
    N, Q = list(map(int,input().split()))
    result = [0]*N
    for i in range(1,Q+1):
        L,R = list(map(int,input().split()))
        for j in range(L,R+1):
            result[j-1] = i
    
    print('#{} {}'.format(case,' '.join(list(map(str,result)))))
```

### 5356. 의석이의 세로로 말해요

```python
T = int(input())
for case in range(1,T+1):
    S_list = []
    L_list = []
    for i in range(5):
        S = list(input())
        S_list.append(S)
        L_list.append(len(S))

    for idx, l in enumerate(L_list):
        if l < max(L_list):
            for i in range(l, max(L_list)):
                S_list[idx].append(None)
    result = ''
    for i in range(max(L_list)):
        for j in range(5):
            if S_list[j][i] != None:
                result += S_list[j][i]

    print('#{} {}'.format(case,result))
```

### 5603. 건초더미

```python
T = int(input())
for case in range(1,T+1):
    N = int(input())

    S_list = []

    for i in range(N):
        S = int(input())
        S_list.append(S)
    r = sum(S_list) // N
    count = 0
    for n in S_list:
        if n > r:
            count += n-r

    print('#{} {}'.format(case,count))
```

### 4676. 늘어지는 소리 만들기

```python
T = int(input())
for case in range(1,T+1):
    S = list(input())
    N = int(input())
    H = list(map(int,input().split()))
    for i in H:
        if i != 0:
            S[i-1] += '-'
        else:
            S[0] = '-' + S[0]


    print('#{} {}'.format(case,''.join(S)))
```

### 4299. 태혁이의 사랑은 타이밍

```python
T = int(input())
for case in range(1, T+1):
    D, H, M = list(map(int,input().split()))
    if D - 11 < 0:
        result = -1
    elif D == 11 and H - 11 < 0:
        result = -1        
    elif D == 11 and H == 11 and M - 11 < 0:
        result = -1
    else:
        result = (D - 11) * 24 * 60 + (H - 11) * 60 + M - 11
    print('#{} {}'.format(case, result))
```

### 3499. 퍼펙트 셔플

```python
T = int(input())
for case in range(1, T+1):
    N = int(input())
    numbers = input().split()
    result = []
    if N % 2 == 0:
        first = numbers[0:N//2]
        second = numbers[N//2:]
        for i in range(N//2):
            result.append(first[i])
            result.append(second[i])
    else:
        first = numbers[0:N//2+1]
        second = numbers[N//2+1:]
        for i in range(N//2):
            result.append(first[i])
            result.append(second[i])
        result.append(first[-1])

    print('#{} {}'.format(case, ' '.join(result)))
```

### 1493. 수의 새로운 연산

```python
def ja(n):
    count = 1
    s1 = 1
    s2 = 1
    while True:
        if s1 <= n and s2 >= n:
            count -= 1
            break
        s1 += count
        count += 1
        s2 += count
    a = n - s1
    n = [1 + a, count + 1 - a]
    return n

T = int(input())
for case in range(1, T+1):
    p, q = map(int, input().split())
    p = ja(p)
    q = ja(q)

    r = []
    for i in range(2):
        r.append(p[i]+q[i])
    a = r[0] - 1
    r = [r[0]-a,r[1]+a]
    count = r[1]
    s1 = 1
    for i in range(1,count):
        s1 += i
    result = s1 + a

    print('#{} {}'.format(case, result))

```

### 5948. 새샘이의 7-3-5

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







