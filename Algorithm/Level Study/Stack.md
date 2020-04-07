# Stack

# BaekJoon study

### 10828. 스택

```python
import sys

input = sys.stdin.readline

class stack():

    def __init__(self):
        self.data = []

    def push(self, X):
        self.data.append(X)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.data.pop()

    def size(self):
        return len(self.data)

    def empty(self):
        if self.data:
            return 0
        else:
            return 1

    def top(self):
        if self.empty():
            return -1
        else:
            return self.data[-1]

Stack = stack()
N = int(input())
for i in range(N):
    order = input().split()
    if order[0] == 'push':
        Stack.push(order[1])
    elif order[0] == 'pop':
        print(Stack.pop())
    elif order[0] == 'size':
        print(Stack.size())
    elif order[0] == 'empty':
        print(Stack.empty())
    else:
        print(Stack.top())
```

```python
# 강사님 풀이

import sys

T = int(sys.stdin.readline())

stack = []

for _ in range(T):
    D = sys.stdin.readline().split()
    if D[0] == 'push':
        stack.append(D[1])
    elif D[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    elif D[0] == 'size':
        print(len(stack))
    elif D[0] == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif D[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
```



### 10773. 제로

```python
from collections import deque

stack = deque()

K = int(input())

for _ in range(K):
    N = int(input())
    if N:
        stack.append(N)
    else:
        stack.pop()
print(sum(stack))
```

```python
# 강사님 풀이
import sys

T = int(sys.stdin.readline())

stack = []

for _ in range(T):
    D = int(sys.stdin.readline())

    if D == 0:
        if len(stack) != 0:
            stack.pop()
    else:
        stack.append(D)

print(sum(stack))

```

### 9012. 괄호

```python
from collections import deque

T = int(input())

for _ in range(T):
    stack = deque()
    result = 'YES'
    S = list(input())
    for i in S:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                result = 'NO'
                break
    if stack:
        result = 'NO'

    print(result)
```

```python
# 강사님 풀이

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    D = sys.stdin.readline().strip()
    stack = []
    for p in D:
        if p == '(':
            stack.append(p)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
```

```python
# 강사님 풀이
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    D = sys.stdin.readline().strip()
    stack = 0
    for p in D:
        if p == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            print('NO')
            break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
```

### 1874. 스택 수열

```python
from collections import deque


n = int(input())
numbers = deque([])
for i in range(1, n+1):
    num = int(input())
    numbers.append(num)
stack = deque([0])
k = 1
s = numbers.popleft()
result = []
while True:
    if s == stack[-1]:
        stack.pop()
        result.append('-')
        s = numbers.popleft()
    else:
        stack.append(k)
        result.append('+')
        k += 1
    if k > n:
        break
while len(stack) > 1:
    if s == stack[-1]:
        stack.pop()
        result.append('-')
        if numbers:
            s = numbers.popleft()
    else:
        result = ['NO']
        break

for r in result:
    print(r)
```

### 1406. 에디터

```python
from collections import deque

S = input()
M = int(input())
stack = deque(S)
temp = deque()
for i in range(M):
    order = input().split()
    if order[0] == 'L':
        if stack:
            temp.appendleft(stack.pop())
    elif order[0] == 'D':
        if temp:
            stack.append(temp.popleft())
    elif order[0] == 'B':
        if stack:
            stack.pop()
    elif order[0] == 'P':
        stack.append(order[1])

for i in temp:
    stack.append(i)
print(''.join(stack))
```

### 4949. 균형잡힌 세상

```python
from collections import deque

while True:
    stack = deque()
    result = 'yes'
    S = input()
    if S == '.':
        break
    for i in S:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 'no'
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = 'no'
                break
    if stack:
        result = 'no'
    print(result)
```

### 2493. 탑

```python
import sys
from _collections import deque

input = sys.stdin.readline

N = int(input())
Q = deque(map(int, input().split()))
stack = deque()
result = [0]*N
for i in range(N-1, -1, -1):
    q = Q.pop()
    if not stack:
        stack.append([q, i])
    else:
        while stack:
            if stack[-1][0] <= q:
                s = stack.pop()
                result[s[1]] = i+1
            else:
                break
        stack.append([q, i])

print(' '.join(map(str, result)))

```





# SWEA study

### 4886. 괄호검사 

```python
from collections import deque

T = int(input())

for case in range(1, T+1):
    stack = deque()
    result = 1
    S = list(input())
    for i in S:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 0
                break
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                result = 0
                break
    if stack:
        result = 0

    print('#{} {}'.format(case, result))
```

### 4873. 반복문자 지우기

```python
from collections import deque

T = int(input())

for case in range(1, T+1):
    stack = deque()
    S = list(input())
    for i in S:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    print('#{} {}'.format(case, len(stack)))
```

```python
# 강사님 풀이

T = int(input())

for tc in range(1, T+1):
    stack = []
    D = input()
    for c in D:
        if stack:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    print('#{} {}'.format(tc, len(stack)))

```

### 

```python

```

### 

```python

```



# programmers

### 올바른 괄호

```python
from collections import deque


def solution(s):
    stack = deque()
    answer = True
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                break
    if stack:
        answer = False

    return answer
```

### 탑

```python
def solution(heights):
    answer = []
    for i in range(len(heights)-1,0,-1):
        j = i-1
        while j >= 0:
            if heights[i] < heights[j]:
                if answer:
                    answer.insert(0,j+1)
                else:
                    answer.append(j+1)
                break
            else:
                j -= 1
            if j == -1:
                if answer:
                    answer.insert(0,0)
                else:
                    answer.append(0)
                break
    if answer:
        answer.insert(0, 0)
    else:
        answer.append(0)

    return answer
```

```python
# 강사님 풀이
def solution(heights):
    answer = []
    for i in range(len(heights)):
        for j in range(i, -1, -1):
            if heights[i] < heights[j]:
                answer.append(j+1)
                break
        else:
            answer.append(0)

    return answer
```

```python
# 강사님 풀이 Stack 풀이
def solution(heights):
    answer = []

    for i in range(len(heights)):
        stack = []
        for j in range(i):
            if heights[i] < heights[j]:
                stack.append(j+1)
        if len(stack) != 0:
            answer.append(stack.pop())
        else:
            answer.append(0)
    return answer
```

### 주식가격

```python
from collections import deque


def solution(prices):
    answer = []
    prices1 = deque(prices)
    for i in range(len(prices)):
        cnt = 0
        a = prices1.popleft()
        for j in range(i+1,len(prices)):
            if a <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer

print(solution([1,2,3,2,3]))
```

```python
# 강사님 풀이
def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)

    return answer
```

```python
# 강사님 풀이
def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)

    return answer
```

```python
# Stack 풀이
def solution(prices):
    stack = []
    result = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            x = stack.pop()
            result[x] = i - x
        stack.append(i)
    while stack:
        x = stack.pop()
        result[x] = i - x
    return result
```



### 쇠막대기

```python
from collections import deque


def solution(arrangement):
    stack = deque()
    answer = 0
    cnt = 0
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stack.append('(')
            cnt += 1
        else:
            if arrangement[i-1] == '(':
                stack.pop()
                cnt -= 1
                answer += cnt
            else:
                cnt -= 1
                answer += 1
                stack.pop()
    answer += cnt
    return answer

```

```

```





