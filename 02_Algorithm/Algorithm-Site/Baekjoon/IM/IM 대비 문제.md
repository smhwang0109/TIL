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
        max_end_L = L
    elif max_H == H:
        if max_start_L > L:
            max_start_L = L
        if max_end_L < L:
            max_end_L = L
    M[L] = H
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

### 2477. 참외밭

```python
N = int(input())
D = {1:[],2:[],3:[],4:[]}
for i in range(6):
    n, l = map(int, input().split())
    if i == 0:
        first = n
    if i == 1:
        second = n
    if i == 4 and first == n:
        D[n].insert(0,l)
    elif i == 5 and second == n:
        D[n].insert(0,l)
    else:
        D[n].append(l)
if len(D[1]) == 1:
    for i in range(3,5):
        if len(D[i]) == 2:
            if i == 3:
                area = D[1][0]*D[i][1] + D[2][0]*D[i][0]
            else:
                area = D[1][0]*D[i][0] + D[2][1]*D[i][1]
else:
    for i in range(3, 5):
        if len(D[i]) == 2:
            if i == 3:
                area = D[2][0] * D[i][0] + D[1][1] * D[i][1]
            else:
                area = D[2][0] * D[i][1] + D[1][0] * D[i][0]
print(N*area)
```

### 2527. 직사각형

```python
for case in range(4):
    x1, y1, x2, y2, p1, q1, p2, q2 = map(int,input().split())
    if x1 > p2 or y2 < q1 or x2 < p1 or y1 > q2:
        result = 'd'
    elif x1 == p2 and y1 == q2 or x2 == p1 and y2 == q1 or x1 == p2 and y2 == q1 or x2 == p1 and y1 == q2:
        result = 'c'
    elif x2 == p1 or x1 == p2 or y2 == q1 or y1 == q2:
        result = 'b'
    else:
        result = 'a'
    print(result)
```

### 10157. 자리배정

```python
C, R = map(int, input().split())
K = int(input())
S = [[-1]*(C+2)]
for r in range(R):
    S.append([-1]+[0]*C+[-1])
S.append([-1]*(C+2))
result = [0]
if K > C*R:
    result = [0]
else:
    i = 1
    j = 1
    k = 1
    while k <= K:
        #위
        while True:
            if S[i][j] == 0:
                S[i][j] = k
                if k == K:
                    result = [j, i]
                    break
                k += 1
                i += 1
            else:
                j += 1
                i -= 1
                break
        if result != [0]:
            break
        #오른쪽
        while True:
            if S[i][j] == 0:
                S[i][j] = k
                if k == K:
                    result = [j, i]
                    break
                k += 1
                j += 1
            else:
                i -= 1
                j -= 1
                break
        if result != [0]:
            break
        #아래
        while True:
            if S[i][j] == 0:
                S[i][j] = k
                if k == K:
                    result = [j, i]
                    break
                k += 1
                i -= 1
            else:
                j -= 1
                i += 1
                break
        if result != [0]:
            break
        #왼쪽
        while True:
            if S[i][j] == 0:
                S[i][j] = k
                if k == K:
                    result = [j,i]
                    break
                k += 1
                j -= 1
            else:
                i += 1
                j += 1
                break
        if result != [0]:
            break
print(' '.join(map(str, result)))
```

### 10158. 개미

```python
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

i = 1
j = 1
for _ in range(t):
    if q+i < 0 or q+i > h:
        i = -i
    elif p+j < 0 or p+j > w:
        j = -j
    q += i
    p += j
print(p,q)

```

```python
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

if ((p+t)//w)%2 == 0:
    f_p = (p+t) % w
else:
    f_p = w - (p + t) % w

if ((q+t)//h)%2 == 0:
    f_q = (q+t) % h
else:
    f_q = h - (q + t) % h

print(f_p,f_q)
```

### 10163. 색종이

```python
N = int(input())

M = []
for _ in range(101):
    M.append([0]*101)

for n in range(1, N+1):
    j, i, W, H = map(int, input().split())
    for h in range(H):
        for w in range(W):
            M[i+h][j+w] = n
for n in range(1, N+1):
    cnt = 0
    for i in range(101):
        cnt += M[i].count(n)
    print(cnt)
```

