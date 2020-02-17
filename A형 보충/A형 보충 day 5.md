# A형 보충 day 5

작성자: 전은정 (2020.02.13)



## * BFS

```
# pseudo code

BFS(s)
	enQ(s)
	V[s] = 1
	while(is_not_emptyQ())
		n = deQ()
		visit(n)
		for i : 1 -> N
			// i 와 인접하면서 미방문한 노드에 관해
			if(A[n][i]==1 && V[i]==0)
				enQ(i)
				// 정점으로부터의 거리를 저장 // 거리가 필요하지 않은 경우엔 V[i] = 1 도 무방
				V[i] = V[n] + 1
```



## 1. 연구소 (14502번)

> [문제](https://www.acmicpc.net/problem/14502)
>
> [소스코드](https://github.com/pyjune/SSA3_2/tree/master/200213)

### 1) 바이러스를 어떻게 확산시킬 것인가?

- BFS를 통해 처음에 바이러스가 있던 칸의 인접한 칸으로 순서대로 확산

- 처음에 바이러스가 있는 칸이 여러 칸이라면?

  - BFS를 위한 queue에 바이러스가 있는 모든 칸을 모두 enqueue 하고 탐색하면 됨.

    - 바이러스가 있는 첫 번째 칸(A)을 방문하고 그 인접 칸들을 enqueue
    - 다음, 바이러스가 있는 두 번째 칸(B)을 방문하고 그 인접 칸들을 enqueue
    - 다음, queue에 있는 A의 인접 칸들을 차례로 방문하면서 그 인접 칸들을 enquequ
    - 다음, queue에 있는 B의 인접 칸들을 차례로 방문하면서 그 인접 칸들을 enqueue
    - 위의 과정을 반복

    

### 2) 확산이 마무리되는 시점을 어떻게 알 수 있을 것인가?

- 방문했던 칸이나 벽이 있는 칸은 enqueue 되지 않으므로 queue 에 남아있는 칸이 없으면 확산이 마무리 된 것임.

  

### 3) 안전 영역의 크기는 어떻게 구할 것인가?

- BFS 가 마무리 된 뒤, 벽이 아니면서 BFS 과정 중에 방문하지 않은 칸은 안전 영역임.



### * 소스코드

```python
from itertools import combinations

def BFS(s, lab, N, M):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    queue = []
    visited = [[0] * M for _ in range(N)]
    for ss in s:
        queue.append(ss)
        visited[ss[0]][ss[1]] = 1
    while queue:
        v = queue.pop(0)
        for i in range(4):
            nr = v[0] + dr[i]
            nc = v[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if lab[nr][nc] != 1 and visited[nr][nc] == 0:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
    return visited

def get_safe_area(lab, visited, N, M):
    safe_area = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0 and visited[i][j] == 0:
                safe_area += 1
    return safe_area

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

virus = []
empty_space = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append((i, j))
        if lab[i][j] == 0:
            empty_space.append((i, j))

candidates = combinations(empty_space, 3)

max_safe_area = 0
for candidate in candidates:
    for r, c in candidate:
        lab[r][c] = 1
    visited = BFS(virus, lab, N, M)
    safe_area = get_safe_area(lab, visited, N, M)
    if safe_area > max_safe_area:
        max_safe_area = safe_area
    for r, c in candidate:
        lab[r][c] = 0
    
print(max_safe_area)
```



## 2. 뱀 (3190번)

> [문제](https://www.acmicpc.net/problem/3190)
>
> [소스코드](https://github.com/pyjune/SSA3_2/tree/master/A보충)



# 끝.

# A형 보충수업 끝!





