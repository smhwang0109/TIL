from itertools import permutations
from copy import deepcopy

def solution(expression):
    answer = 0
    oper = set()
    L = []
    temp = ''
    for e in expression:
        if e.isnumeric():
            temp += e
        if not e.isnumeric():
            L.append(int(temp))
            temp = ''
            L.append(e)
            oper.add(e)
    L.append(int(temp))
    oper = list(oper)
    p = list(permutations(oper, len(oper)))
    for order in p:
        new_L = deepcopy(L)
        for o in order:
            i = 1
            while True:
                if new_L[i] == o:
                    if o == '+':
                        new_L[i-1] += new_L[i+1]
                    elif o == '-':
                        new_L[i-1] -= new_L[i+1]
                    else:
                        new_L[i-1] *= new_L[i+1]
                    new_L.pop(i+1)
                    new_L.pop(i)
                    if len(new_L) <= i:
                        break
                else:
                    if len(new_L) > i + 2:
                        i += 2
                    else:
                        break
        if answer < abs(new_L[0]):
            answer = abs(new_L[0])
    return answer

print(solution("100-200*300-500+20"))