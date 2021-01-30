def solution(n, t, m, p):
    answer = ''
    num = 1
    cnt = 0
    tell = 1
    if p == 1:
        answer += '0'
    while num < t * m:
        temp_num = num
        # if num >= n ** cnt:
        for temp_cnt in range(cnt, -1, -1):
            tell += 1
            if temp_num >= n ** temp_cnt:
                result = temp_num // (n ** temp_cnt)
                temp_num %= n ** temp_cnt
                if not (tell - p) % m:
                    if result >= 10:
                        answer += chr(ord('A') + result - 10)
                    else:
                        answer += str(result)
            else:
                if not (tell - p) % m:
                    answer += '0'
            if len(answer) == t:
                return answer

        num += 1

        if num == n ** (cnt + 1):
            cnt += 1
    return answer


print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))