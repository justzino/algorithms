# 표준 라이브러리

## 내장함수
### eval()
- eval() 함수는 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.  
```python
result = eval("(3 + 5) * 7")
print(result)
```
`56`

### sorted()
- iterable 객체가 들어왔을 떄, 정렬된 결과를 반환
- key 속성으로 정렬 기준 명시
- reverse 속성으로 정렬된 결과 리스트를 뒤집을지 여부
```python
result = sorted([9, 1, 8, 5, 4])        # 오름차순 정렬
print(result)
result = sorted([9, 1, 8, 5, 4], reverse=True)        # 내림차순 정렬
print(result)
```
`[1, 4, 5, 8, 9]`  
`[9, 8, 5, 4, 1]`

- 리스트의 원소로 리스트나 튜플이 존재할 때, 특정한 기준에 따라서 정렬을 수행할 수 있다. (key 속성)
```python
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse=True)
print(result)
```
`[('이순신', 75), ('아무개', 50), ('홍길동', 35)]`
- list 와 같은 iterable 객체는 기본적으로 sort() 함수를 내장하고 있어서 sorted() 사용할 필요 없다.
- 이 경우 list 객체의 내부 값이 정렬된 값으로 바로 변경 된다.
```python
data = [9, 1, 8, 5, 4]
data.sort()
print(data)
```
`[1, 4, 5, 8, 9]`

---

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

## heapq
- 다익스트라 최단 경로 알고리즘을 포함한, 다양한 알고리즘에서 **우선순위 큐 기능을 구현할 때 사용**.
- PriorityQueue 라이브러리를 사용할 수 있지만, 코테 환경에서는 보통 heapq가 더 빠르다.
- 파이썬의 힙은 **최소 힙(Min Heap)** 으로 구성되어 있다.
- 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
- `heapq.heappush()`
- `heapq.heappop()`
- ex) Heap Sort 를 heapq 로 구현
```python
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
```
`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`


- 파이썬에서는 최대 힙(Max Heap)을 제공하지 않는다.
- Max Heap을 구현 해야할 때는 원소의 부호를 임시로 변경하는 방식 사용
- ex) Max Heap을 통한, 내림차순 힙 정렬
```python
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
```
`[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]`

---

## bisect

### bisect_left, bisect_right
- 이진 탐색을 쉽게 구현하기 위한 라이브러리
- '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.
- `bisect_left(a, x)`: 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- `bisect_right(a, x)`: 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
- ex) 정렬된 리스트 [1, 2, 4, 4, 8]이 있을 때, 새로 데이터 4를 삽입할 인덱스
```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
```
`2`   
`4`
- `bisect_left()`함수와 `bisect_right()`함수는 '정렬된 리스트'에서 
  '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때, 효과적으로 사용
- ex) 값이 [left_value, right_value]인 데이터의 개수를 반환
- 즉 값이 left_value <= x <= right_value인 원소의 개술를 O(logN)으로 빠르게 계산 가능
```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
```
`2`   
`6`

### insort
bisect.insort 는 정렬될 수 있는 위치에 해당 항목을 삽입한다.
```python
from bisect import insort 

a = [60, 70, 80, 90]
insort(a, 85)
print(a)
```
`[60, 70, 80, 85, 90]`


---

## collections
### deque
- 큐를 구현할 때 사용
- 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능은 사용할 수 없음
- 연속적으로 나열된 데이터의 시작, 끝부분에 데이터를 삽입, 삭제시 매우 효과적(O(1))
```python
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))   # 리스트 자료형으로 변환
```
`deque([1, 2, 3, 4, 5])`  
`[1, 2, 3, 4, 5]`

### Counter
- 등장 횟수를 세는 기능 제공
- iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 등장한 횟수를 dict 형태로 반환
- 원소별 등장 횟수를 세는 기능이 필요할 때 사용
```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter)
print(dict(counter))        # 사전 자료형으로 변환
print(counter['blue'])      # 'blue'가 등장한 횟수 출력
print(counter['green'])     # 'green'이 등장한 횟수 출력
```
`Counter({'blue': 3, 'red': 2, 'green': 1})`
`{'red': 2, 'blue': 3, 'green': 1}`  
`3`  
`1`  

### defaultdict
- dictionary 를 사용하다 보면 어떤 키(key)에 대한 값(value)이 없는 경우에 대한 처리를 해야하는 경우가 자주 발생한다.
- 이런 경우 defaultdict를 사용하여 dict 의 default 값을 설정할 수 있다.

#### dictionary 의 value 로 list 사용
```python
from collections import defaultdict

a = [(100, 'b'), (40, 'f', ), (100, 'a'), (80, 'e'), (100, 'c'), (60, 'g'), (40, 'h'), (80, 'd')]

result = defaultdict(list)
for key, value in a:
    result[key].append(value)

print(result)
```
`defaultdict(<class 'list'>, {100: ['b', 'a', 'c'], 40: ['f', 'h'], 80: ['e', 'd'], 60: ['g']})`

---

## math
- 팩토리얼, 제곱근, 최대공약수(GCD) 등
### factorial()
```python
import math

print(math.factorial(5))    # 5 팩토리얼을 출력
```
`120`

### sqrt()
- x의 제곱근
```python
import math

print(math.sqrt(7))     # 7의 제곱근을 출력
```
`2.6457513110645907`

### gcd
- 최대 공약수
```python
import math

print(math.gcd(21, 14))
```
`7`  

### 파이(pi), e(자연 상수)
```python
import math

print(math.pi)  # 파이(pi) 출력
print(math.e)   # 자연상수 3출력
```
`3.141592653589793`  
`2.718281828459045`
