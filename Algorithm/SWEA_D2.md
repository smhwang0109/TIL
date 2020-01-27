# SW Expert Academy Algorithm D2

### 1976. 시각 덧셈
``` python
T = int(input())

for case in range(1,T+1):
    N = input().split()
    N_list = list(map(int,N))
    C = N_list[0]+N_list[2]
    M = N_list[1]+N_list[3]
    if C < 13:
        if M < 60:
            print('#{} {} {}'.format(case, C, M))
        else:
            print('#{} {} {}'.format(case, C+1, M-60))
    else:
        if M < 60:
            print('#{} {} {}'.format(case, C-12, M))
        else:
            print('#{} {} {}'.format(case, C-11, M-60))

```

### 1974. 스도쿠 검증
``` python
def horizontal():
    for i in range(9):
        for num in range(1, 10):
            if num not in N_list_all[i]:
                return 0
    return 1

def vertical():
    for i in range(9):
        s_list = []
        for j in range(9):
            s_list.append(N_list_all[j][i])
        for num in range(1, 10):
            if num not in s_list:
                return 0
    return 1

def square():
    for i in range(3):
        for j in range(3):
            X_list = []
            for k in range(3):
                for l in range(3):
                    X_list.append(N_list_all[3*i+k][3*j+l])
            for num in range(1,10):
                if num not in X_list:
                    return 0
    return 1


T = int(input())

for case in range(1,T+1):
    result = 1
    N_list_all = []
    for k in range(9):
        N = input().split()
        N_list = list(map(int,N))
        N_list_all.append(N_list)
    result = horizontal()
    if result == 0:
        print('#{} {}'.format(case, result))
    else:
        result = vertical()
        if result == 0:
            print('#{} {}'.format(case, result))
        else:
            result = square()
            if result == 0:
                print('#{} {}'.format(case, result))
            else:
                print('#{} {}'.format(case, result))

```






### 1970. 쉬운 거스름돈
``` python
T = int(input())

M_case = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for case in range(1,T+1):
    print('#{}'.format(case))
    M = int(input())
    for i in M_case:
        count = M//i
        if i == 10:
            print(count)
        else:
            print(count,end = ' ')
        M -= i*count
```

### 1859. 백만 장자 프로젝트
``` python
T = int(input())

for case in range(1,T+1):
    count = 0
    N = int(input())
    price = input().split()
    price_list = list(map(int, price))
    for p in range(N):
        re_list = price_list[p:]
        if price_list[p] < max(re_list):
            count += (max(re_list) - price_list[p])
    print('#{} {}'.format(case, count))
```

### 1926. 간단한 369게임
``` python
T = input()
l = len(T)
num = int(T)

for n in range(1,num+1):
    count = 0
    m = n
    if m < 10:
        if m % 3 == 0:
            count += 1
    elif m < 100:
        for i in range(1,-1,-1):
            a = m // 10**i
            if a % 3 == 0 and m != 0:
                count += 1
            m -= a * 10**i
    elif m < 1000:
        for i in range(2,-1,-1):
            a = m // 10**i
            if a % 3 == 0 and m != 0:
                count += 1
            m -= a * 10**i
    if count != 0:
        if n == num:
            print('-'*count)
        else:
            print('-'*count, end = ' ')
    else:
        if n == num:
            print(n)
        else:
            print(n, end = ' ')

```

### 2007. 패턴 마디의 길이
``` python
T = int(input())

for case in range(1, T+1):
    S = input()
    for idx in range(len(S)):
        if S[:idx+1] == S[idx+1:2*(idx+1)]:
            print('#{} {}'.format(case,idx+1))
            break
```

### 2005. 파스칼의 삼각형
``` python
T = int(input())

for case in range(1, T+1):
    print('#{}'.format(case))
    num = int(input())
    l = [1]
    for i in range(1, num+1):
        if i == 1:
            print(l[0])
        else:
            m = l
            l = []
            for k in range(1, i+1):
                if k == 1:
                    print(1, end = ' ')
                    l.append(1)
                elif k == i:
                    print(1)
                    l.append(1)
                else:
                    print(m[k-2]+m[k-1], end = ' ')
                    l.append(m[k-2]+m[k-1])

```

