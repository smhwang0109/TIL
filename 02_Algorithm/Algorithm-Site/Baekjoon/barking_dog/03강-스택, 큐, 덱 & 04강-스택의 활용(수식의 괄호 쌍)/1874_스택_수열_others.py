import sys
from collections import deque


input = lambda: sys.stdin.readline().strip()

def solution():
    n = int(input())
    compare_list = [int(input()) for _ in range(n)]
    stack = deque()
    answer = []

    num = 1

    for compare in compare_list:
        while num <= compare:
            stack.append(num)
            answer.append('+')
            num += 1
        if stack.pop() != compare:
            return 'NO'
        else:
            answer.append('-')

    return '\n'.join(map(str, answer))


print(solution())
