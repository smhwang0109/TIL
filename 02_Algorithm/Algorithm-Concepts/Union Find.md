# Union Find

> Union Find 는 그래프 알고리즘의 일종으로 상호 배타적 집합(Disjoint-set) 이라고도 하며, 같은 집합에 포함되어 있는지 확인하는 알고리즘입니다.

## 1. 기본 구현

> 기본 구현

```python
def find(num):
    if parent[num] == num:
        return num
    else:
        return find(parent[num])

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a == parent_b:
        return
    else:
        parent[parent_b] = parent_a
        return
```

- 시간복잡도 : O(N)

- 단점

  - 시간복잡도가 커서 시간초과 오류 발생

  

## 2. find, union 최적화

> 시간 복잡도를 줄이기 위한 방법

```python
def find(num):
    if parent[num] == num:
        return num
    else:
        parent[num] = find(parent[num])
        return parent[num]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a == parent_b:
        return
    elif level[parent_a] > level[parent_b]:
        parent[parent_b] = parent_a
        return
    elif level[parent_a] < level[parent_b]:
        parent[parent_a] = parent_b
        return
    else:
        parent[parent_b] = parent_a
        level[parent_a] += 1
        return 
```

- 시간복잡도 : O(logN)

- 단점

  - parent, level 배열을 두 가지 쓰기 때문에 메모리를 많이 사용

  

## 3. Weighted Union Find

> 메모리 줄이기 위한 방법

```python
def find(num):
    if parent[num] < 0:
        return num

    parent[num] = find(parent[num])
    return parent[num]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a == parent_b:
        return


    if parent[parent_a] < parent[parent_b]:
        parent[parent_b] = parent_a
    elif parent[parent_a] > parent[parent_b]:
        parent[parent_a] = parent_b
    else:
        parent[parent_a] -= 1
        parent[parent_b] = parent_a
```

- parent[x] < 0
  - root 노드
- parent[x] >= 0
  - 부모 노드

