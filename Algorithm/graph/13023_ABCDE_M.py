import sys

V, Edge = map(int,input().split())
M = [[0]*V for _ in range(V)]
# G = {node: [] for node in range(V)}
G = [[] for _ in range(V)]
# {node : [e1, e2]}
F = []

for _ in range(Edge):
    f, t = map(int, input().split())
    # 1. 인접행렬
    # [[]]
    M[f][t] = M[t][f] = 1

    # 2. 인접 리스트
    # {f: [t1, t2]}
    G[f].append(t)
    G[t].append(f)

    # 3. edge 리스트
    F.append([f, t])
    F.append([t, f])

for i in range(len(F)):
    for j in range(len(F)):
        A, B = F[i]
        C, D = F[j]

        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not M[B][C]:
            continue
        for E in G[D]:
            if E == A or E == B or E == C or E == D:
                continue
            print(1)
            sys.exit(0)
else:
    print(0)

# print(M)
# print(G)
# print(F)