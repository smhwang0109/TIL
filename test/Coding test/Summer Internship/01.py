from collections import Counter

def solution(p):
    while True:
        p += 1
        if len(Counter(str(p))) == 4:
            break
    return p

print(solution(1987))
print(solution(2015))