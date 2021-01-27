import sys

input = lambda : sys.stdin.readline().strip()

num_list = [0] * 10
total = 1
for _ in range(3):
    total *= int(input())

for t in str(total):
    num_list[int(t)] += 1

for num in num_list:
    print(num)