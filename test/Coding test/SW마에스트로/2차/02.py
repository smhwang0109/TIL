N, M = map(int, input().split())
capa = []
D = {n+1:0 for n in range(N)}
cnt = 1
team = {}
for n in range(N):
    capa.append(list(map(int, input().split())))
for m in range(M):
    a, b = map(int, input().split())
    if D[a] == 0 and D[b] == 0:
        D[a] = cnt
        D[b] = cnt
        cnt += 1
    elif D[a] != 0:
        D[b] = D[a]
    elif D[b] != 0:
        D[a] = D[b]
for key in D.keys():
    if D[key] == 0:
        D[key] = cnt
        cnt += 1
for key, value in D.items():
    if value not in team.keys():
        team[value] = {key}
    else:
        team[value].add(key)
result = 0
for value in team.values():
    minx = 100000000
    miny = 100000000
    maxx = 1
    maxy = 1
    for v in value:
        v -= 1
        if minx > capa[v][0]:
            minx = capa[v][0]
        if miny > capa[v][1]:
            miny = capa[v][1]
        if maxx < capa[v][0]:
            maxx = capa[v][0]
        if maxy < capa[v][1]:
            maxy = capa[v][1]
    sumv = (maxx - minx) * 2 + (maxy - miny) * 2
    if result < sumv:
        result = sumv

print(result)