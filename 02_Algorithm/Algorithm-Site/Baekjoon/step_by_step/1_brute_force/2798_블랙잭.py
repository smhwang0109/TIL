N, M = map(int, input().split())
num_list = list(map(int, input().split()))
L = len(num_list)

max_v = 0
sum_v = 0

for first_idx in range(L-2):
    sum_v += num_list[first_idx]
    for second_idx in range(first_idx + 1, L-1):
        sum_v += num_list[second_idx]
        for third_idx in range(second_idx + 1, L):
            sum_v += num_list[third_idx]
            if sum_v <= M and sum_v > max_v:
                max_v = sum_v
            sum_v -= num_list[third_idx]
        sum_v -= num_list[second_idx]
    sum_v -= num_list[first_idx]

print(max_v)
