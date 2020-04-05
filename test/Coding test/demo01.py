def check(v, i, n, L):
    if v[i][n] not in L.keys():
        L[v[i][n]] = 1
    else:
        L[v[i][n]] = 2
    return L

def plus(L, answer):
    for key in L.keys():
        if L[key] == 1:
            answer.append(key)
    return answer

def solution(v):
    X = {}
    Y = {}
    answer = []
    for i in range(3):
        X = check(v, i, 0, X)
        Y = check(v, i, 1, Y)

    answer = plus(X, answer)
    answer = plus(Y, answer)

    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))