T = int(input())
for case in range(1, T+1):
    test = int(input())
    X = []
    X_a = []
    X_90 = []
    X_180 = []
    X_270 = []

    for __ in range(test):
        X_a.append(0)
    for _ in range(test):
        num = list(map(int,input().split()))
        X.append(num)
        X_90.append(X_a)
    X_180 = X_90
    X_270 = X_180

    for i in range(test):
        for j in range(test):
            X_90[j][test-1-i] = X[i][j]

    print(X_90)