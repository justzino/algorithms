# 알고리즘 공부

#### 쉬운 것도 무시하지 말고 기본부터 다시 쌓아 올리자.

## 알고리즘 정리
### Python

<details markdown="1">
<summary><strong>🛠 입력 받기 </strong></summary>

### 입출력 속도 비교
`sys.stdin.readline > raw_input() > input()`

```python
n = int(input())
```
```python
import sys

n = int(sys.stdin.readline())   # 한 줄 입력 받을 때
# n = input()

a = [sys.stdin.readline() for i in range(n)]
```
```python
import sys

for line in sys.stdin:          # 여러줄 입력 받을 때
    a, b = map(int, line.split())
    print(a+b)
```
### 주의/참고 사항
1. 재귀함수가 있는 경우 재귀 깊이를 설정해야 한다. (python3 의 경우 사용가능 / pypy에서는 사용 불가)
2. ```python
   sys.setrecursionlimit(10**8) # 10^8 까지 늘림.
   ```
3. sys.stdin.readline을 사용할 때, 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 **.strip()**을 추가로 해 주는 것이 좋다.
4. sys.stdin.readline().split()의 split()은  공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누기 때문에 strip을 추가할 필요가 없다.(주로 숫자 다룰 때)


### Reference
- https://infinitt.tistory.com/26

</details>


<details markdown="1">
<summary><strong>🛠 예외 처리 </strong></summary>

### 1. 오류는 어떤 때 발생하는가?
#### 1. **FileNotFoundError** : 디렉터리 안에 없는 파일을 열려고 시도했을 때
    ```python
    >>> f = open("나없는파일", 'r')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'
    ```
#### 2. **ZeroDivisionError** : 0으로 다른 숫자를 나누는 경우
    ```python
    >>> 4 / 0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero
    ```
#### 3. **IndexError** : 리스트 범위에서 벗어난 경우
    ```python
    >>> a = [1,2,3]
    >>> a[4]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range
    ```

### 2. 오류 예외 처리 기법
#### 1. **try, except문**
    - 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행
    ```python
    try:
       ...
    except:
       ...
    ```
    - except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행
    ```python
    try:
       ...
    except 발생 오류:
       ...
    ```
    - 오류 메시지의 내용까지 알고 싶을 때 사용
    ```python
    try:
       ...
    except 발생 오류 as 오류 메시지 변수:
       ...
    ```
    ```python
    try:
       4 / 0
    except ZeroDivisionError as e:
       print(e)
    ```
    > 결과값: division by zero  
#### 2. **try .. finally**  
    try문에는 finally절을 사용할 수 있다. finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 
    보통 finally절은 사용한 리소스를 close해야 할 때에 많이 사용한다.
    ```python
    f = open('foo.txt', 'w')
    try:
        # 무언가를 수행
    finally:
        f.close()
    ```
#### 3. **여러개의 오류 처리하기**
    ```python
    try:
        ...
    except 발생 오류1:
       ... 
    except 발생 오류2:
       ...
    ```
    ex1)
    ```python
    try:
        a = [1,2]
        print(a[3])
        4/0
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except IndexError:
        print("인덱싱 할 수 없습니다.")
    ```
    ex2)
    ```python
    try:
        a = [1,2]
        print(a[3])
        4/0
    except ZeroDivisionError as e:
        print(e)
    except IndexError as e:
        print(e)
    ```
    > "list index out of range" 오류 메시지가 출력  

    ex3)
    ```python
    try:
        a = [1,2]
        print(a[3])
        4/0
    except (ZeroDivisionError, IndexError) as e:
        print(e)
    ```
   
### 3. 오류 회피하기
### 4. 오류 일부러 발생시키기
### 5. 예외 만들기

### Reference
- https://wikidocs.net/30#_1

</details>

<details markdown="1">
<summary><strong>🛠 진법 다루기 </strong></summary>

## 2진수, 8진수, 16진수 다루기
1373번  
2진수: 0b / 8진수: 0o / 16진수: 0x

#### 다른 진수의 형태로 숫자를 표현하기
```python
>>> 42 == 0b101010
True
>>> 42 == 0o52
True
>>> 42 == 0x2a
True
```
#### 숫자에서 다른 진수의 문자열로 변환하기 (int(10진법 숫자) ->  n진법 문자열)
```python
>>> bin(42)
'0b101010'
>>> oct(42)
'0o52'
>>> hex(42)
'0x2a'
```
#### 다른 진수의 문자열로 숫자형으로 변환하기 (문자열 -> n진법 숫자)
```python
>>> int('0b101010', 2)
42
>>> int('0o52', 8)
42
>>> int('0x2a', 16)
```
#### 추가
```python
>>> format(42, 'b')
'101010'
>>> format(42, 'o')
'52'
>>> format(42, 'x')
'2a'
>>> format(42, 'X')
'2A'
>>> format(42, 'd')
'42'
```

## 골드 바흐 문제
백준 6588, 17103번
- 속도 최적화에 대한 고민 필요
- 꼭 다시 풀어 볼 것!!!

## itertools 찾아보기

### Reference
- https://www.daleseo.com/python-int-bases/

</details>


<details markdown="1">
<summary><strong>🛠 자료 구조 </strong></summary>

### 시간 제한
- 리스트의 슬라이싱은 O(N)
- 삭제나 추가 연산이 모두 O(n)의 시간복잡도

### pass 와 comtinue 차이  
#### 1406번
- pass: 단순히 실행할 코드가 없다는 것을 의미
- continue: 다음 순번의 loop를 돌도록 강제


## deque
### 1158
이 문제는 deque를 쓰면 쉽게 풀 수 있을 것 같다는 생각이 들었다.  
글자를 <>사이는 queue 특성을 이용하여 popleft()로, 역순은 stack 특성을 이용하여 pop()시키면 될것 같다.  

