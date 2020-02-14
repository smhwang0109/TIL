import sys
from collections import deque

sys.stdin = open("input.txt")

N, E = map(int, input().split())
D = [[] for _ in range(N)]
for i in range(E):
    n1, n2 = map(int, input().split())
    D[n1-1].append(n2-1)
    D[n2-1].append(n1-1)

visited = [0]*N
stack = deque()
i = 0
visited[i] = 1
stack.append(i)
result = [1]
while True:
    for n in D[i]:
        if visited[n] == 0:
            visited[n] = 1
            i = n
            stack.append(i)
            result.append(i+1)
            break
    else:
        stack.pop()
        if stack:
            i = stack[-1]
    if not stack:
        break
print(result)
