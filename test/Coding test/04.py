def solution(snapshots, transactions):
    log = set()
    for t in transactions:
        if t[0] not in log:
            log.add(t[0])
            if t[1] == "SAVE":
                for i in range(len(snapshots)):
                    if t[2] == snapshots[i][0]:
                        snapshots[i][1] = str(int(snapshots[i][1])+int(t[3]))
                        break
                else:
                    snapshots.append([t[2],t[3]])
            elif t[1] == "WITHDRAW":
                for i in range(len(snapshots)):
                    if t[2] == snapshots[i][0]:
                        snapshots[i][1] = str(int(snapshots[i][1])-int(t[3]))
                        break
    return snapshots

print(solution(	[["ACCOUNT1", "100"], ["ACCOUNT2", "150"]], [["1", "SAVE", "ACCOUNT2", "100"], ["2", "WITHDRAW", "ACCOUNT1", "50"], ["1", "SAVE", "ACCOUNT2", "100"], ["4", "SAVE", "ACCOUNT3", "500"], ["3", "WITHDRAW", "ACCOUNT2", "30"]]))