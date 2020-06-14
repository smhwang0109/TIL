T = int(input())
for case in range(1, T+1):
    num = list(map(int,input().split()))
    puzzle_list = []
    for i in range(num[0]):
        puzzle = input()
        puzzle_list.append(puzzle)
    count_sum = 0
    count_horizontal = 0
    for n in range(num[1],num[0]+1):
        for k in range(num[0]):
            if n == num[1]:
                if '1 '*n in puzzle_list[k]:
                    count_horizontal += 1
            else:
                if '1 '*n in puzzle_list[k]:
                    count_horizontal -= 1
            if count_horizontal > 0:
                count_sum += count_horizontal
    print(count_sum)