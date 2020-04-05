def solution(dataSource, tags):
    answer = []
    check = {}
    for data in dataSource:
        cnt = 0
        for d in data[1:]:
            if d in tags:
                cnt += 1
        if cnt:
            if data[0] not in check.keys():
                check[data[0]] = cnt
            else:
                check[data[0]] += cnt
    for num in range(len(tags), 0, -1):
        temp = []
        for key, value in check.items():
            if value == num:
                temp.append(key)
        temp = sorted(temp)
        for t in temp:
            answer.append(t)

    return answer

print(solution(	[["doc1", "t1", "t2", "t3"], ["doc2", "t0", "t2", "t3"], ["doc3", "t1", "t6", "t7"], ["doc4", "t1", "t2", "t4"], ["doc5", "t6", "t100", "t8"]], ["t1", "t2", "t3"]))