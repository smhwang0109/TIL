def DFS(v):
    stack = []
    stack.append(v)
    visited[v] = 1
    print(v, end = "-")

    while stack:
        p = v
        for w in G[v]:
            if not visited[w]:
                stack.append(w)
                v = w
                visited[w] = 1
                print(v, end = "-")
                break
        else:
            if p == v:
                v = stack.pop()
# 재귀 방식
def DFS2(v):
    visited[v] = 1

    print(v, end=" ")

    for w in G[v]:
        if not visited[w]:
            DFS2(w)




import sys

sys.stdin = open('input2.txt')

V, E = map(int, input().split())

G = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

print(G)
DFS2(1)