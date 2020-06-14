# SWEA lv3_5789

test_num = int(input())

for i in range(test_num):
    box_num, work_num = map(int, input().split())
    boxes = [0] * box_num
    print(boxes)
    for j in range(work_num):
        l,r = map(int, input().split())
        for k in range(0, r-l+1):
            boxes[l-1+k] = j + 1
        print(boxes)

    
    print(f'#{i+1}', end='')
    print(''.join(map(str, boxes)))