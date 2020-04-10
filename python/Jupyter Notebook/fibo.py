def fibo_recursion(n):
    '''
    fibonacci 수열을 구하는 함수 (재귀 버전)
    '''
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
    

def fibo_for(n):
    if n < 2: 
        return n
    
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b