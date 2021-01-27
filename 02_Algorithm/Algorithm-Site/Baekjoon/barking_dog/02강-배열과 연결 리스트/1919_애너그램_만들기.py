import sys


input = lambda : sys.stdin.readline().strip()

S1 = input()
S2 = input()

start = ord('a')
alpha_list = [0] * 26

for s in S1:
    alpha_list[ord(s) - start] += 1

for s in S2:
    alpha_list[ord(s) - start] -= 1

total = 0
for alpha_cnt in alpha_list:
    total += abs(alpha_cnt)

print(total)