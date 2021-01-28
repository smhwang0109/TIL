import sys
from collections import deque


input = lambda : sys.stdin.readline().strip()

def solution():
    N = int(input())

    input_data = list(map(int, input().split()))
    num_list = []
    for idx in range(len(input_data)):
        num_list.append((idx, input_data[idx]))
    L = len(num_list)

    compare_stack = deque()

    answer = [0] * L

    for idx, num in num_list[::-1]:
        while compare_stack:
            if num >= compare_stack[-1][1]:
                compare_idx, compare_num = compare_stack.pop()
                answer[compare_idx] = idx + 1
            else:
                break
        compare_stack.append((idx, num))

    return answer

print(' '.join(map(str, solution())))
