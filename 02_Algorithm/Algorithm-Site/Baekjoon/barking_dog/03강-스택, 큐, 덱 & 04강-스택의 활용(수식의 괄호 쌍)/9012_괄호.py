import sys

input = lambda : sys.stdin.readline().strip()

def solution():
    S = input()
    cnt = 0
    for s in S:
        if s == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return 'NO'
    if cnt:
        return 'NO'
    else:
        return 'YES'

T = int(input())
for tc in range(T):
    print(solution())