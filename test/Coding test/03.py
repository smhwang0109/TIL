def solution(road, n):
    answer = 0
    state0 = []
    state1 = []
    cnt1 = 0
    cnt0 = 0
    condition = 0
    for r in road:
        if r == '1':
            cnt1 += 1
            if cnt0 and not state1:
                condition = 1
            if cnt0:
                state0.append(cnt0)
                cnt0 = 0
        else:
            if cnt1:
                state1.append(cnt1)
                cnt1 = 0
            cnt0 += 1
    if cnt1:
        state1.append(cnt1)
    if cnt0:
        state0.append(cnt0)

    if n >= sum(state0):
        answer = sum(state1) + sum(state0)
        return answer
    for i in range(len(state0)):
        p = 1
        if n > state0[i]:
            new_n = n - state0[i]
        else:
            new_n = 0
        if condition:
            sumv = state0[i]
        else:
            sumv = state0[i] + state1[i]
        while new_n:
            i += 1
            if new_n >= state0[i]:
                new_n -= state0[i]
            else:
                new_n = 0
                p = 0
            sumv += state0[i] + state1[i]
        if len(state1) > i+1 and p:
            sumv += state1[i+1]
        if answer < sumv:
            answer = sumv
        if i+1 == len(state1)-1 and p:
            return answer
    return answer

print(solution("001100", 5))