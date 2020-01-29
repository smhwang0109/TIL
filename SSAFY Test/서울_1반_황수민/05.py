def q5(number):
    s_num = str(number)
    if len(s_num)!=1:
        for i in range(len(s_num)-1):
            r = int(s_num[i]) - int(s_num[i+1])
            if  r != 1 and r != -1:
                return False
    return True  

print(q5(8))
print(q5(79))
print(q5(5567))
print(q5(4343456))
print(q5(89098))