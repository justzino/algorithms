# 브루트 포스(brute force)
- brute: 무식한, force: 힘   무식한 힘으로 해석할 수 있다.

완전탐색 알고리즘. 즉, 가능한 모든 경우의 수를 모두 탐색하면서 요구조건에 충족되는 결과만을 가져온다.

이 알고리즘의 강력한 점은 예외 없이 100%의 확률로 정답만을 출력한다.

- 일반적인 방법으로 문제를 해결하기 위해서는 모든 자료를 탐색해야 하기 때문에 특정한 구조를 전체적으로 탐색할 수 있는 방법을 필요로 한다.

- 알고리즘 설계의 가장 기본적인 접근 방법은 해가 존재할 것으로 예상되는 모든 영역을 전체 탐색하는 방법이다.

- **선형 구조**를 전체적으로 탐색하는 `순차 탐색`, **비선형 구조**를 전체적으로 탐색하는 `깊이 우선 탐색(DFS, Depth First
 Search)`과 `너비 우선 탐색(BFS, breadth first search)`이 가장 기본적인 도구이다.

- `너비 우선 탐색`은 `브루트 포스`와 관련이 깊고, `깊이 우선 탐색`은 다음에 작성될 `백트래킹`과 관련이 깊다.

### 문제해결 방법  
1. 문제를 선형 구조로 구조화한다.

2. 구조화된 문제공간을 적절한 방법으로 해를 구성할 때까지 탐색한다.

3. 구성된 해를 정리한다.
 
 
 
### 너비 우선 탐색(BFS, Breadth-first search)
- 그래프에서 완전탐색 방법 중 하나

- 탐색트리의 루트노드부터 목표노드를 만날 때까지 단계별로 횡방향으로 탐색을 진행해 나가는 방식

#### 장점
- 출발노드에서 목표노드까지의 최단 길이 경로를 보장한다.

#### 단점
- 경로가 매우 길 경우에는 탐색 가지가 급격히 증가함에 따라 보다 많은 기억 공간을 필요로 한다.

- 해가 존재하지 않는다면 유한(finite) 그래프의 경우에는 모든 그래프를 탐색한 후에 실패로 끝난다.

- 무한(infinite) 그래프의 경우에는 결코 해를 찾지도 못하고, 끝내지도 못한다.

즉, **'해가 하나 이상 존재한다'** 라는 가정을 세우고 모든 영역을 탐색한다.



## 순열과 조합
[출처](https://programmers.co.kr/learn/courses/4008/lessons/12836)
### 순열과 조합 - combinations, permutations
이번 강의에서는 iterable의 원소로 순열과 조합을 구하는 방법을 배워봅시다.

예시)

- 1,2,3의 숫자가 적힌 카드가 있을 때, 이 중 두 장을 꺼내는 경우의 수 -> 12, 13, 21, 23, 31, 32
- 'A', 'B', 'C'로 만들 수 있는 경우의 수 -> 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
---
다른 언어에서는..(또는 이 기능을 모르시는 분은)   
보통 사람들은 for 문을 이용해 permutation 함수를 구현합니다.

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