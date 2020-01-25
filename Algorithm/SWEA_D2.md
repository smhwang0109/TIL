# SW Expert Academy Algorithm D2

### 1976.
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

### 1974.
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






### 1970.
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

### 1859.
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

### 1926.
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

### 2007.
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



```

### 
``` python

```

### 
``` python

```

### 
``` python

```

### 
``` python

```