### 2001. 파리 퇴치
``` python

T = int(input())

for case in range(1, T+1):
    N_M = list(map(int,input().split()))
    N_list = []
    for n in range(N_M[0]):
        N = list(map(int,input().split()))
        N_list.append(N)
    final_sum = 0
    for i in range(N_M[0]-N_M[1]+1):
        for j in range(N_M[0]-N_M[1]+1):
            sum0 = 0
            for k in range(N_M[1]):
                for l in range(N_M[1]):
                    sum0 += N_list[i+k][j+l]
            if final_sum < sum0:
                final_sum = sum0
    print('#{} {}'.format(case, final_sum))

```

### 1989. 초심자의 회문 검사
``` python

T = int(input())

for case in range(1, T+1):
    word = input()
    l = len(word)
    p = 1
    for r in range(l-1,-1,-1):
        r_letter = word[r]
        if r_letter != word[l-1-r]:
            p = 0
    if p == 0:
        print('#{} 0'.format(case))
    else:
        print('#{} 1'.format(case))


```

### 1986. 지그재그 숫자
``` python

T = int(input())

for case in range(1, T+1):
    num = int(input())
    sum_a = 0
    for odd in range(1, num+1, 2):
        sum_a += odd
    for even in range(2, num+1, 2):
        sum_a -= even
    print('#{} {}'.format(case, sum_a))



```

### 1984. 중간 평균값 구하기
``` python

T = int(input())

for case in range(1, T+1):
    num = list(map(int,input().split()))
    Max = max(num)
    Min = min(num)
    Sum = sum(num) - (Max + Min)
    print('#{} {}'.format(case, round(Sum/8)))

```

### 1983. 조교의 성적 메기기
``` python

T = int(input())
grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for case in range(1, T+1):
    num = list(map(int,input().split()))
    Sum = []
    for students in range(num[0]):
        student = list(map(int,input().split()))
        Sum.append(0.35*student[0] + 0.45*student[1] + 0.2*student[2])

    key_student = Sum[num[1]-1]
    m = num[0]/10
    final = sorted(Sum)
    g = (num[0] - (final.index(key_student)+1))
    grade = grade_list[int(g // m)]


    print('#{} {}'.format(case, grade))


```

### 1979. 어디에 단어가 들어갈 수 있을까
``` python

T = int(input())
for case in range(1, T+1):
    num = list(map(int,input().split()))
    puzzle_list = []
    for i in range(num[0]):
        puzzle = input()
        puzzle_list.append(puzzle)

    if '1 '*num[1]+'0' in 

```

### 1966. 숫자를 정렬하자
``` python

T = int(input())
for case in range(1, T+1):
    test_case = int(input())
    num = sorted(list(map(int,input().split())))
    print('#{}'.format(case), end=' ')
    for i in range(test_case):
        if i == test_case-1:
            print(num[i])
        else:
            print(num[i], end = ' ')

```

### 1961. 숫자 배열 회전
``` python

T = int(input())
for case in range(1, T+1):
    test = int(input())
    X = []
    X_90 = []
    X_180 = []
    X_270 = []
    print('#{}'.format(case))

    for _ in range(test):
        num = list(map(int,input().split()))
        X_a = []
        for __ in range(test):
            X_a.append(0)
        X.append(num)
        X_90.append(X_a)
    for _ in range(test):
        X_a = []
        for __ in range(test):
            X_a.append(0)
        X.append(num)
        X_180.append(X_a)
    for _ in range(test):
        X_a = []
        for __ in range(test):
            X_a.append(0)
        X.append(num)
        X_270.append(X_a)


    for i in range(test):
        for j in range(test):
            X_90[j][test-1-i] = X[i][j]
    for i in range(test):
        for j in range(test):
            X_180[j][test-1-i] = X_90[i][j]
    for i in range(test):
        for j in range(test):
            X_270[j][test-1-i] = X_180[i][j]

    for i in range(test):
        for j in range(test):
            print(X_90[i][j],end='')
        print('',end=' ')
        for k in range(test):
            print(X_180[i][k],end='')
        print('',end=' ')
        for l in range(test):
            print(X_270[i][l],end='')
        print()


```

