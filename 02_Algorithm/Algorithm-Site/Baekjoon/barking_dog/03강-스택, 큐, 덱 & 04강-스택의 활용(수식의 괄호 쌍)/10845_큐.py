import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()

N = int(input())

que = deque()
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        que.append(command[1])
    elif command[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
