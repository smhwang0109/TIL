import sys
from collections import deque


input = lambda : sys.stdin.readline().strip()


N, M = map(int, input().split())
goal_list = deque(map(int, input().split()))

deq = deque(range(1, N + 1))

answer = 0
cnt = 0
goal = goal_list.popleft()
while True:
    num = deq.popleft()
    if num == goal:
        if N - cnt < cnt:
            cnt = N - cnt
        N -= 1
        answer += cnt
        cnt = 0
        if goal_list:
            goal = goal_list.popleft()
        else:
            break
    else:
        deq.append(num)
        cnt += 1

print(answer)
