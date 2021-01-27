N = int(input())

num_list = [0] * 10
for s in str(N):
    num_list[int(s)] += 1

max_v = 0

temp = 0
for num in range(len(num_list)):
    if num == 6:
        temp = num_list[6]
    elif num == 9:
        temp = (temp + num_list[9] - 1) // 2 + 1
        if max_v < temp:
            max_v = temp
    else:
        if max_v < num_list[num]:
            max_v = num_list[num]

print(max_v)