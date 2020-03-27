# 해당 위치에 값 삽입
def put(i, L, num):
    if L[i]:
        L[i] += num
    else:
        L[i] = num

# 어디에 위치해야 하는지 확인
def check(i, L, num):
    if num < 0:
        # 가장자리 확인
        if i-1 == -1:
            put(0, L, -num)
        else:
            put(i-1, L, num)
    else:
        # 가장자리 확인
        if i+1 == 10:
            put(9, L, -num)
        else:
            put(i+1, L, num)

# 테스트 케이스 받아서 해당 횟수만큼 반복
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    for n in range(N):
        temp = [0]*10
        for i in range(10):
            # 절대값이 10 이상인 경우
            if abs(A[i]) >= 10:
                check(i, temp, -abs(A[i]) // 2)
                check(i, temp, +abs(A[i]) // 2)
            # 절대값이 10 미만인 경우
            else:
                check(i, temp, A[i])
        A = temp

    print('#{} {} {} {} {} {} {} {} {} {} {}'.format(tc, *A))