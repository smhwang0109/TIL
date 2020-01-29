def q3(number):
    m1 = number%10**2
    m2 = m1%10
    if number % 4:
        return False
    
    elif m1 % 3:
        return False
    
    elif m2 % 2:
        return False
    return True

print(q3(512))
print(q3(384))
print(q3(321))