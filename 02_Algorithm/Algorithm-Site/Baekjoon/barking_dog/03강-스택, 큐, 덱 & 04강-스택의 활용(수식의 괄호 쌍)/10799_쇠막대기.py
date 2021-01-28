import sys
from collections import deque

input = lambda : sys.stdin.readline()

S = input()[:-1]
stack = deque()
answer = 0

for idx in range(len(S)):
    if S[idx] == '(':
        stack.append(True)
    else:
        stack.pop()
        if S[idx - 1] == '(':
            answer += len(stack)
        else:
            answer += 1

print(answer)