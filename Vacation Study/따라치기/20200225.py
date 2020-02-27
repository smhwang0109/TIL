# SWEA - course - IM - Tree - 5174 Subtree

def f(v):
    global cnt
    cnt += 1
    for u in tree[v]:
        f(u)

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    d = list(map(int, input().split()))

    tree = [[] for _ in range(E+2)]
    for i in range(E):
        p = d[2*i]
        c = d[2*i+1]
        tree[p].append(c)

    cnt = 0
    f(N)
    
    print('#{} {}'.format(tc, cnt))