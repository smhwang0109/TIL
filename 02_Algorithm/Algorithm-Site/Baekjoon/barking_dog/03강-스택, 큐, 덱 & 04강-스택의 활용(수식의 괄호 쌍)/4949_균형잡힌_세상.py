from collections import deque

def check(S):
    stack = deque()
    for s in S:
        if s == '(':
            stack.append('(')
        elif s == '[':
            stack.append('[')
        elif s == ')':
            if not stack:
                print('no')
                return
            elif stack.pop() != '(':
                print('no')
                return
        elif s == ']':
            if not stack:
                print('no')
                return
            elif stack.pop() != '[':
                print('no')
                return
    if stack:
        print('no')
    else:
        print('yes')



while True:
    S = input()

    if S == '.':
        break
    check(S)

