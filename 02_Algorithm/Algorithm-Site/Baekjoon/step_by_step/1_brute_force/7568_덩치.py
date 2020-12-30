N = int(input())

people_info = []

for n in range(N):
    people_info.append(list(map(int, input().split())))

answer = [1] * N
for origin in range(N):
    origin_person = people_info[origin]
    for compare in range(origin + 1, N):
        compare_person = people_info[compare]
        if origin_person[0] > compare_person[0] and origin_person[1] > compare_person[1]:
            answer[compare] += 1
        elif origin_person[0] < compare_person[0] and origin_person[1] < compare_person[1]:
            answer[origin] += 1

for idx in range(N):
    if idx == N-1:
        print(answer[idx])
    else:
        print(answer[idx], end=' ')