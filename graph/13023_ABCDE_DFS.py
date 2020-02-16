def DFS(s, c):
    if c == 5:
        return 1
    visited[s] = 1
    for i in D[s]:
        if visited[i] == 0:
            if DFS(i, c+1) == 1:
                return 1
            else:
                visited[i] = 0
    return 0
    


V, E = map(int,input().split())
D = [[] for _ in range(V)]
for _ in range(E):
    u, v = map(int,input().split())
    D[u].append(v)
    D[v].append(u)
for i in range(V):
    visited = [0] * V
    if DFS(i, 1) == 1:
        print(1)
        break
else:
    print(0)