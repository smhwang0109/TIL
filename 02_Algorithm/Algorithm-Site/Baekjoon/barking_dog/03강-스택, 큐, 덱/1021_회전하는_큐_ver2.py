import sys


input = lambda : sys.stdin.readline().strip()


N, M = map(int, input().split())
goal_list = list(map(int, input().split()))
num_list = list(range(1, N + 1))

answer = 0
pre_idx = 0
for goal in goal_list:
    cur_idx = num_list.index(goal)
    cnt = abs(cur_idx - pre_idx)
    answer += min(N - cnt, cnt)
    num_list.pop(cur_idx)
    N -= 1
    pre_idx = cur_idx

print(answer)