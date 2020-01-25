# SW Expert Academy Algorithm D1

### 1938
``` python
nums = input().split()

num_list = list(map(int,nums))

a = num_list[0]
b = num_list[1]

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
```

### 1933
``` python
N = int(input())

for num in range(1,N+1):
    if N == num:
        print(num)
    elif N % num == 0:
        print(num, end = ' ')
```

### 1936
``` python
A_B = input().split()
A = A_B[0]
B = A_B[1]

if A == '1':
    if B == '2':
        print('B')
    else:
        print('A')
elif A == '2':
    if B == '3':
        print('B')
    else:
        print('A')
else:
    if B == '1':
        print('B')
    else:
        print('A')
```

### 2019
``` python
num = int(input())

for i in range(num+1):
    if i == num:
        print(2**i)
    else:
        print(2**i, end=' ')
```

### 1545
``` python
num = int(input())

for i in range(num,-1,-1):
    if i == 0:
        print(i)
    else:
        print(i, end=' ')
```