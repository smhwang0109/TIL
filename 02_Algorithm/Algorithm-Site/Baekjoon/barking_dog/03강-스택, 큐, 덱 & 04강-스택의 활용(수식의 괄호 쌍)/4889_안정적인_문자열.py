import sys
from collections import deque


def solution(S):
    stack = deque()
    answer = 0
    for s in S:
        if s == '{':
            stack.append(True)
        elif s == '}':
            if stack:
                stack.pop()
            else:
                stack.append(True)
                answer += 1
    if stack:
        answer += len(stack) // 2
    return answer


input = lambda : sys.stdin.readline().strip()

cnt = 0
while True:
    cnt += 1
    S = input()
    if '-' in S:
        break
    print('{}. {}'.format(cnt, solution(S)))