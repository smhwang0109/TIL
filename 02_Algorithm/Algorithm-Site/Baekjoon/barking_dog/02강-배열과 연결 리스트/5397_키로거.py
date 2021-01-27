import sys
from collections import deque


input = lambda : sys.stdin.readline().strip()

T = int(input())
for tc in range(T):
    L = list(input())
    left_stack = deque()
    right_stack = deque()
    for l in L:
        if l == '<':
            if left_stack:
                right_stack.appendleft(left_stack.pop())
        elif l == '>':
            if right_stack:
                left_stack.append(right_stack.popleft())
        elif l == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(l)

    print(''.join(left_stack+right_stack))