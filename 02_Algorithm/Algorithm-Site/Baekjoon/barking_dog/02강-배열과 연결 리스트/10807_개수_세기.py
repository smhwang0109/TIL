N = int(input())
num_list = list(map(int, input().split()))
v = int(input())
cnt = 0
for idx in range(N):
    if num_list[idx] == v:
        cnt += 1

print(cnt)