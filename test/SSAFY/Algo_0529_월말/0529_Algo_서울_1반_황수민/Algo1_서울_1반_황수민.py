def check(i, j, n):
    # 행 확인
    for col in range(9):
        if S[i][col] == n:
            return 0
    # 열 확인
    for row in range(9):
        if S[row][j] == n:
            return 0
    # 3X3 박스 확인
    start_i = 3 * (i//3) # 해당 박스 시작 행 결정
    start_j = 3 * (j//3) # 해당 박스 시작 열 결정
    for k in range(start_i, start_i + 3):
        for l in range(start_j, start_j + 3):
            if S[k][l] == n:
                return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(9)]
    result = -1
    for cnt in range(1, N+1):
        i, j, n = map(int, input().split())
        if result == -1: # 이미 result값이 결정됐으면 그냥 통과
            # 중복되는게 하나라도 있는지 체크 
            if not check(i, j, n):
                # 하나라도 있으면 하나 전 수행 횟수까지만 가능하니까 result에 값 할당
                result = cnt - 1
    if result == -1: # 만약 다 돌고도 result가 그대로면 모든 수행 횟수 가능하니까 result에 N을 할당
        result = N
    print("#{} {}".format(tc, result))
