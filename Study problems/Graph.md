# Graph

## SWEA study

### 1267. 작업순서

```python
T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # D는 1부터 시작
    D = [[] for _ in range(V+1)]
    L = list(map(int, input().split()))
    for i in range(0, len(L), 2):
        i = L[i]
```

