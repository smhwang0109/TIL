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





