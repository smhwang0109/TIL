def q6(number):
    s_num = str(number)
    for i in range(len(s_num)-2):
        if s_num[i] == s_num[i+2]:
            return True
    return False

print(q6(8))
print(q6(155))
print(q6(1555))
print(q6(2020))
print(q6(414092133))