T = int(input())
for case in range(1, T+1):
    N = int(input())
    count = 0
    s = set()
    while len(s) < 10:
        count += 1
        c = count * N
        for i in range(6,-1,-1):
            m = c//10**i
            if m != 0:
                l = i
                break
        for k in range(l,-1,-1):
            m = c // 10 ** k
            s.add(m)
            c -= m*10**k
    print('#{} {}'.format(case, count*N))