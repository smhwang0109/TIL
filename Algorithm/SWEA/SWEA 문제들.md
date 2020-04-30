# SWEA 문제들

### 이진수

```python
T = int(input())
for tc in range(1, T+1):
    L, value = input().split()
    result = ''
    for v in value:
        B = str(format(int(v, 16), 'b'))
        if len(B) < 4:
            for i in range(4-len(B)):
                B = '0' + B
        result += B
    print('#{} {}'.format(tc, result))
```

