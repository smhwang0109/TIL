'''
Python How To Break Multiple Loops

Java에는 labled statements라고 하여 break 한방으로 라벨링한 반복문까지 탈출하는 문법이 있다. 반면, Python에는 그런 도구는 없는데, 주로 함수로 빼서 return 예약어를 사용하면 충분하기 때문으로 보인다. 다만 아래와 같은 방법도 고려해볼 수 있을 것 같다.
'''

N = 3
num = 7
matrix = [[0 for _ in range(N)] for _ in range(N)]
matrix[2][1] = 6

loop_breaker = False
for i in range(N):
    for j in range(N):
        for k in range(1, num):
            if matrix[i][j] = k:
                print(i,j)
                loop_breaker = True
                break
        if loop_breaker:
            break
    if loop_breaker:
        break
