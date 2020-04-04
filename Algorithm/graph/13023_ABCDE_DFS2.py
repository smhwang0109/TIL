def DFS(s):
    stack = []
    visited[s] = 1
    stack.append(s)
    cnt = 1
    while True:
        for i in D[s]:
            if visited[i] == 0:
                visited[i] = 1
                stack.append(i)
                s = i
                break
        else:
            stack.pop()
            if stack:
                s = stack[-1]
            else:
                break
    


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