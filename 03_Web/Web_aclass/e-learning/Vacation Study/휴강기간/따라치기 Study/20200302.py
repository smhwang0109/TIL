# Next permutation in python

def next_permutation(array):

    # 끝에서부터 꼭지위치 i 탐색 (꼭지 : 뒤에서부터 찾을 때 가장 큰 원소)
    i = len(array)-1
    while i > 0 and array[i-1] >= array[i]:
        i -= 1

    # 탈출조건: 더이상 꼭지가 없음
    if i == 0:
        return False

    # 끝에서부터 i-1보다 큰 최초의 j탐색: 최악의 경우에 j == i 찍고 탈출
    j = len(array) - 1
    while array[i-1] >= array[j]:
        j -= 1

    # i-1과 j 원소 스왑
    array[i-1], array[j] = array[j], array[i-1]

    # i부터 끝까지 원소반전 (파이써닉한 반전로직이 있을 듯)
    j = len(array)-1
    while i<j:
        array[i], array[j] = array[j], array[i]
        # 후처리
        i += 1
        j -= 1
    
    return True

'''
넥퍼는 do-while문과 조합하여 오름차순으로 정렬된 최초배열에 대해서 (1,3,5,7,9)
내림차순으로 정렬때까지 순열을 돌려준다. (9,7,5,3,1) 5! = 120
원소가 중복되는 경우에도 걱정없이 사용할 수 있기 때문에
조합에 응용할 수 있다. (0,0,0,1,1)
'''

# case1
odds = [1,3,5,7,9]

count = 0
while True:
    print(odds)
    count += 1
    if next_permutation(odds) == False:
        break #pythonic do-while loop
print(count)

# case2
array = [2,4,6,8,10]
combi = [0,0,1,1,1] #5 C 3

count = 0
while True:
    result = [array[idx] for idx in range(len(combi)) if combi[idx]]
    print(result)

    count += 1
    if not next_permutation(combi):
        break
print(count)