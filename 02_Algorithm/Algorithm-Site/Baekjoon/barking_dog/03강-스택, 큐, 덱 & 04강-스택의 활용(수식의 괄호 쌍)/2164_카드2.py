import sys
from collections import deque

input = lambda : sys.stdin.readline()

N = int(input())

que = deque(range(N, 0, -1))
while len(que) != 1:
    que.pop()
    que.appendleft(que.pop())

print(que.pop())