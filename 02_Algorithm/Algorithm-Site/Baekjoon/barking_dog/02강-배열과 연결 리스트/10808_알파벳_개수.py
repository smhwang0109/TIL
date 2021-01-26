import sys

input = lambda : sys.stdin.readline().strip()

S = input()

start = ord('a')
alpha_list = [0] * 26

for s in S:
    idx = ord(s) - start
    alpha_list[idx] += 1

print(' '.join(map(str, alpha_list)))