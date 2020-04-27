# 위, 오른위, 오른쪽, 오른아래, 아래, 왼아래, 왼쪽, 왼위 순서대로 각 행과 열 index 변화 리스트
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for t in range(1, T+1):
    # 영역 크기 n, 광맥지도 board 를 입력받아 주는 코드
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 한 번 채굴용 로봇이 지나간 지역을 다시 검사하는 일을 막기 위한 체크용 맵.
    chk = [[False for _ in range(n)] for __ in range(n)]

    # 정답으로 쓰일 광맥들 중 최대 매장량
    maxi = 0
    # 정답으로 쓰일 최대 매장 광맥의 면적
    maxi_area = 0
    for r in range(n):
        for c in range(n):
            # 매장량이 0이 아니고, 채굴용 로봇이 지나간 적 없다면 채굴시작.
            if board[r][c] and not chk[r][c]:
                value = board[r][c]  # 탐색 시작할 광맥의 단위 값
                cnt = board[r][c]  # 광맥 매장량. 단위 값을 더하고 시작함.(현위치 채굴완료)
                area = 1  # 광맥 면적. 1으로 시작 (현위치 채굴완료)
                chk[r][c] = True  # 현재 채굴한 위치 체크
                q = [(r, c)] # 자료구조 Queue 이용한 bfs 사용 예정
                while q:
                    sr, sc = q.pop(0) # 큐에서 탐색시작 위치 가져오기
                    for d in range(8): # 전방향 탐색
                        nr, nc = sr + dr[d], sc + dc[d]
                        if nr < 0 or nc < 0 or nr >= n or nc >= n or chk[nr][nc]:
                            continue  # 탐색위치를 벗어나거나 이미 채굴 로봇이 지나간 곳이면 검사하지 않음
                        if board[nr][nc] == value: # 광맥의 단위 값이 일치하면 (동일한 광맥이면)
                            cnt += value # 매장량 더하기
                            area += 1 # 광맥 면적 더하기
                            chk[nr][nc] = True # 채굴했음을 표시
                            q.append((nr, nc)) # 큐에 현재 위치 추가

                if cnt > maxi: # 매장량이 더 많을 경우 업데이트
                    maxi = cnt
                    maxi_area = area
                elif cnt == maxi: # 매장량은 같지만,
                    if maxi_area > area: # 면적이 더 작을 경우 업데이트
                        maxi_area = area

    print("#{} {} {}".format(t, maxi, maxi_area))
