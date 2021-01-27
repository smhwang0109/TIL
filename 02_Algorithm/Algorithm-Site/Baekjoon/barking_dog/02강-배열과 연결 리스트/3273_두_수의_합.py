import sys


input = lambda : sys.stdin.readline().strip()

n = int(input())
num_list = list(map(int, input().split()))
x = int(input())

max_v = max(num_list)
visited = [0] * (max_v + 1)

result = 0

for num in num_list:
    if x > num and max_v >= x - num and visited[x - num]:
        result += 1
    visited[num] = 1

print(result)
