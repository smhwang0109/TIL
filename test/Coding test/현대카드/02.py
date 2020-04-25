from collections import Counter, deque

def solution(ip_addrs, langs, scores):
    answer = 0
    D = Counter(ip_addrs)
    two = deque()
    three = deque()
    for key, value in D.items():
        if value == 1:
            answer += 1
        elif value == 2:
            two.append(key)
        elif value == 3:
            three.append(key)
    for t in two:
        lang = 0
        for i in range(len(ip_addrs)):
            if ip_addrs[i] == t:
                if lang:
                    if lang == 'C' or lang == 'C++' or lang == 'C#':
                        if langs[i] == 'C' or langs[i] == 'C++' or langs[i] == 'C#':
                            if score != scores[i]:
                                answer += 2
                        else:
                            answer += 2
                    elif lang == langs[i]:
                        if score != scores[i]:
                            answer += 2
                    else:
                        answer += 2
                    break
                else:
                    lang = langs[i]
                    score = scores[i]
    for t in three:
        cnt = 0
        lang = 0
        for i in range(len(ip_addrs)):
            if ip_addrs[i] == t:
                if lang:
                    if lang == 'C' or lang == 'C++' or lang == 'C#':
                        if langs[i] != 'C' and langs[i] != 'C++' and langs[i] != 'C#':
                            answer += 3
                            break
                    elif lang != langs[i]:
                        answer += 3
                        break
                else:
                    lang = langs[i]
                cnt += 1
                if cnt == 3:
                    break


    return answer

print(solution(["5.5.5.5", "155.123.124.111", "10.16.125.0", "155.123.124.111", "5.5.5.5", "155.123.124.111", "10.16.125.0", "10.16.125.0"], ["Java", "C++", "Python3", "C#", "Java", "C", "Python3", "JavaScript"], [294, 197, 373, 45, 294, 62, 373, 373]))