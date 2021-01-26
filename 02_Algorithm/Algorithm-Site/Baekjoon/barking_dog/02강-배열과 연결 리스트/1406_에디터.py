import sys

input = lambda : sys.stdin.readline().strip()

S = list(input())
M = int(input())
idx = len(S) - 1
for _ in range(M):
    command = input()
    if command == 'L':
        idx -= 1
        if idx < -1:
            idx = -1
        continue
    elif command == 'B':
        if idx != -1:
            S.pop(idx)
            idx -= 1
        continue
    elif len(command) == 3:
        S = S[:idx + 1] + [command[-1]] + S[idx+1:]
    idx += 1
    if idx >= len(S):
        idx = len(S) - 1

print(''.join(S))