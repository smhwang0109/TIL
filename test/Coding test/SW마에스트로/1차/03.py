N, K = map(int, input().split())
L = list(map(int, input().split()))
sub = [0] * (N-1)
for i in range(N-1):
    sub[i] = L[i+1] - L[i]
sub = sorted(sub)[:N-1-(K-1)]
print(sum(sub))