# 순열과 조합 (permutations, combinations)

## itertools
- 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
### permutations
- 리스트와 같은 iterable 객체엥서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해준다.
- permutations 는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
- ex) 리스트 ['A', 'B', 'C']에서 3개(r = 3)를 뽑아 나열하는 모든 경우를 출력
```python
from itertools import permutations

data = ['A', 'B', 'C']      # 데이터 춘비
result = list(permutations(data, 3))    # 모든 순열 구하기

print(result)
```
`[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]`

### combinations
- 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 **순서를 고려하지 않고** 나열하는 모든 경우(조합)를 계산해준다.
- combinations 는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용해야 한다.
- ex) 리스트 ['A', 'B', 'C']에서 2개(r = 2)를 뽑아 순서에 상관없이 나열하는 모든 경우를 출력
```python
from itertools import combinations

data = ['A', 'B', 'C']      # 데이터 춘비
result = list(combinations(data, 2))    # 2개를 뽑는 모든 조합 구하기

print(result)
```
`[('A', 'B'), ('A', 'C'), ('B', 'C')]`

### product
- permutations 와 같은 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다.
- 다만, **원소를 중복**하여 뽑는다.
- product 객체를 초기화 할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다.
- product 는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용해야 한다.
- ex) 리스트 ['A', 'B', 'C']에서 중복을 포함하여 2개(r = 2)를 뽑아 나열하는 모든 경우를 출력
```python
from itertools import product

data = ['A', 'B', 'C']      # 데이터 춘비
result = list(product(data, repeat=2))    # 2개를 뽑는 모든 순열 구하기(중복 허용)

print(result)
```
`[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]`

### combinations_with_replacement
- combinations 와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 **순서를 고려하지 않고** 나열하는 모든 경우(조합)을 계산한다.
- 다만, **원소를 중복**하여 뽑는다.
- combinations_with_replacement 는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환해서 사용해야 한다.
- ex) 리스트 ['A', 'B', 'C']에서 중복을 포함하여 2개(r = 2)를 뽑아 순서에 상관없이 나열하는 모든 경우를 출력
```python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']      # 데이터 춘비
result = list(combinations_with_replacement(data, 2))    # 2개를 뽑는 모든 조합 구하기(중복 허용)

print(result)
```
`[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]`


---


## 예시 : iterable의 원소로 순열과 조합을 구하는 방법

예시)

- 1,2,3의 숫자가 적힌 카드가 있을 때, 이 중 두 장을 꺼내는 경우의 수 -> 12, 13, 21, 23, 31, 32
- 'A', 'B', 'C'로 만들 수 있는 경우의 수 -> 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
---
다른 언어에서는..(또는 이 기능을 모르시는 사람은)   
보통 사람들은 for 문을 이용해 permutation 함수를 구현

```python
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result
```

파이썬에서는 [itertools.permutation](https://docs.python.org/3/library/itertools.html#itertools.permutations) 를 이용하면, for문을 사용하지 않고도 순열을 구할 수 있습니다.
```python
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
```


# Reference
- https://programmers.co.kr/learn/courses/4008/lessons/12836