from itertools import combinations

def check(S1, S2, l):
    cnt = 0
    double = 0
    maxd = 0
    for i in range(l):
        if S1[i] != '0' and S2[i] != '0' and S1[i] == S2[i]:
            cnt += 1
            double += 1

        else:
            if maxd < double:
                maxd = double
            double = 0
    if maxd < double:
        maxd = double
    return cnt+(maxd**2)



def solution(answer_sheet, sheets):
    answer = 0
    wrong_list = []
    l = len(answer_sheet)
    for sheet in sheets:
        wrong = ''
        for i in range(l):
            if sheet[i] == answer_sheet[i]:
                wrong += '0'
            else:
                wrong += sheet[i]
        wrong_list.append(wrong)
    for c in combinations(wrong_list, 2):
        value = check(c[0], c[1], l)
        if answer < value:
            answer = value

    return answer

print(solution("4132315142", ["3241523133","4121314445","3243523133","4433325251","2412313253"]))