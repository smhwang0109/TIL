def q7(n):
    num_list = [0,1,2,3,4,5]
    count = 0
    for num1 in num_list[1:]:
        for num2 in num_list:
            if num1 != num2:
                if n == num1 + num2:
                    count += 1
    return count*4

print(q7(9))
print(q7(4))