### 1959. 두 개의 숫자열
``` python

T = int(input())
for case in range(1, T+1):
    num = list(map(int,input().split()))
    num_A = list(map(int,input().split()))
    num_B = list(map(int, input().split()))

    sum1 = []

    if num[0] < num[1]:
        c = num[1] - num[0]
        for i in range(c+1):
            sum0 = []
            for k in range(len(num_A)):
                sum0.append(num_B[i+k]*num_A[k])
            if sum(sum0) > sum(sum1):
                sum1 = sum0
    else:
        c = num[0] - num[1]
        for i in range(c+1):
            sum0 = []
            for k in range(len(num_B)):
                sum0.append(num_B[k]*num_A[i+k])
            if sum(sum0)>sum(sum1):
                sum1 = sum0

    print('#{} {}'.format(case, sum(sum1)))

```

### 1954. 달팽이 숫자
``` python
T = int(input())
for case in range(1, T+1):
    num = int(input())
    X = []
    for i in range(num):
        X_a = []
        for k in range(num):
            X_a.append(0)
        X.append(X_a)

    a = 1
    for i in range(int(num/2)):
        for c in range(4):
            for j in range(num - a):
                if c == 0:
                    X[i][j+i] = 4*i*(num-a+2) + c*(num - a) + j + 1
                elif c == 1:
                    X[j+i][num - 1 - i] = 4*i*(num-a+2) + c*(num - a) + j + 1
                elif c == 2:
                    X[num - 1 - i][num - 1 - j - i] = 4*i*(num-a+2) + c*(num - a) + j + 1
                else:
                    X[num - 1 - j - i][i] = 4*i*(num-a+2) + c*(num - a) + j + 1
        a += 2
    if num % 2:
        X[int(num/2)][int(num/2)] = num**2
    print('#{}'.format(case))
    for i in range(num):
        for j in range(num):
            if j == num-1:
                print(X[i][j])
            else:
                print(X[i][j], end = ' ')

```

### 1948. 날짜 계산기
``` python

T = int(input())
for case in range(1, T+1):
    date = list(map(int,input().split()))
    month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    days = 0

    if date[0] == date[2]:
        days = date[3]-date[1]+1
    else:
        for month in range(date[0]+1,date[2]):
            days += month_dict[month]
        days += month_dict[date[0]]- date[1] + date[3] + 1

    print('#{} {}'.format(case, days))

```

### 1946. 간단한 압축 풀기
``` python

T = int(input())
for case in range(1, T+1):
    test = int(input())
    count = 0
    print('#{}'.format(case))
    for _ in range(test):
        al_num = input().split()
        for i in range(int(al_num[1])):
            if count == 9:
                print(al_num[0])
                count = 0
            else:
                print(al_num[0], end='')
                count += 1
    print()

```

### 1945. 간단한 소인수분해
``` python
T = int(input())
for case in range(1, T+1):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while N != 1:
        if N % 2 == 0 :
            N = N//2
            a += 1
        elif N % 3 == 0:
            N = N//3
            b += 1
        elif N % 5 == 0:
            N = N//5
            c += 1
        elif N % 7 == 0:
            N = N//7
            d += 1
        else:
            N = N//11
            e += 1
    print('#'+ str(case),a,b,c,d,e)
```

### 1940. 가랏! RC카!
``` python

T = int(input())
for case in range(1, T+1):
    test = int(input())
    distance = 0
    speed = 0
    for i in range(test):
        inp = list(map(int, input().split()))
        if inp[0] == 1:
            speed += inp[1]
        elif inp[0] == 2:
            speed -= inp[1]
            if speed < 0:
                speed = 0
        distance += speed
    print('#{} {}'.format(case, distance))

```

### 1928. Base64 Decoder
``` python



```

### 1288. 새로운 불면증 치료법
``` python
T = int(input())
for case in range(1, T+1):
    N = int(input())
    count = 0
    s = set()
    while len(s) < 10:
        count += 1
        c = count * N
        for i in range(6,-1,-1):
            m = c//10**i
            if m != 0:
                l = i
                break
        for k in range(l,-1,-1):
            m = c // 10 ** k
            s.add(m)
            c -= m*10**k
    print('#{} {}'.format(case, count*N))
```

### 1285. 아름이의 돌 던지기
``` python

```

### 
``` python

```

### 
``` python

```
