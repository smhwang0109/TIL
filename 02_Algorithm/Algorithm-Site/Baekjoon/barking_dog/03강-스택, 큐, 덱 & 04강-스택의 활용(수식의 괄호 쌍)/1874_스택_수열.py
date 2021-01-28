import sys
from collections import deque


input = lambda: sys.stdin.readline().strip()

n = int(input())
compare_que = deque()
stack = deque()
answer = []

for _ in range(n):
    compare_que.append(int(input()))

compare_num = compare_que.popleft()
for num in range(1, n + 1):
    if num < compare_num:
        stack.append(num)
        answer.append('+')
    elif num == compare_num:
        answer.append('+')
        answer.append('-')
        flag = False
        while compare_que:
            compare_num = compare_que.popleft()
            if compare_num > num:
                break
            elif compare_num < num:
                if stack and compare_num == stack[-1]:
                    num = stack.pop()
                    answer.append('-')
                else:
                    flag = True
                    break
            else:
                raise RuntimeError
        if flag:
            print('NO')
            break
    else:
        flag = True
        print('NO')
        break

if not flag:
    for a in answer:
        print(a)
