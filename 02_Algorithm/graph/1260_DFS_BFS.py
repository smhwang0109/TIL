N, M, V = map(int, input().split())

D = {}
for n in range(1, N+1):
    D[n] = []

for _ in range(M):
    n1, n2 = map(int, input().split())
    D[n1].append(n2)
    D[n2].append(n1)
print(D)
result = []
inp = []

