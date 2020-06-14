def DFS(s):
    p = 1
    for i in rev[s]:
        if visited[i] == 0:
            p = 0
    if p == 1:
        if visited[s] == 0:
            visited[s] = 1
            print('',s, end= '')
        for i in D[s]:
            DFS(i)



T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # D는 1부터 시작
    D = [[] for _ in range(V+1)]
    rev = [[] for _ in range(V+1)]
    L = list(map(int, input().split()))
    visited = [0]*(V+1)
    for i in range(0, len(L), 2):
        D[L[i]].append(L[i+1])
        rev[L[i+1]].append(L[i])
    start = []
    for i in range(1, V+1):
        if not rev[i]:
            start.append(i)
    print('#{}'.format(tc),end='')
    for a in start:
        DFS(a)
    print()