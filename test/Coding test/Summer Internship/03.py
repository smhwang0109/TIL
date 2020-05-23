def check(n):
    global D, answer
    for d in D[n]:
        if not D[d]:
            answer[n] += 1
            answer[d] = 1
            continue
        answer[n] += check(d)
    return answer[n]


def solution(total_sp, skills):
    global D, answer
    answer = [0] * (len(skills) + 2)
    D = {i:[] for i in range(1, len(skills) + 2)}
    search = [0] * (len(skills) + 2)
    for n1, n2 in skills:
        D[n1].append(n2)
        if not search[n2]:
            search[n2] = 1
    for s in range(1, len(search)):
        if not search[s]:
            first = s
            break
    check(first)
    C = total_sp//sum(answer)
    for i in range(len(answer)):
        answer[i] *= C

    return answer[1:]

print(solution(121, [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]))