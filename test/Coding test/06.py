def solution(directory, command):
    for c in command:
        cmd = []
        c = c.split()
        if c[0] == 'mkdir':
            directory.append(c[1])
        elif c[0] == 'cp':
            temp = []
            for d in directory:
                if d.startswith(c[1]):
                    directory.append(c[2]+c[1])
                    temp.append(d)
            for t in temp:
                directory.remove(t)
        elif c[0] == 'rm':
            for d in directory:
                

    return directory

print(solution(["/", "/hello", "/hello/tmp", "/root", "/root/abcd", "/root/abcd/etc", "/root/abcd/hello"], ["mkdir /root/tmp", "cp /hello /root/tmp", "rm /hello"]))