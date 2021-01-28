import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()

def solution():
    N = int(input())
    num_list = []
    compare_stack = deque()
    result = [0] * N

    for n in range(N):
        num_list.append((n, int(input())))

    for idx, num in num_list[::-1]:
        while compare_stack:
            if num > compare_stack[-1][1]:
                compare_idx, compare_num = compare_stack.pop()
                result[idx] += result[compare_idx] + 1
            else:
                break

        compare_stack.append((idx, num))

    return sum(result)

print(solution())
