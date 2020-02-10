# BaekJoon IM

### 2669. 직사각형 네개의 합집합의 면적 구하기

```python
M = []
for i in range(100):
    M.append([0]*100)

for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            M[i][j] = 1
count = 0
for i in range(100):
    for j in range(100):
        if M[i][j] == 1:
            count += 1

print(count)
```

### 2635. 수 이어가기

```python
N = int(input())
max0 = 0
for n in range(N, N//2 -1, -1):
    result = [N,n]
    cnt = 0
    S1 = N
    S2 = n
    while True:
        if S1-S2 >= 0:
            result.append(S1-S2)
            S1, S2 = S2, S1-S2
            cnt += 1
        else:
            break
    if max0 < cnt:
        max0 = cnt
        final = result

print(max0+2)
print(' '.join(map(str,final)))
```

### 1244. 스위치 켜고 끄기

```python
s_n = int(input())
switch = list(map(int,input().split()))
N = int(input())
for n in range(N):
    order, num = list(map(int,input().split()))
    if order == 1:
        for i in range(1,s_n//num+1):
            if switch[num*i-1] == 0:
                switch[num * i - 1] = 1
            else:
                switch[num * i - 1] = 0
    elif order == 2:
        for i in range(min(num - 1, s_n - num)+1):
            if switch[num-1+i] != switch[num-1-i]:
                i = i - 1
                break
        for j in range(num-1-i,num-1+i+1):
            if switch[j] == 0:
                switch[j] = 1
            else:
                switch[j] = 0


for i in range((len(switch)-1)//20+1):
    if i == (len(switch)-1)//20:
        print(' '.join(list(map(str,switch[20*i:]))))
    else:
        print(' '.join(list(map(str, switch[20*i:20*(i+1)]))))
```

### 2628. 종이자르기

```python
J, I = map(int,input().split())
N = int(input())
H = []
V = []
for n in range(N):
    order,num = map(int,input().split())
    if order == 0:
        H.append(num)
    else:
        V.append(num)
H = sorted(H)
V = sorted(V)
H.append(I)
V.append(J)
area = []
start_i = 0
for i in H:
    start_j = 0
    for j in V:
        area.append(abs((i - start_i) * (j - start_j)))
        start_j = j
    start_i = i
print(max(area))
```

### 2116. 주사위 쌓기

```python
N = int(input())
D = {}
dice_list = []
for n in range(N):
    D = {}
    a1, b1, c1, b2, c2, a2 = map(int,input().split())
    D[a1] = a2
    D[a2] = a1
    D[b1] = b2
    D[b2] = b1
    D[c1] = c2
    D[c2] = c1
    dice_list.append(D)
result = []
u_under = 0
real_under = 0
for num in range(1, 7):
    under = num
    cnt = 0
    for D in dice_list:
        if D[under] == 6:
            if under == 5:
                cnt += 2
            else:
                cnt += 1
        if under == 6:
            if D[under] == 5:
                cnt += 2
            else:
                cnt += 1
        under = D[under]
    result.append(cnt)
print(N*6-min(result))

```

### 2304. 창고 다각형

```python

N = int(input())
M = [0]*1001
max_H = 0
L_list = []
max_start_L = 0
max_end_L = 0
end_H = 0
for _ in range(N):
    L, H = map(int,input().split())
    L_list.append(L)
    if max_H < H:
        max_H = H
        max_start_L = L
    elif max_H == H:
        end_H = H
        max_end_L = L
    M[L] = H
if max_H != end_H:
    max_end_L = max_start_L
L_list = sorted(L_list)
height = 0
area = 0
curr_L = 0
for i in L_list[:L_list.index(max_start_L)+1]:
    if height < M[i]:
        area += height*(i-curr_L)
        height = M[i]
        curr_L = i

area += height*(max_end_L - max_start_L +1)

while height != 0:
    max_H = 0
    initial_L = max_end_L
    for i in L_list[L_list.index(max_end_L)+1:]:
        if max_H < M[i]:
            max_H = M[i]
            max_end_L = i
    width = max_end_L - initial_L
    height = max_H
    area += height*width
print(area)

```

```python

N = int(input())
M = [0]*1001
max_H = 0
L_list = []
max_start_L = 0
max_end_L = 0
end_H = 0
for _ in range(N):
    L, H = map(int,input().split())
    L_list.append(L)
    if max_H < H:
        max_H = H
        max_start_L = L
    elif max_H == H:
        end_H = H
        max_end_L = L
    M[L] = H
if max_H != end_H:
    max_end_L = max_start_L
end = max(L_list)
M = M[:end+1]
height = 0
area = 0
curr_L = 0
start_point = 0
for i in range(max_start_L+1):
    if M[i] > height:
        area += (i - start_point) * height
        start_point = i
        height = M[i]

area += height*(max_end_L - max_start_L +1)


start_point = len(M)-1
height = M[-1]
for j in range(len(M)-1,max_end_L-1,-1):
    if M[j] > height:
        area += (start_point-j) * height
        start_point = j
        height = M[j]


print(area)

```

### 2559. 수열

```python
N, K = map(int,input().split())
N_list = list(map(int, input().split()))
s = 0
for i in range(K):
    s += N_list[i]
S1 = [s]

for i in range(K,N):
    S1.append(S1[-1]+N_list[i]-N_list[i-K])
print(max(S1))
```

### 2578. 빙고

```python
board = []
check = []
for i in range(5):
    b = list(map(int, input().split()))
    board.append(b)
    check.append([0]*5)

tell = []
for i in range(5):
    tell += list(map(int, input().split()))
for t in range(len(tell)):
    bingo = 0
    for i in range(5):
        if tell[t] in board[i]:
            j = board[i].index(tell[t])
            break
    check[i][j] = 1
    l_u = 0
    r_u = 0
    for k in range(5):
        if check[k][k] == 1:
            l_u += 1
        if check[4-k][k] == 1:
            r_u += 1
        if sum(check[k]) == 5:
            bingo += 1
        down = 0
        for i in range(5):
            if check[i][k] == 1:
                down += 1
        if down == 5:
            bingo += 1
    if l_u == 5:
        bingo += 1
    if r_u == 5:
        bingo += 1

    if bingo >= 3:
        break


print(t+1)


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





