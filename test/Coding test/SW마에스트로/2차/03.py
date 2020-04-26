N = int(input())
L = []
for n in range(N):
    L.append(list(map(int, input().split())))
for l in L:
    cnt = 0
    for c in L:
        if c[0] < l[0] < c[1]:
            cnt += 1
    print(cnt)