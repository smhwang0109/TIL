def check():
    for i in range(V):
        for j in D[i]:
            for k in D[j]:
                if k != j and k != i:
                    for l in D[k]:
                        if l != j and l != i and l != k:
                            for m in D[l]:
                                if m != l and m != j and m != i and m != k:
                                    return 1
    return 0

V, E = map(int,input().split())
D = {}
for i in range(V):
    D[i] = []
for _ in range(E):
    f, t = map(int,input().split())
    # 1. 인접행렬
    # [[]]

    # 2. 인접 리스트
    # {f: t1, t2}
    D[f].append(t)
    D[t].append(f)

result = check()


print(result)