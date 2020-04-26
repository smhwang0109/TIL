from _collections import deque

def check(answer, sum_day, price):
    if price < 10000:
        answer[0] += sum_day
    elif price < 20000:
        answer[1] += sum_day
    elif price < 50000:
        answer[2] += sum_day
    elif price < 100000:
        answer[3] += sum_day
    else:
        answer[4] += sum_day

def solution(purchase):
    answer = [0, 0, 0, 0, 0]
    que = deque()
    cur_price = 0
    for i in range(len(purchase)):
        date, price = purchase[i].split()
        datelist = date.split('/')
        if i == 0:
            sum_day = month_day[:int(datelist[1])-1] + int(datelist[2])-1
            answer[0] += sum_day
        datecount = sum(month_day[:int(datelist[1])]) + int(datelist[2])
        que.append([datecount, price])
        while True:
            i = 0
            if datecount == que[i][0]:
                break
            if datecount - que[i][0] > 30:
                sum_day = 30
                d, price = que.popleft()
                cur_price += price
                check(answer, sum_day, cur_price)
                cur_price = 0
            else:
                sum_day += datecount - que[i][0]
                cur_price += que[i][0]




    return answer

month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"])