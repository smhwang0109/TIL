# SW Expert Academy Algorithm D2

### 1976
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

### 1974
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






### 1970
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

### 1859
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

### 1926
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

### 
``` python

```

### 
``` python

```

### 
``` python

```