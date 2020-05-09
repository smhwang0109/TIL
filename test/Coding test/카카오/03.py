from collections import deque

def solution(gems):
    answer = []
    gems_set = set(gems)
    gems_list = list(gems_set)
    k = len(gems_list)
    D = {}
    for gem in gems_list:
        D[gem] = 0
    minv = len(gems)
    start = 0
    end = k - 1
    q = deque(gems[:k])
    for gem in q:
        D[gem] += 1
    if 0 not in D.values():
        answer = [start + 1, end + 1]
        return answer
    for gem in gems[k:]:
        q.append(gem)
        D[gem] += 1
        end += 1
        if 0 not in D.values():
            while True:
                if D[q[0]] > 1:
                    temp = q.popleft()
                    D[temp] -= 1
                    start += 1
                else:
                    break
            l = len(q)
            if minv > l:
                minv = l
                answer = [start+1, end+1]
            elif minv == l and not answer:
                answer = [start+1, end+1]
    return answer