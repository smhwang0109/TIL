def solution(n):
    answer = 0
    order = 0
    a = 0
    while True:
        order += 2 ** a
        if order > n:
            order -= 2 ** a
            break
        a += 1
    B = list(reversed(str(bin(n - (order + 1)))[2:]))
    answer += 3**a
    for i in range(len(B)):
        if B[i] == '1':
            answer += 3**i


    return answer

print(solution(4))
print(solution(11))