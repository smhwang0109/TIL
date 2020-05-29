def give(n, cnt): # n은 현재 줄 사탕 번호, cnt는 현재까지 사탕 종류 총합
    global M, sumv
    # 어차피 cnt는 1개씩 늘기 때문에
    # 줄 수 있는 사탕 종류 개수 합이 가장 큰 결과값에서 cnt와의 차이보다 작거나 같으면
    # 아무리 돌아도 현재까지 결과값보다 클 수 없으므로 돌 필요 없이 멈춘다.
    if M - n + 1 <= sumv - cnt:
        return
    if n > M: # 사탕을 다 나눠줬을 때
        if sumv < cnt:
            sumv = cnt
        return
    for i in range(len(L)):
        if not visited[i]:
            visited[i] = 1
            origin = len(L[i])
            L[i].add(n)
            if len(L[i]) == origin: # set으로 만들었기 때문에 하나 추가했는데 기존과 개수가 같으면 다음 사탕번호로 넘어갈 때 cnt는 그대로
                give(n + 1, cnt)
            else: # 기존과 개수가 다르면 cnt에도 1추가한다.
                give(n + 1, cnt +1)
                L[i].remove(n)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 사탕 개수를 빼기 위해 1번 인덱스부터 가져오고
    # set을 이용하여 값을 받아올 때 중복 없애기
    L = [set(list(map(int, input().split()))[1:]) for _ in range(N)]
    sumv = 0
    cnt = 0
    # 현재까지 사탕의 종류 총합을 구한다.
    for l in L:
        cnt += len(l)
    if N > M:  # 사탕 종류보다 어린이 인원수가 더 많을 때 사탕 번호보다 높은 번호를 가진 어린이는 제외한다.
        L = L[:M]
    else:  # 어린이 인원수보다 사탕 종류가 같거나 더 많을 때 재귀를 멈출 조건을 정하기 위해 M에 N값을 넣는다.
        M = N
    visited = [0] * len(L)
    give(1, cnt)
    print('#{} {}'.format(tc, sumv))