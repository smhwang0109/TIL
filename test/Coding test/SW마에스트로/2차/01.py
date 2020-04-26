N = int(input())
L = list(map(int, input().split()))
sumv = 0
maxv = -1000000
for l in L:
    sumv += l
    if maxv < sumv:
        maxv = sumv
    if sumv < 0:
        sumv = 0
print(maxv)

