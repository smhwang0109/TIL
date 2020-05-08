N = int(input())
result = 0
if not N % 2:
    result = '1'*(N//2)
else:
    result = '7' + '1'*(N//2 -1)

print(result)