### 13300. 방 배정

```python

N, K = map(int, input().split())

D = {}

for g in range(1,7):
    D[g] = {0:0, 1:0}

for _ in range(N):
    s, g = map(int, input().split())
    D[g][s] += 1

room_cnt = 0
for g in range(1,7):
    for i in range(2):
        if D[g][i] != 0:
            room_cnt += (D[g][i]-1)//K +1

print(room_cnt)
```

### 14696. 딱지놀이

```python
N = int(input())
A = []
B = []

for _ in range(N):
    n, *A = list(map(int, input().split()))
    n, *B = list(map(int, input().split()))
    for j in range(4,0,-1):
        if A.count(j) > B.count(j):
            print('A')
            break
        elif A.count(j) < B.count(j):
            print('B')
            break
        else:
            if j == 1:
                print('D')
```

### 2309. 일곱 난쟁이

```python
import itertools

H = []

for _ in range(9):
    h = int(input())
    H.append(h)

for h in itertools.combinations(H,7):
    if sum(h) == 100:
        break
for i in sorted(h):
    print(i)
```

### 2605. 줄 세우기

```python
N = int(input())
arr = []
numbers = list(map(int, input().split()))

for n in range(1, N+1):
    arr.insert(n-1 - numbers[n-1],n)

print(' '.join(map(str, arr)))
```

### 2563. 색종이

```python
M = []
for _ in range(101):
    M.append([0]*101)

N = int(input())
arr = []
for n in range(N):
    J, I = map(int, input().split())
    for i in range(I, I+10):
        for j in range(J, J+10):
            M[i][j] = 1
area = 0
for i in range(101):
    area += M[i].count(1)

print(area)
```

### 2564. 경비원

```python
h, v = map(int,input().split())

N = int(input())
store = []
for n in range(N):
    s = list(map(int, input().split()))
    store.append(s)

d_p, dis = map(int, input().split())

sum0 = 0

for n in range(N):
    if d_p == 1:
        if store[n][0] == 3:
            short = store[n][1]+dis
        elif store[n][0] == 4:
            short = store[n][1]+(h-dis)
        elif store[n][0] == 2:
            short = min(store[n][1] + dis + v, 2*h - store[n][1] - dis + v)
        else:
            short = abs(store[n][1]-dis)
    elif d_p == 2:
        if store[n][0] == 3:
            short = v-store[n][1]+dis
        elif store[n][0] == 4:
            short = v-store[n][1]+(h-dis)
        elif store[n][0] == 1:
            short = min(store[n][1] + dis + v, 2*h - store[n][1] - dis + v)
        else:
            short = abs(store[n][1]-dis)
    elif d_p == 3:
        if store[n][0] == 1:
            short = store[n][1]+dis
        elif store[n][0] == 2:
            short = store[n][1]+(v-dis)
        elif store[n][0] == 4:
            short = min(store[n][1] + dis + h, 2*v - store[n][1] - dis + h)
        else:
            short = abs(store[n][1]-dis)
    elif d_p == 4:
        if store[n][0] == 1:
            short = h-store[n][1] + dis
        elif store[n][0] == 2:
            short = h-store[n][1] + (v - dis)
        elif store[n][0] == 3:
            short = min(store[n][1] + dis + h, 2 * v - store[n][1] - dis + h)
        else:
            short = abs(store[n][1] - dis)
    sum0 += short

print(sum0)
```

### 2491. 수열

```python
N = int(input())

n = list(map(int, input().split()))
cnt = 1
l = 1
for i in range(1, N):
    if n[i-1] <= n[i]:
        cnt += 1
        if l < cnt:
            l = cnt
    else:
        cnt = 1
cnt = 1
for i in range(1, N):
    if n[i-1] >= n[i]:
        cnt += 1
        if l < cnt:
            l = cnt
    else:
        cnt = 1
print(l)
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





