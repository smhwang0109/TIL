import sys


input = lambda : sys.stdin.readline().strip()

N, K = map(int, input().split())
girls = [0] * 7
boys = [0] * 7
for n in range(N):
    S, Y = map(int, input().split())
    if not S:
        girls[Y] += 1
    else:
        boys[Y] += 1

room_cnt = 0
for idx in range(1, 7):
    if girls[idx]:
        room_cnt += ((girls[idx] - 1) // K) + 1
    if boys[idx]:
        room_cnt += ((boys[idx] - 1) // K) + 1
print(room_cnt)