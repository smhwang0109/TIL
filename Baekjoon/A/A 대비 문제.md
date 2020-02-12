# BaekJoon IM

### 17144. 미세먼지 안녕!

```python
R, C, T = map(int,input().split())
room = []
room.append([-1]*(C+2))
for i in range(R):
    r = list(map(int, input().split()))
    room.append([-1]+r+[-1])
room.append([-1]*(C+2))
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for idx in range(1, R + 1):
    if room[idx][1] == -1:
        break


up_wind = []
for j in range(1, C + 1):
    up_wind.append([idx, j])
for i in range(1, idx):
    up_wind.append([idx - i, j])
for j in range(C - 1, 0, -1):
    up_wind.append([idx - i, j])
for i in range(2, idx + 1):
    up_wind.append([i, j])

idx += 1
down_wind = []
for j in range(1, C + 1):
    down_wind.append([idx, j])
for i in range(1, idx):
    down_wind.append([idx + i, j])
for j in range(C - 1, 0, -1):
    down_wind.append([idx + i, j])
for i in range(R-1, idx-1,-1):
    down_wind.append([i, j])


for s in range(T):
    # 확산
    temp_room = []
    for i in range(R+2):
        r = []
        for j in range(C+2):
            r.append(room[i][j])
        temp_room.append(r)
    for i in range(1,R+1):
        for j in range(1,C+1):
            if room[i][j] != 0 and room[i][j] != -1:
                p_count = 0
                for k in range(4):
                    if room[i+dx[k]][j+dy[k]] != -1:
                        temp_room[i + dx[k]][j + dy[k]] += int(room[i][j]/5)
                        p_count += 1
                temp_room[i][j] -= int(room[i][j]/5)*p_count
    room = []
    for i in range(R + 2):
        r = []
        for j in range(C + 2):
            r.append(temp_room[i][j])
        room.append(r)
    # 공기 청정기
    for i in range(1, len(up_wind)-1):
        if room[up_wind[i][0]][up_wind[i][1]] != 0:
            if i != len(up_wind)-2:
                temp_room[up_wind[i+1][0]][up_wind[i+1][1]] = room[up_wind[i][0]][up_wind[i][1]]
            if temp_room[up_wind[i][0]][up_wind[i][1]] != room[up_wind[i-1][0]][up_wind[i-1][1]]:
                    temp_room[up_wind[i][0]][up_wind[i][1]] = 0
    for i in range(1, len(down_wind)-1):
        if room[down_wind[i][0]][down_wind[i][1]] != 0:
            if i != len(down_wind) - 2:
                temp_room[down_wind[i + 1][0]][down_wind[i + 1][1]] = room[down_wind[i][0]][down_wind[i][1]]
            if temp_room[down_wind[i][0]][down_wind[i][1]] != room[down_wind[i-1][0]][down_wind[i-1][1]]:
                temp_room[down_wind[i][0]][down_wind[i][1]] = 0
    room = []
    for i in range(R + 2):
        r = []
        for j in range(C + 2):
            r.append(temp_room[i][j])
        room.append(r)


count = 0

for i in range(1,R+1):
    for j in range(1,C+1):
        if room[i][j] > 0:
            count += room[i][j]

print(count)
```

### 17135. 캐슬 디펜스

```python
from pprint import pprint
from copy import deepcopy

#공격
def attack(k, l):
    result = 0
    nearest = 1000000
    n_list = []
    for j in range(M):
        for i in range(N):
            if new_A[i][j] == 1:
                if abs(k-i) + abs(l-j) <= D and abs(k-i) + abs(l-j) < nearest:
                    nearest = abs(k-i) + abs(l-j)
                    n_list = []
                    n_list.append([i,j])
                elif abs(k-i) + abs(l-j) <= D and abs(k-i) + abs(l-j) < nearest:
                    n_list.append([i, j])
    min_j = 1000000
    for n in n_list:
        if n[1] < min_j:
            min_j = n[1]
            result = n
    if result:
        return  result

def down():
    for i in range(N-1,-1,-1):
        for j in range(M):
            if new_A[i][j] == 1:
                if i != N:
                    new_A[i+1][j] = new_A[i][j]
                new_A[i][j] = 0




N, M, D = map(int, input().split())

A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)
A.append([0]*M)
max_cnt = 0
# 궁수 [N,a], [N,b], [N,c]
for a in range(M-2):
    for b in range(a, M-1):
        for c in range(b, M):
            new_A = deepcopy(A)
            A_cnt = 0
            while True:
                att1 = attack(N, a)
                att2 = attack(N, b)
                att3 = attack(N, c)
                if att1:
                    new_A[att1[0]][att1[1]] = 0
                    A_cnt += 1
                if att2:
                    new_A[att2[0]][att2[1]] = 0
                    if att1 != att2:
                        A_cnt += 1
                if att3:
                    new_A[att3[0]][att3[1]] = 0
                    if att1 != att3 and att2 != att3:
                        A_cnt += 1
                down()
                cnt = 0
                for i in range(N):
                    if new_A[i].count(1):
                        cnt = 1
                        break
                if cnt == 0:
                    break
            if max_cnt < A_cnt:
                max_cnt = A_cnt
print(max_cnt)
```

### 15684. 사다리 조작

```python
def check(i,j):
    while i <= 2*H:
        if A[i][j+1] == 1:
            j += 2
            i += 1
        elif A[i][j-1] == 1:
            j -= 2
            i += 1
        else:
            i += 1


N, M, H = map(int, input().split())
A = []

for i in range(H*2+1):
    A.append([0] + [1, 0]*(N-1)+[1] + [0])
print(A)
for _ in range(M):
    a, b = map(int,input().split())
    A[a*2][b*2] = 1
print(A)
ab_list = []
for i in range(2,2*N+1,2):
    for j in range(2,2*H,2):
        if A[i][j] == 0 and A[i][j+2] == 0 and A[i][j-2] == 0:
            ab_list.append([a,b])


i = 1
for j in range(1,N*2,2):



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





