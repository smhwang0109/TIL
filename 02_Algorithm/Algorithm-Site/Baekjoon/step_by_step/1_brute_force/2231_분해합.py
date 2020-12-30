
N = int(input())

answer = 0
for n in range(N):
    str_n = str(n)
    temp_n = n
    for elem in str_n:
        temp_n += int(elem)
    if temp_n == N:
        answer = n
        break

print(answer)