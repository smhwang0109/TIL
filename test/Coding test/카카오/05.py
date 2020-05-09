def solution(n, path, order):
    answer = True
    visited = [0] * n
    visited[0] = 1
    D = {}
    for i in range(n):
        D[i] = []
    for p in path:
        D[p[0]].append(p[1])
        D[p[1]].append(p[0])
    check = {}
    for o in order:
        check[o[1]] = o[0]
    L = []
    for d in D[0]:
        L.append(d)
    i = 0
    while L:
        if L[i] in check.keys():
            if not visited[check[L[i]]]:
                i += 1
                if i >= len(L):
                    answer = False
                    break
                continue
        visited[L[i]] = 1
        for d in D[L[i]]:
            if visited[d] == 0:
                L.append(d)
        L.pop(i)
        i = 0
    return answer

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))