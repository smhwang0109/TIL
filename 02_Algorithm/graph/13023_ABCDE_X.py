def check():
    for i in range(V):
        for j in X[i]:
            for k in X[j]:
                if k != j and k != i:
                    for l in X[k]:
                        if l != j and l != i and l != k:
                            for m in X[l]:
                                if m != l and m != j and m != i and m != k:
                                    return 1
    return 0

V, E = map(int,input().split())
X = []
for i in range(V):
    X.append([])
for _ in range(E):
    f, t = map(int,input().split())
    # 1. 인접행렬
    # [[]]
    X[f].append(t)
    X[t].append(f)

    # 2. 인접 리스트
    # # {f: t1, t2}

result = check()


print(result)