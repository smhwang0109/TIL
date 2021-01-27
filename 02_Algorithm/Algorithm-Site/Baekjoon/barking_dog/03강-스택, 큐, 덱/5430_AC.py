import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()

def solution():
    p = input()
    n = int(input())
    num_deque = deque(input()[1:-1].split(','))
    is_back = False
    for command in p:
        if command == 'R':
            is_back = not is_back
        if command == 'D':
            if not num_deque:
                return 'error'
            if is_back:
                num = num_deque.pop()
            else:
                num = num_deque.popleft()
            if not num:
                return 'error'
    if is_back:
        num_deque = reversed(num_deque)
    return '[' + ','.join(num_deque) + ']'

T = int(input())
for tc in range(T):
    print(solution())