[dequq 참고 사이트](https://statinknu.tistory.com/12)  
list를 사용해도 되지만 반복적인 pop, append가 등장하는 경우 deque를 사용해야 속도에서 이득을 볼 수 있다.
- In python docs I can see that deque is a special collection highly optimized for poping/adding items from left or right sides.  
- Source. Stack Overflow python: deque vs list performance comparison

### deque에 append와 extend, 원소 추가
```python
from collections import deque


dq =deque()
dq.append('right') #리스트 append와 같이 오른쪽에서부터 append deque(['left'])
dq.appendleft('left') # 왼쪽으로 append #deque(['left', 'right'])

#dq.extend('right') #extend이기 때문에 #deque(['left', 'right', 'r', 'i', 'g', 'h', 't'])
#원하는 결과를 얻고자 하면
dq.extend(['right']) #오른쪽으로 extend
dq.extendleft(['left']) #마찬가지로 왼쪽으로 extend
```

### deque의 pop와 remove, 원소 삭제
```python
from collections import deque


dq = deque()
dq.extend('python') #deque(['p','y','t','h','o','n'])

dq.pop() #'n'반환, deque(['p','y','t','h','o'])
dq.popleft() #'p'반환, deque(['y','t','h','o'])
dq.remove('t') #'t'를 찾아서 첫번째 t 항목 삭제

dq.clear() #모든 항목 삭제
```

### 그 외 deque의 중요한 기능
```python
dq = deque()
dq.extend('python') #deque(['p','y','t','h','o','n'])
dq.cnt('p') #1
dq.index('y') #1
#dq.reverse() #deque(['n', 'o', 'h', 't', 'y', 'p'])
dq2 = reversed(dq) 
# list(dq2) : ['n', 'o', 'h', 't', 'y', 'p']
# deque(dq2) : deque(['n', 'o', 'h', 't', 'y', 'p'])
len(dq) #'6'
dq[0] #'p'
dq[1:3] # error

dq.rotate(n=1) #default값은 1으로 왼쪽원소를 오른쪽으로 n씩 민다, 즉 길이만큼 밀면 제자리
```

```python
dq = deque([0]*3, maxlen = 3)

#maxlen을 설정해놓으면 일정길이를 넘어가지 못하기 때문에 자동으로 밀려나가게 된다.
#즉 1,2,3의 원소를 가진 deque의 maxlen이 3이라면 여기에 4를 오른쪽에서 append해주면
#deque의 1원소는 자동으로 pop되고 2,3,4 를 가지게 된다.
```

```python
# 덧붙여 deque는 slicing이 불가능한데, list로 만들어주면 할수 있다
dq = deque()
dq.extend('python')
dq[0:3] # error
list(dq)[0:3] # ['p', 'y', 't']
```

## collections 내장 모듈
파이썬 collections 내장 모듈에서는 많은것을 지원해준다. 추후에 공부, 정리 해보자.
- Counter 부터 deque, defaultdict 등등


## Reference
### about pythonic
[파이썬 클린코드 - 파이썬스러운 코드와 이를 기반으로 한 클린 코드를 짜는 것](https://dailyheumsi.tistory.com/221)  
> pythonic 코드 작성을 위한 참고 링크들  
> [파이썬을 파이썬 답게. (코딩 문제편)](https://dailyheumsi.tistory.com/31)  
> [파이썬 코드 스타일](https://python-guide-kr.readthedocs.io/ko/latest/writing/style.html)  
> [Pythonic code가 과연 효율적일까?](https://www.youtube.com/watch?v=Txz7K6Zc-_M&feature=youtu.be)  
> [책 - 파이썬답게 코딩하기](http://www.yes24.com/Product/Goods/60493752)  

[파이썬 주의사항 및 Tips - BOJ](https://deepwelloper.tistory.com/69)  
[파이썬 자료형 별 주요 연산자의 시간 복잡도 (Big-O)](https://wayhome25.github.io/python/2017/06/14/time-complexity/)    


### List Comprehension 에 대한 이해
[list comprehension에 대한 이해](https://shoark7.github.io/programming/python/about-list-comprehension-python)  


### dictionary 를 사용하는 여러가지 방식
1935, 1918번 참고

```python
num = {}

N = int(stdin.readline())
exp = list(stdin.readline().rstrip())
stack = []

for i in range(N):
    num[chr(65+i)] = int(stdin.readline())      # {'A' : 1}

for c in exp:
    if 64 < ord(c) < 91:
        stack.append(num[c])
```

```python
def priority(x):
    if x == "*" or x == "/":
        return 2
    elif x == "+" or x == "-":
        return 1
    elif x == "(" or x == ")":
        return 0

    return -1
```
```python
# 위의 방법을 dict를 이용하여 이렇게 choice_set으로 사용가능
priority = {
    '*': 2
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
}
```

## int 요소를 갖는 list -> 문자열 출력
```python
result = [1, 2, 3, 4]
print(' '.join(map(str, result)))       # 이게 밑에거보다 느림
print(' '.join([str(i) for i in result]))
```

## asterisk(*)
10808 번  
[asterisk list](https://mingrammer.com/understanding-the-asterisk-of-python/)
```python
print(' '.join(map(str, result)))
print(*result)
```


## 문자 함수
10820
```python
        if c.islower():         # 'a' <= c <= 'z'
            result[0] += 1
        elif c.isupper():       # 'A' <= c <= 'Z'
            result[1] += 1
        elif c.isdigit():       # '0' <= c <= '9' 
```


</details>

<details markdown="1">
<summary><strong>🛠 DP </strong></summary>

### 동적계획법(Dynamic Programmin, DP)
1. 어떤 문제를 DP로 풀기 위해서는 '최적의 원리' (Principle of Optimality) 가 성립하는지를 확인

2. 메모이제이션(Memoization)을 사용

### 메모이제이션
자꾸만 반복되지만 그 결과 값은 변하지 않는 작은 문제들의 결과값을 저장 하는 것.  

```python
# 백준 9095번
# a(n) = a(n-1) + a(n-2) + a(n-3)
T = int(input())

for _ in range(T):
    n = int(input())
    mem = [0, 1, 2, 4] + [0] * (n - 3)
    for i in range(4, n + 1):
        mem[i] = mem[i-1] + mem[i-2] + mem[i-3]
    print(mem[n])
```
### Reference

</details>


<details markdown="1">
<summary><strong>🛠 DFS - BFS </strong></summary>

### DFS

```python
# 1260 DFS 와 BFS
import sys
sys.setrecursionlimit(100000)

n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

def dfs(vertex):
    print(vertex, end=' ')
    visited[vertex] = True
    for edge in adj[vertex]:
        if not visited[edge]:
            dfs(edge)

visited = [False] * (n+1)
dfs(v)
```
### BFS
```python
# 1260 DFS 와 BFS
from collections import deque

n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

def bfs(vertex):
    q = deque([vertex])
    while q:
        vertex = q.popleft()
        if not visited[vertex]:
            visited[vertex] = True
            print(vertex, end=' ')
            for edge in adj[vertex]:
                if not visited[edge]:
                    q.append(edge)

visited = [False] * (n+1)
bfs(v)
```

</details>


<details markdown="1">
<summary><strong>🛠 Dijkstra </strong></summary>

```python
import heapq
import sys


input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기.
n, e = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

# 모든 간선 정보를 입력받기
for _ in range(e):
    a, b, c = map(int, input().split())
    # a번 노드에서 c번으로 가는 비용이 b이다. b를 기준으로 heap sorting 됨
    graph[a].append((b, c))


# Heap sort 사용 = O(e * log v)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:    # 큐가 비어있지 않다면
        # 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# 모든 노드를 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우
    if distance[i] == INF:
        print('unreached')
    else:
        print(distance[i])
```



</details>

## 📅 푼 문제 기록 (아직 업데이트 중...)

|                 |                                   1                                   |                                  2                                   |                                   3                                   |                                  4                                  |                                  5                                  |
| :-------------: | :-------------------------------------------------------------------: | :------------------------------------------------------------------: | :-------------------------------------------------------------------: | :-----------------------------------------------------------------: | :-----------------------------------------------------------------: |
|     입출력      |          [Hello World](https://www.acmicpc.net/problem/2557)          |             [A+B](https://www.acmicpc.net/problem/1000)              |            [A+B - 2](https://www.acmicpc.net/problem/2558)            |          [A+B - 3](https://www.acmicpc.net/problem/10950)           |          [A+B - 4](https://www.acmicpc.net/problem/10951)           |
|                 |           [A+B - 5](https://www.acmicpc.net/problem/10952)            |           [A+B - 6](https://www.acmicpc.net/problem/10953)           |           [A+B - 7](https://www.acmicpc.net/problem/11021)            |          [A+B - 8](https://www.acmicpc.net/problem/11022)           |      [그대로 출력하기](https://www.acmicpc.net/problem/11718)       |
|                 |      [그대로 출력하기 2](https://www.acmicpc.net/problem/11719)       |          [숫자의 합](https://www.acmicpc.net/problem/11720)          |    [열 개씩 끊어 출력하기](https://www.acmicpc.net/problem/11721)     |           [N 찍기](https://www.acmicpc.net/problem/2741)            |           [기찍 N](https://www.acmicpc.net/problem/2742)            |
|                 |            [구구단](https://www.acmicpc.net/problem/2739)             |            [2007년](https://www.acmicpc.net/problem/1924)            |              [합](https://www.acmicpc.net/problem/8393)               |         [최소, 최대](https://www.acmicpc.net/problem/10818)         |         [별 찍기 - 1](https://www.acmicpc.net/problem/2438)         |
|                 |          [별 찍기 - 2](https://www.acmicpc.net/problem/2439)          |         [별 찍기 - 3](https://www.acmicpc.net/problem/2440)          |          [별 찍기 - 4](https://www.acmicpc.net/problem/2441)          |         [별 찍기 - 5](https://www.acmicpc.net/problem/2442)         |         [별 찍기 - 8](https://www.acmicpc.net/problem/2445)         |
|                 |          [별 찍기 - 9](https://www.acmicpc.net/problem/2522)          |         [별 찍기 - 12](https://www.acmicpc.net/problem/2446)         |         [별 찍기 - 16](https://www.acmicpc.net/problem/10991)         |        [별 찍기 - 17](https://www.acmicpc.net/problem/10992)        |
|                 |
|    자료구조     |             [스택](https://www.acmicpc.net/problem/10828)             |         [단어 뒤집기](https://www.acmicpc.net/problem/9093)          |             [괄호](https://www.acmicpc.net/problem/9012)              |          [스택 수열](https://www.acmicpc.net/problem/1874)          |           [에디터](https://www.acmicpc.net/problem/1406)            |
|                 |              [큐](https://www.acmicpc.net/problem/10845)              |        [조세퍼스 문제](https://www.acmicpc.net/problem/1158)         |              [덱](https://www.acmicpc.net/problem/10866)              |       [단어 뒤집기 2](https://www.acmicpc.net/problem/17413)        |          [쇠막대기](https://www.acmicpc.net/problem/10799)          |
|                 |            [오큰수](https://www.acmicpc.net/problem/17298)            |          [오등큰수](https://www.acmicpc.net/problem/17299)           |         [후위 표기식2](https://www.acmicpc.net/problem/1935)          |         [후위 표기식](https://www.acmicpc.net/problem/1918)         |        [알파벳 개수](https://www.acmicpc.net/problem/10808)         |
|                 |         [알파벳 찾기](https://www.acmicpc.net/problem/10809)          |         [문자열 분석](https://www.acmicpc.net/problem/10820)         |        [단어 길이 재기](https://www.acmicpc.net/problem/2743)         |           [ROT13](https://www.acmicpc.net/problem/11655)            |           [네 수](https://www.acmicpc.net/problem/10824)            |
|                 |         [접미사 배열](https://www.acmicpc.net/problem/11656)          |
|                 |
|      수학       |            [나머지](https://www.acmicpc.net/problem/10430)            |   [최대공약수와 최소공배수](https://www.acmicpc.net/problem/2609)    |          [최소공배수](https://www.acmicpc.net/problem/1934)           |          [소수 찾기](https://www.acmicpc.net/problem/1978)          |         [소수 구하기](https://www.acmicpc.net/problem/1929)         |
|                 |        [골드바흐의 추측](https://www.acmicpc.net/problem/6588)        |          [팩토리얼](https://www.acmicpc.net/problem/10872)           |       [팩토리얼 0의 개수](https://www.acmicpc.net/problem/1676)       |        [조합 0의 개수](https://www.acmicpc.net/problem/2004)        |           [GCD 합](https://www.acmicpc.net/problem/9613)            |
|                 |          [숨바꼭질 6](https://www.acmicpc.net/problem/17087)          |         [2진수 8진수](https://www.acmicpc.net/problem/1373)          |          [8진수 2진수](https://www.acmicpc.net/problem/1212)          |            [2진수](https://www.acmicpc.net/problem/2089)            |      [골드바흐 파티션](https://www.acmicpc.net/problem/17103)       |
|                 |         [진법 변환 2](https://www.acmicpc.net/problem/11005)          |          [진법 변환](https://www.acmicpc.net/problem/2745)           |       [Base Conversion](https://www.acmicpc.net/problem/11576)        |         [소인수분해](https://www.acmicpc.net/problem/11653)         |
|                 |
|       DP        |          [1로 만들기](https://www.acmicpc.net/problem/1463)           |         [2×n 타일링](https://www.acmicpc.net/problem/11726)          |         [2×n 타일링 2](https://www.acmicpc.net/problem/11727)         |       [1, 2, 3 더하기](https://www.acmicpc.net/problem/9095)        |       [카드 구매하기](https://www.acmicpc.net/problem/11052)        |
|                 |       [카드 구매하기 2](https://www.acmicpc.net/problem/16194)        |      [1, 2, 3 더하기 5](https://www.acmicpc.net/problem/15990)       |         [쉬운 계단 수](https://www.acmicpc.net/problem/10844)         |           [이친수](https://www.acmicpc.net/problem/2193)            | [가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053) |
|                 | [가장 긴 증가하는 부분 수열 4](https://www.acmicpc.net/problem/14002) |            [연속합](https://www.acmicpc.net/problem/1912)            |          [제곱수의 합](https://www.acmicpc.net/problem/1699)          |           [합분해](https://www.acmicpc.net/problem/2225)            |      [1, 2, 3 더하기 3](https://www.acmicpc.net/problem/15988)      |
|                 |            [RGB거리](https://www.acmicpc.net/problem/1149)            |            [동물원](https://www.acmicpc.net/problem/1309)            |          [오르막 수](https://www.acmicpc.net/problem/11057)           |           [스티커](https://www.acmicpc.net/problem/9465)            |         [포도주 시식](https://www.acmicpc.net/problem/2156)         |
|                 |          [정수 삼각형](https://www.acmicpc.net/problem/1932)          |   [가장 큰 증가 부분 수열](https://www.acmicpc.net/problem/11055)    |  [가장 긴 감소하는 부분 수열](https://www.acmicpc.net/problem/11722)  | [가장 긴 바이토닉 부분 수열](https://www.acmicpc.net/problem/11054) |          [연속합 2](https://www.acmicpc.net/problem/13398)          |
|                 |          [타일 채우기](https://www.acmicpc.net/problem/2133)          |            [동물원](https://www.acmicpc.net/problem/1309)            |          [RGB거리 2](https://www.acmicpc.net/problem/17404)           |           [합분해](https://www.acmicpc.net/problem/2225)            |
|                 |
|   브루트 포스   |          [일곱 난쟁이](https://www.acmicpc.net/problem/2309)          |          [사탕 게임](https://www.acmicpc.net/problem/3085)           |           [날짜 계산](https://www.acmicpc.net/problem/1476)           |         [N과 M (1)](https://www.acmicpc.net/problem/15649)          |         [N과 M (2)](https://www.acmicpc.net/problem/15650)          |
|                 |          [N과 M (3)](https://www.acmicpc.net/problem/15651)           |          [N과 M (4)](https://www.acmicpc.net/problem/15652)          |          [N과 M (5)](https://www.acmicpc.net/problem/15654)           |         [N과 M (6)](https://www.acmicpc.net/problem/15655)          |         [N과 M (7)](https://www.acmicpc.net/problem/15656)          |
|                 |          [N과 M (8)](https://www.acmicpc.net/problem/15657)           |          [N과 M (9)](https://www.acmicpc.net/problem/15663)          |          [N과 M (10)](https://www.acmicpc.net/problem/15664)          |         [N과 M (11)](https://www.acmicpc.net/problem/15665)         |         [N과 M (12)](https://www.acmicpc.net/problem/15666)         |
|                 |          [다음 순열](https://www.acmicpc.net/problem/10972)           |          [이전 순열](https://www.acmicpc.net/problem/10973)          |          [모든 순열](https://www.acmicpc.net/problem/10974)           |
|                 |
| Graph(DFS/BFS)  |           [DFS와 BFS](https://www.acmicpc.net/problem/1260)           |           [숨바꼭질](https://www.acmicpc.net/problem/1697)           |           [바이러스](https://www.acmicpc.net/problem/2606)            |         [유기농 배추](https://www.acmicpc.net/problem/1012)         |        [효율적인 해킹](https://www.acmicpc.net/problem/1325)        |
|                 | [타겟 넘버](https://programmers.co.kr/learn/courses/30/lessons/43165) | [네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162) | [단어 변환](https://programmers.co.kr/learn/courses/30/lessons/43163) |
| Graph(Dijkstra) |             [해킹](https://www.acmicpc.net/problem/10282)             |
|     Greedy      |              [배](https://www.acmicpc.net/problem/1092)               |
|     Search      |

---

## 💻 문제집 목록

<details markdown="1">
<summary><strong>📄 입 / 출력 </strong></summary>

| 문제 번호 |         제목          |                  URL                  |
| :-------: | :-------------------: | :-----------------------------------: |
|   2557    |      Hello World      | https://www.acmicpc.net/problem/2557  |
|   1000    |          A+B          | https://www.acmicpc.net/problem/1000  |
|   2558    |        A+B - 2        | https://www.acmicpc.net/problem/2558  |
|   10950   |        A+B - 3        | https://www.acmicpc.net/problem/10950 |
|   10951   |        A+B - 4        | https://www.acmicpc.net/problem/10951 |
|   10952   |        A+B - 5        | https://www.acmicpc.net/problem/10952 |
|   10953   |        A+B - 6        | https://www.acmicpc.net/problem/10953 |
|   11021   |        A+B - 7        | https://www.acmicpc.net/problem/11021 |
|   11022   |        A+B - 8        | https://www.acmicpc.net/problem/11022 |
|   11718   |    그대로 출력하기    | https://www.acmicpc.net/problem/11718 |
|   11719   |   그대로 출력하기 2   | https://www.acmicpc.net/problem/11719 |
|   11720   |       숫자의 합       | https://www.acmicpc.net/problem/11720 |
|   11721   | 열 개씩 끊어 출력하기 | https://www.acmicpc.net/problem/11721 |
|   2741    |        N 찍기         | https://www.acmicpc.net/problem/2741  |
|   2742    |        기찍 N         | https://www.acmicpc.net/problem/2742  |
|   2739    |        구구단         | https://www.acmicpc.net/problem/2739  |
|   1924    |        2007년         | https://www.acmicpc.net/problem/1924  |
|   8393    |          합           | https://www.acmicpc.net/problem/8393  |
|   10818   |      최소, 최대       | https://www.acmicpc.net/problem/10818 |
|   2438    |      별 찍기 - 1      | https://www.acmicpc.net/problem/2438  |
|   2439    |      별 찍기 - 2      | https://www.acmicpc.net/problem/2439  |
|   2440    |      별 찍기 - 3      | https://www.acmicpc.net/problem/2440  |
|   2441    |      별 찍기 - 4      | https://www.acmicpc.net/problem/2441  |
|   2442    |      별 찍기 - 5      | https://www.acmicpc.net/problem/2442  |
|   2445    |      별 찍기 - 8      | https://www.acmicpc.net/problem/2445  |
|   2446    |      별 찍기 - 9      | https://www.acmicpc.net/problem/2446  |
|   2522    |     별 찍기 - 12      | https://www.acmicpc.net/problem/2522  |
|   10991   |     별 찍기 - 16      | https://www.acmicpc.net/problem/10991 |
|   10992   |     별 찍기 - 17      | https://www.acmicpc.net/problem/10992 |

---

</details>
<details markdown="1">
<summary><strong>📄 백준 Code Plus 알고리즘 기초 1/2 </strong></summary>

#### 📄 자료구조 1

| 문제 번호 |      제목      |                  URL                  |
| :-------: | :------------: | :-----------------------------------: |
|   10828   |      스택      | https://www.acmicpc.net/problem/10828 |
|   9093    |  단어 뒤집기   | https://www.acmicpc.net/problem/9093  |
|   9012    |      괄호      | https://www.acmicpc.net/problem/9012  |
|   1874    |   스택 수열    | https://www.acmicpc.net/problem/1874  |
|   1406    |     에디터     | https://www.acmicpc.net/problem/1406  |
|   10845   |       큐       | https://www.acmicpc.net/problem/10845 |
|   1158    | 조세퍼스 문제  | https://www.acmicpc.net/problem/1158  |
|   10866   |       덱       | https://www.acmicpc.net/problem/10866 |
|   17413   | 단어 뒤집기 2  | https://www.acmicpc.net/problem/17413 |
|   10799   |    쇠막대기    | https://www.acmicpc.net/problem/10799 |
|   17298   |     오큰수     | https://www.acmicpc.net/problem/17298 |
|   17299   |    오등큰수    | https://www.acmicpc.net/problem/17299 |
|   1935    |  후위 표기식2  | https://www.acmicpc.net/problem/1935  |
|   1918    |  후위 표기식   | https://www.acmicpc.net/problem/1918  |
|   10808   |  알파벳 개수   | https://www.acmicpc.net/problem/10808 |
|   10809   |  알파벳 찾기   | https://www.acmicpc.net/problem/10809 |
|   10820   |  문자열 분석   | https://www.acmicpc.net/problem/10820 |
|   2743    | 단어 길이 재기 | https://www.acmicpc.net/problem/2743  |
|   11655   |     ROT13      | https://www.acmicpc.net/problem/11655 |
|   10824   |     네 수      | https://www.acmicpc.net/problem/10824 |
|   11656   |  접미사 배열   | https://www.acmicpc.net/problem/11656 |

---

#### 📄 수학 1

| 문제 번호 |          제목           |                  URL                  |
| :-------: | :---------------------: | :-----------------------------------: |
|   10430   |         나머지          | https://www.acmicpc.net/problem/10430 |
|   2609    | 최대공약수와 최소공배수 | https://www.acmicpc.net/problem/2609  |
|   1934    |       최소공배수        | https://www.acmicpc.net/problem/1934  |
|   1978    |        소수 찾기        | https://www.acmicpc.net/problem/1978  |
|   1929    |       소수 구하기       | https://www.acmicpc.net/problem/1929  |
|   6588    |     골드바흐의 추측     | https://www.acmicpc.net/problem/6588  |
|   10872   |        팩토리얼         | https://www.acmicpc.net/problem/10872 |
|   1676    |    팩토리얼 0의 개수    | https://www.acmicpc.net/problem/1676  |
|   2004    |      조합 0의 개수      | https://www.acmicpc.net/problem/2004  |
|   9613    |         GCD 합          | https://www.acmicpc.net/problem/9613  |
|   17087   |       숨바꼭질 6        | https://www.acmicpc.net/problem/17087 |
|   1373    |       2진수 8진수       | https://www.acmicpc.net/problem/1373  |
|   1212    |       8진수 2진수       | https://www.acmicpc.net/problem/1212  |
|   2089    |         -2진수          | https://www.acmicpc.net/problem/2089  |
|   17103   |     골드바흐 파티션     | https://www.acmicpc.net/problem/17103 |
|   11005   |       진법 변환 2       | https://www.acmicpc.net/problem/11005 |
|   2745    |        진법 변환        | https://www.acmicpc.net/problem/2745  |
|   11576   |     Base Conversion     | https://www.acmicpc.net/problem/11576 |
|   11653   |       소인수분해        | https://www.acmicpc.net/problem/11653 |

---

#### 📄 DP 1

| 문제 번호 |             제목             |                  URL                  |
| :-------: | :--------------------------: | :-----------------------------------: |
|   2557    |          1로 만들기          | https://www.acmicpc.net/problem/1463  |
|   1463    |          2×n 타일링          | https://www.acmicpc.net/problem/11726 |
|   11726   |         2×n 타일링 2         | https://www.acmicpc.net/problem/11727 |
|   11727   |        1, 2, 3 더하기        | https://www.acmicpc.net/problem/9095  |
|   9095    |        카드 구매하기         | https://www.acmicpc.net/problem/11052 |
|   11052   |       카드 구매하기 2        | https://www.acmicpc.net/problem/16194 |
|   16194   |       1, 2, 3 더하기 5       | https://www.acmicpc.net/problem/15990 |
|   15990   |         쉬운 계단 수         | https://www.acmicpc.net/problem/10844 |
|   10844   |            이친수            | https://www.acmicpc.net/problem/2193  |
|   2193    |  가장 긴 증가하는 부분 수열  | https://www.acmicpc.net/problem/11053 |
|   11053   | 가장 긴 증가하는 부분 수열 4 | https://www.acmicpc.net/problem/14002 |
|   14002   |            연속합            | https://www.acmicpc.net/problem/1912  |
|   1912    |         제곱수의 합          | https://www.acmicpc.net/problem/1699  |
|   1699    |            합분해            | https://www.acmicpc.net/problem/2225  |
|   2225    |       1, 2, 3 더하기 3       | https://www.acmicpc.net/problem/15988 |
|   15988   |           RGB거리            | https://www.acmicpc.net/problem/1149  |
|   1149    |            동물원            | https://www.acmicpc.net/problem/1309  |
|   1309    |          오르막 수           | https://www.acmicpc.net/problem/11057 |
|   11057   |            스티커            | https://www.acmicpc.net/problem/9465  |
|   9465    |         포도주 시식          | https://www.acmicpc.net/problem/2156  |
|   2156    |         정수 삼각형          | https://www.acmicpc.net/problem/1932  |
|   1932    |    가장 큰 증가 부분 수열    | https://www.acmicpc.net/problem/11055 |
|   11055   |  가장 긴 감소하는 부분 수열  | https://www.acmicpc.net/problem/11722 |
|   11722   |  가장 긴 바이토닉 부분 수열  | https://www.acmicpc.net/problem/11054 |
|   11054   |           연속합 2           | https://www.acmicpc.net/problem/13398 |
|   13398   |         타일 채우기          | https://www.acmicpc.net/problem/2133  |
|   2133    |            동물원            | https://www.acmicpc.net/problem/1309  |
|   1309    |          RGB거리 2           | https://www.acmicpc.net/problem/17404 |
|   17404   |            합분해            | https://www.acmicpc.net/problem/2225  |

---

#### 📄 Brute Force

| 문제 번호 |      제목      |                  URL                  |
| :-------: | :------------: | :-----------------------------------: |
|   2309    |  일곱 난쟁이   | https://www.acmicpc.net/problem/2309  |
|   3085    |   사탕 게임    | https://www.acmicpc.net/problem/3085  |
|   1476    |   날짜 계산    | https://www.acmicpc.net/problem/1476  |
|   1107    |     리모컨     | https://www.acmicpc.net/problem/1107  |
|   14500   |   테트로미노   | https://www.acmicpc.net/problem/14500 |
|   6064    |   카잉 달력    | https://www.acmicpc.net/problem/6064  |
|   1748    | 수 이어 쓰기 1 | https://www.acmicpc.net/problem/1748  |
|   9095    | 1, 2, 3 더하기 | https://www.acmicpc.net/problem/9095  |
|   15649   |   N과 M (1)    | https://www.acmicpc.net/problem/15649 |
|   15650   |   N과 M (2)    | https://www.acmicpc.net/problem/15650 |
|   15651   |   N과 M (3)    | https://www.acmicpc.net/problem/15651 |
|   15652   |   N과 M (4)    | https://www.acmicpc.net/problem/15652 |
|   15654   |   N과 M (5)    | https://www.acmicpc.net/problem/15654 |
|   15655   |   N과 M (6)    | https://www.acmicpc.net/problem/15655 |
|   15656   |   N과 M (7)    | https://www.acmicpc.net/problem/15656 |
|   15657   |   N과 M (8)    | https://www.acmicpc.net/problem/15657 |
|   15663   |   N과 M (9)    | https://www.acmicpc.net/problem/15663 |
|   15664   |   N과 M (10)   | https://www.acmicpc.net/problem/15664 |
|   15665   |   N과 M (11)   | https://www.acmicpc.net/problem/15665 |
|   15666   |   N과 M (12)   | https://www.acmicpc.net/problem/15666 |
|   10972   |   다음 순열    | https://www.acmicpc.net/problem/10972 |
|   10973   |   이전 순열    | https://www.acmicpc.net/problem/10973 |
|   10974   |   모든 순열    | https://www.acmicpc.net/problem/10974 |
|   10819   | 차이를 최대로  | https://www.acmicpc.net/problem/10819 |
|   10971   | 외판원 순회 2  | https://www.acmicpc.net/problem/10971 |
|   6603    |      로또      | https://www.acmicpc.net/problem/6603  |
|   9095    | 1, 2, 3 더하기 | https://www.acmicpc.net/problem/9095  |
|   1759    |  암호 만들기   | https://www.acmicpc.net/problem/1759  |
|   14501   |      퇴사      | https://www.acmicpc.net/problem/14501 |
|   14889   | 스타트와 링크  | https://www.acmicpc.net/problem/14889 |
|   15661   | 링크와 스타트  | https://www.acmicpc.net/problem/15661 |
|   2529    |     부등호     | https://www.acmicpc.net/problem/2529  |
|   1248    |     맞춰봐     | https://www.acmicpc.net/problem/1248  |
|   11723   |      집합      | https://www.acmicpc.net/problem/11723 |
|   1182    | 부분수열의 합  | https://www.acmicpc.net/problem/1182  |
|   14889   | 스타트와 링크  | https://www.acmicpc.net/problem/14889 |
|   14391   |   종이 조각    | https://www.acmicpc.net/problem/14391 |

---

</details>

<details markdown="1">
<summary><strong>📄 삼성 SW 역량 테스트 기출 문제</strong></summary>

| 문제 번호 |           제목           |                  URL                  |
| :-------: | :----------------------: | :-----------------------------------: |
|   13460   |       구슬 탈출 2        | https://www.acmicpc.net/problem/13460 |
|   12100   |        2048(Easy         | https://www.acmicpc.net/problem/12100 |
|   3190    |            뱀            | https://www.acmicpc.net/problem/3190  |
|   13458   |        시험 감독         | https://www.acmicpc.net/problem/13458 |
|   14499   |      주사위 굴리기       | https://www.acmicpc.net/problem/14499 |
|   14500   |        테트로미노        | https://www.acmicpc.net/problem/14500 |
|   14501   |           퇴사           | https://www.acmicpc.net/problem/14501 |
|   14502   |          연구소          | https://www.acmicpc.net/problem/14502 |
|   14503   |       로봇 청소기        | https://www.acmicpc.net/problem/14503 |
|   14888   |     연산자 끼워넣기      | https://www.acmicpc.net/problem/14888 |
|   14889   |      스타트와 링크       | https://www.acmicpc.net/problem/14889 |
|   14890   |          경사로          | https://www.acmicpc.net/problem/14890 |
|   14891   |         톱니바퀴         | https://www.acmicpc.net/problem/14891 |
|   15683   |           감시           | https://www.acmicpc.net/problem/15683 |
|   15684   |       사다리 조작        | https://www.acmicpc.net/problem/15684 |
|   15685   |       드래곤 커브        | https://www.acmicpc.net/problem/15685 |
|   15686   |        치킨 배달         | https://www.acmicpc.net/problem/15686 |
|   5373    |           큐빙           | https://www.acmicpc.net/problem/5373  |
|   16234   |        인구 이동         | https://www.acmicpc.net/problem/16234 |
|   16235   |       나무 재테크        | https://www.acmicpc.net/problem/16235 |
|   16236   |        아기 상어         | https://www.acmicpc.net/problem/16236 |
|   17144   |      미세먼지 안녕!      | https://www.acmicpc.net/problem/17144 |
|   17143   |          낚시왕          | https://www.acmicpc.net/problem/17143 |
|   17140   |    이차원 배열과 연산    | https://www.acmicpc.net/problem/17140 |
|   17142   |         연구소 3         | https://www.acmicpc.net/problem/17142 |
|   17779   |       게리맨더링 2       | https://www.acmicpc.net/problem/17779 |
|   17837   |      새로운 게임 2       | https://www.acmicpc.net/problem/17837 |
|   17822   |       원판 돌리기        | https://www.acmicpc.net/problem/17822 |
|   17825   |      주사위 윷놀이       | https://www.acmicpc.net/problem/17825 |
|   19235   |      모노미노도미노      | https://www.acmicpc.net/problem/19235 |
|   20061   |     모노미노도미노 2     | https://www.acmicpc.net/problem/20061 |
|   19236   |       청소년 상어        | https://www.acmicpc.net/problem/19236 |
|   19237   |        어른 상어         | https://www.acmicpc.net/problem/19237 |
|   19238   |       스타트 택시        | https://www.acmicpc.net/problem/19238 |
|   20055   | 컨베이어 벨트 위의 로봇  | https://www.acmicpc.net/problem/20055 |
|   20056   |  마법사 상어와 파이어볼  | https://www.acmicpc.net/problem/20056 |
|   20057   |  마법사 상어와 토네이도  | https://www.acmicpc.net/problem/20057 |
|   20058   | 마법사 상어와 파이어스톰 | https://www.acmicpc.net/problem/20058 |

---

</details>

<details markdown="1">
<summary><strong>📄 SW Expert Academy 모의 SW 역량테스트 </strong></summary>

| 문제 번호 |         제목         |                                              URL                                              |
| :-------: | :------------------: | :-------------------------------------------------------------------------------------------: |
|   1949    |     등산로 조성      | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq |
|   1953    |     탈주범 검거      | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq |
|   2105    |     디저트 카페      | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu |
|   2112    |      보호 필름       | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu |
|   2117    |    홈 방범 서비스    | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu |
|   2382    |     미생물 격리      | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl |
|   2383    |    점심 식사시간     | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl |
|   4013    |     특이한 자석      | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH |
|   4014    |     활주로 건설      | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH |
|   5644    |      무선 충전       | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo |
|   5648    | 원자 소멸 시뮬레이션 | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo |
|   5650    |      핀볼 게임       | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo |
|   5653    |     줄기세포배양     | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo |
|   5656    |      벽돌 깨기       | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo |
|   5658    |  보물상자 비밀번호   | https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo |

---

</details>

<details markdown="1">
<summary><strong>📄 프로그래머스</strong></summary>

|     제목      |                           URL                            |
| :-----------: | :------------------------------------------------------: |
|  가장 큰 수   | https://programmers.co.kr/learn/courses/30/lessons/42746 |
|     카펫      | https://programmers.co.kr/learn/courses/30/lessons/42842 |
|   조이스틱    | https://programmers.co.kr/learn/courses/30/lessons/42860 |
|   숫자야구    | https://programmers.co.kr/learn/courses/30/lessons/42841 |
|   타겟 넘버   | https://programmers.co.kr/learn/courses/30/lessons/43165 |
|  N으로 표현   | https://programmers.co.kr/learn/courses/30/lessons/42895 |
|  타일 장식물  | https://programmers.co.kr/learn/courses/30/lessons/43104 |
| 전화번호 목록 | https://programmers.co.kr/learn/courses/30/lessons/42577 |
|   네트워크    | https://programmers.co.kr/learn/courses/30/lessons/43162 |
|     위장      | https://programmers.co.kr/learn/courses/30/lessons/42578 |
|   단어변환    | https://programmers.co.kr/learn/courses/30/lessons/43163 |
|      탑       | https://programmers.co.kr/learn/courses/30/lessons/42588 |
|    H-Index    | https://programmers.co.kr/learn/courses/30/lessons/42747 |
|   입국 심사   | https://programmers.co.kr/learn/courses/30/lessons/43238 |
|     예산      | https://programmers.co.kr/learn/courses/30/lessons/43237 |

---

</details>

<details markdown="1">
<summary><strong>📄 2021 KAKAO BLIND RECRUITMENT (프로그래머스)</strong></summary>

|       문제       | 레벨 |                           URL                            |
| :--------------: | :--: | :------------------------------------------------------: |
| 신규 아이디 추천 |  1   | https://programmers.co.kr/learn/courses/30/lessons/72410 |
|   메뉴 리뉴얼    |  2   | https://programmers.co.kr/learn/courses/30/lessons/72411 |
|    순위 검색     |  2   | https://programmers.co.kr/learn/courses/30/lessons/72412 |
|  합승 택시 요금  |  3   | https://programmers.co.kr/learn/courses/30/lessons/72413 |
|    광고 삽입     |  3   | https://programmers.co.kr/learn/courses/30/lessons/72414 |
|  카드 짝 맞추기  |  3   | https://programmers.co.kr/learn/courses/30/lessons/72415 |
| 매출 하락 최소화 |  4   | https://programmers.co.kr/learn/courses/30/lessons/72416 |

---

</details>

<details markdown="1">
<summary><strong>📄 2020 KAKAO BLIND RECRUITMENT (프로그래머스)</strong></summary>

|      문제      | 레벨 |                           URL                            |
| :------------: | :--: | :------------------------------------------------------: |
|  문자열 압축   |  2   | https://programmers.co.kr/learn/courses/30/lessons/60057 |
|   괄호 변환    |  2   | https://programmers.co.kr/learn/courses/30/lessons/60058 |
| 자물쇠와 열쇠  |  3   | https://programmers.co.kr/learn/courses/30/lessons/60059 |
| 기둥과 보 설치 |  3   | https://programmers.co.kr/learn/courses/30/lessons/60061 |
|   외벽 점검    |  3   | https://programmers.co.kr/learn/courses/30/lessons/60062 |
| 블록 이동하기  |  3   | https://programmers.co.kr/learn/courses/30/lessons/60063 |
|   가사 검색    |  4   | https://programmers.co.kr/learn/courses/30/lessons/60060 |

---

</details>

<details markdown="1">
<summary><strong>📄 2020 카카오 인턴십 (프로그래머스)</strong></summary>

|     문제      | 레벨 |                           URL                            |
| :-----------: | :--: | :------------------------------------------------------: |
| 키패드 누르기 |  1   | https://programmers.co.kr/learn/courses/30/lessons/67256 |
|  수식 최대화  |  2   | https://programmers.co.kr/learn/courses/30/lessons/67257 |
|   보석 쇼핑   |  3   | https://programmers.co.kr/learn/courses/30/lessons/67258 |
|  경주로 건설  |  3   | https://programmers.co.kr/learn/courses/30/lessons/67259 |
|   동굴 탐험   |  4   | https://programmers.co.kr/learn/courses/30/lessons/67260 |

---

</details>

<details markdown="1">
<summary><strong>📄 2019 KAKAO BLIND RECRUITMENT (프로그래머스)</strong></summary>

|        문제        | 레벨 |                           URL                            |
| :----------------: | :--: | :------------------------------------------------------: |
|       실패율       |  1   | https://programmers.co.kr/learn/courses/30/lessons/42889 |
|     오픈채팅방     |  2   | https://programmers.co.kr/learn/courses/30/lessons/42888 |
|       후보키       |  2   | https://programmers.co.kr/learn/courses/30/lessons/42890 |
|    길 찾기 게임    |  3   | https://programmers.co.kr/learn/courses/30/lessons/42892 |
|     매칭 점수      |  3   | https://programmers.co.kr/learn/courses/30/lessons/42893 |
| 무지의 먹방 라이브 |  4   | https://programmers.co.kr/learn/courses/30/lessons/42891 |
|     블록 게임      |  4   | https://programmers.co.kr/learn/courses/30/lessons/42894 |

---

</details>

<details markdown="1">
<summary><strong>📄 2019 카카오 개발자 겨울 인턴십 문제 (프로그래머스)</strong></summary>

|         문제         | 레벨 |                           URL                            |
| :------------------: | :--: | :------------------------------------------------------: |
| 크레인 인형뽑기 게임 |  1   | https://programmers.co.kr/learn/courses/30/lessons/64061 |
|         튜플         |  2   | https://programmers.co.kr/learn/courses/30/lessons/64065 |
|     불량 사용자      |  3   | https://programmers.co.kr/learn/courses/30/lessons/64064 |
|     호텔 방 배정     |  3   | https://programmers.co.kr/learn/courses/30/lessons/64063 |
|   징검다리 건너기    |  4   | https://programmers.co.kr/learn/courses/30/lessons/64062 |

---

</details>

<details markdown="1">
<summary><strong>📄 2018 KAKAO BLIND RECRUITMENT (프로그래머스)</strong></summary>

|         문제          | 레벨 |                           URL                            |
| :-------------------: | :--: | :------------------------------------------------------: |
|    [1차] 비밀지도     |  1   | https://programmers.co.kr/learn/courses/30/lessons/17681 |
|    [1차] 다트 게임    |  1   | https://programmers.co.kr/learn/courses/30/lessons/17682 |
| [1차] 뉴스 클러스터링 |  2   | https://programmers.co.kr/learn/courses/30/lessons/17677 |
|   [1차] 프렌즈4블록   |  2   | https://programmers.co.kr/learn/courses/30/lessons/17679 |
|      [1차] 캐시       |  2   | https://programmers.co.kr/learn/courses/30/lessons/17680 |
|    [3차] 방금그곡     |  2   | https://programmers.co.kr/learn/courses/30/lessons/17683 |
|      [3차] 압축       |  2   | https://programmers.co.kr/learn/courses/30/lessons/17684 |
|   [3차] 파일명 정렬   |  2   | https://programmers.co.kr/learn/courses/30/lessons/17686 |
|   [3차] n진수 게임    |  2   | https://programmers.co.kr/learn/courses/30/lessons/17687 |
|   [1차] 추석 트래픽   |  3   | https://programmers.co.kr/learn/courses/30/lessons/17676 |
|    [1차] 셔틀버스     |  3   | https://programmers.co.kr/learn/courses/30/lessons/17678 |
|    [3차] 자동완성     |  4   | https://programmers.co.kr/learn/courses/30/lessons/17685 |

---

</details>

<details markdown="1">
<summary><strong>📄 카카오 코드 페스티벌 2018 예선</strong></summary>

| 문제 번호 |   제목    |               URL                |
| :-------: | :-------: | :------------------------------: |
|   15953   | 상금 헌터 | http://acmicpc.net/problem/15953 |
|   15954   |  인형들   | http://acmicpc.net/problem/15954 |

---

</details>

<details markdown="1">
<summary><strong>📄 카카오 코드 페스티벌 2018</strong></summary>

| 문제 번호 |    제목    |               URL                |
| :-------: | :--------: | :------------------------------: |
|   15997   | 승부 예측  | http://acmicpc.net/problem/15997 |
|   15998   | 카카오머니 | http://acmicpc.net/problem/15998 |

---

</details>

## Reference

- https://github.com/CodeTest-StudyGroup/Code-Test-Study.git
- [백준](https://code.plus/course/41)
- [블로그](https://plzrun.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4PS-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0)
