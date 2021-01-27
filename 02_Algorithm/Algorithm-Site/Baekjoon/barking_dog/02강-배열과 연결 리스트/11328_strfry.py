import sys


input = lambda : sys.stdin.readline().strip()

start = ord('a')
N = int(input())
for tc in range(N):
    A_list = [0] * 26
    B_list = [0] * 26
    A, B = input().split()
    for a in A:
        A_list[ord(a) - start] += 1
    for b in B:
        B_list[ord(b) - start] += 1
    if A_list == B_list:
        print("Possible")
    else:
        print("Impossible")