## 순열과 조합 (permutations, combinations)

### iterable의 원소로 순열과 조합을 구하는 방법

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

파이썬에서는
[itertools.permutation](https://docs.python.org/3/library/itertools.html#itertools.permutations) 를 이용하면, for문을 사용하지 않고도 순열을 구할 수 있습니다.
```python
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
```
※ 조합은 [itertools.combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations) 를 사용해서 구할 수 있습니다. 사용법은 permutations와 비슷해요!

# Reference
- https://programmers.co.kr/learn/courses/4008/lessons/12836