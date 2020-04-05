def solution(inputString):
    answer = -1
    L = [0]*4
    cnt = 0
    for s in inputString:
        if s == '(':
            L[0] += 1
        elif s == ')':
            if L[0] == 0:
                return answer
            L[0] -= 1
            cnt += 1
        elif s == '{':
            L[1] += 1
        elif s == '}':
            if L[1] == 0:
                return answer
            L[1] -= 1
            cnt += 1
        elif s == '[':
            L[2] += 1
        elif s == ']':
            if L[2] == 0:
                return answer
            L[2] -= 1
            cnt += 1
        elif s == '<':
            L[3] += 1
        elif s == '>':
            if L[3] == 0:
                return answer
            L[3] -= 1
            cnt += 1

    if sum(L) == 0:
        answer = cnt

    return answer