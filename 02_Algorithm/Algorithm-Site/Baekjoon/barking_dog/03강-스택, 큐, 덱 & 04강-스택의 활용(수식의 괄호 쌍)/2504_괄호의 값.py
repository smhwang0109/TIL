import sys
from collections import deque


input = lambda : sys.stdin.readline().strip()

def solution():
    S = input()

    stack = deque()
    answer = 0
    multi = 1

    pre_s = False
    for s in S:
        if s == '(':
            multi *= 2
            stack.append(s)
        elif s == '[':
            multi *= 3
            stack.append(s)
        elif s == ')':
            if not stack:
                return 0
            elif stack.pop() != '(':
                return 0
            multi //= 2
            if pre_s == '(':
                answer += 2 * multi
        elif s == ']':
            if not stack:
                return 0
            elif stack.pop() != '[':
                return 0
            multi //= 3
            if pre_s == '[':
                answer += 3 * multi
        pre_s = s

    if stack:
        return 0
    return answer

print(solution())
