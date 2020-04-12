test_num = int(input())

for i in range(test_num):
    student_num, submit_num = map(int, input().split())
    submit_students = list(map(int, input().split()))

    no_submit_students = []
    for n in range(1, student_num+1):
        if n not in submit_students:
            no_submit_students.append(n)

    result = sorted(no_submit_students)

    print(f'#{i+1}', end='')
    print(''.join(map(str, result)))