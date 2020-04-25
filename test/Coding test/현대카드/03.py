def solution(registered_list, new_id):
    answer = ''
    if new_id not in registered_list:
        answer = new_id
        return answer
    S = ''
    for i in range(len(new_id)):
        if new_id[i].isnumeric():
            S = new_id[:i]
            N = new_id[i:]
            break
    if not S:
        S = new_id
        N = 0
    while True:
        N = str(int(N)+1)
        new_id = S+N
        if new_id not in registered_list:
            answer = new_id
            return answer

print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))