# 알고리즘 공부

#### 쉬운 것도 무시하지 말고 기본부터 다시 쌓아 올리자.

## String 정리

#### 진법 및 아스키코드 변환

|     method     |            Return type : 설명             |                    Ex                    |
| :------------: | :------------------------------------- : | :--------------------------------------: |
|     chr()      |   string : 숫자(아스키 코드) → 문자 변환     |       chr(65) = 'A', chr(97) = 'a'       |
|     ord()      |       int : 문자 → 숫자(아스키 코드)        |       ord('A') = 65, ord('a') = 97       |
| int(num, base) | int : n진법으로 표기된 문자열 → 10진법 숫자   |           int('3212', 5) = 432           |
|     bin()      |        string : 2진수 문자열로 변환         | bin(10) = '0b1010', bin(0o12) = '0b1010' |
|     oct()      |        string : 8진수 문자열로 변환         |   oct(10) = '0o12', oct(0xa) = '0o12'    |
|     hex()      |        string : 16진수 문자열로 변환        |    hex(10) = '0xa', hex(0o12) = '0xa'    |

#### string Method

|                     Method                     |                        Return type : 설명 (대 소문자 구분)                        |                                                                              Ex                                                                               |
| :--------------------------------------------: | :-------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                    len(str)                    |                                int : 문자열의 길이                                |                                                            str = 'Hello World' <br> len(str) -> 11                                                            |
|                  str.split()                   |                     list : 문자열을 기준에 따라 나누어 return                     |                                                  str = 'Hello World' <br> str.split() -> ['Hello', 'World']                                                   |
|                  str.strip()                   |           string : 문자열의 양쪽 끝에 해당 문자가 있으면 지운 후 return           |                                                          str = '.abc.' <br> str.strip('.') -> 'abc'                                                           |
|                   str.join()                   |            string : string을 list파라미터의 중간에 넣어 합친후 return             |                          a = ['Hello', 'World'] <br> ' '.join(a) -> 'Hello World' <br> str = 'abc' <br> str.join('123') -> 1abc2abc3                          |
|                 str.replace()                  | string : 문자열의 특정 부분을 바꾸어 return <br> 특정 부분이 없다면 그대로 return |                                           str = 'Hello World' <br> str.replace('World', 'Python') -> 'Hello Python'                                           |
|        str.find(문자열, 찾기시작할위치)        |         int/-1 : 매개변수로 입력한 문자열의 index return 없으면 return -1         |                               str = 'aa bb aa bb' <br> str.find('bb') -> 3 <br> str.find('bb', 4) -> 9 <br> str.find('h') -> -1                               |
|                  str.index()                   |             int/ValueError : find와 동일하나 없으면 return ValueError             |                                     str = 'abc가나다123' <br> str.index('가나다') -> 4 <br> str.index('d') -> ValueError                                      |
|        str.startswith(문자열, 시작지점)        |           bool : 매개변수로 문자열이 시작하면 True, 그렇지 않으면 False           |                   str = 'aabbaa' <br> str.startswith('aa') -> True <br> str.startswith('AA') -> False <br> str.startswith('aa', 4) -> True                    |
| str.endswith(문자열, 문자열의시작, 문자열의끝) |            bool : 매개변수로 문자열이 끝나면 True, 그렇지 않으면 False            |                                      str = 'World' <br> str.endswith('l') -> False <br> str.endswith('l', 0, 4) -> True                                       |
|                  str.count()                   |                        int : 매개변수의 문자열 개수 return                        |                                   str = 'Hello' <br> str.count('l') -> 2 <br> str.count('ll') -> 1 <br> str.count('x') -> 0                                   |
|                 str.isalpha()                  |           bool : 문자열이 영어, 한글로만 이루어졌으면 True 아니면 False           |                               str = 'abc가나다' <br> str.isalpha() -> True <br> str = 'abc 가나다' <br> str.isalpha() -> False                                |
|                 str.isdigit()                  |              bool : 문자열이 숫자로만 이루어졌으면 True 아니면 False              |                                      str = '123' <br> str.isdigit() -> True <br> str = '1 23'<br> str.isdigit() -> False                                      |
|                 str.isalnum()                  |        bool : 문자열이 영어, 한글, 숫자로만 이루어졌으면 True 아니면 False        |                              str = 'abc가나다123' <br> str.isalnum() -> True <br> str = 'ab 가나 12' <br> str.isalnum() -> False                              |
|                 str.islower()                  |      bool : 문자열 중 알파벳이 모두 소문자로만 되어졌으면 True 아니면 False       | str = 'abc 123 가나다' <br> str.islower() -> True <br> str = 'Abc 123 가나다' <br> str.islower() -> False <br> str = '123 가나다' <br> str.islower() -> False |
|                 str.isupper()                  |      bool : 문자열 중 알파벳이 모두 대문자로만 되어졌으면 True 아니면 False       | str = 'ABC 123 가나다' <br> str.isupper() -> True <br> str = 'aBC 123 가나다' <br> str.isupper() -> False <br> str = '123 가나다' <br> str.isupper() -> False |
|                  str.lower()                   |                       string : 문자열을 모두 소문자로 변환                        |                                                  str = 'Abc 123 가나다' <br> str.lower() -> 'abc 123 가나다'                                                  |
|                  str.upper()                   |                       string : 문자열을 모두 대문자로 변환                        |                                                  str = 'Abc 123 가나다' <br> str.upper() -> 'ABC 123 가나다'                                                  |
|                   str[::-1]                    |                             string : 문자열을 뒤집기                              |                                                              str = 'abc' <br> str[::-1] -> 'cba'                                                              |
|                str.capitalize()                |                string : 문자열의 첫 글자를 대문자로 바꾸어 return                 |                                                  str = 'hello world' <br> str.capitalize() -> 'Hello world'                                                   |
|                  str.title()                   |           string : 문자열에서 알파벳의 첫 글자를 대문자로 바꾸어 return           |                                                 str = 'hello wo세상rld' <br> str.title() -> 'Hello Wo세상Rld'                                                 |
|          str.rjust(문자열 길이, 문자)          |          string : 오른쪽 정렬, 문자열 왼쪽에 입력한 문자로 채워서 return          |                                                         str = 'abc' <br> str.rjust(5, '#') -> '##abc'                                                         |
|          str.ljust(문자열 길이, 문자)          |          string : 왼쪽 정렬, 문자열 오른쪽에 입력한 문자로 채워서 return          |                                                         str = 'abc' <br> str.ljust(5, '#') -> 'abc##'                                                         |
|             str.zfill(문자열 길이)             |                        string : 0으로 왼쪽을 채워서 return                        |                                                           str = 'abc' <br> str.zfill(5) -> '00abc'                                                            |


## [정규표현식 정리](Regular-Expression.py)

|  정규 표현식   | 동일 표현식 |                의미                | 예시                 |
| :------------: | :---------: | :--------------------------------: | -------------------- |
|       -        |             |        두 문자 사이의 범위         |                      |
|       ^        |             |                not                 |                      |
|    [a-zA-Z]    |             |            알파벳 모두             |                      |
|     [0-9]      |     \d      |                숫자                |                      |
|     [^0-9]     |     \D      |          숫자가 아닌 문자          |                      |
| [ \t\n\r\f\v]  |     \s      |          whitespace 문자           |                      |
| [^ \t\n\r\f\v] |     \S      |    whitespace 문자가 아닌 문자     |                      |
|  [a-zA-Z0-9_]  |     \w      |             문자+숫자              |                      |
| [^a-za-z0-9_]  |     \W      |       문자+숫자가 아닌 문자        |                      |
|       .        |             |       \n을 제외한 모든 문자        |                      |
|      a.b       |             |       "a" + "모든문자" + "b"       | "aab", "a0b", "abc"  |
|     a[.]b      |             |               "a.b"                |                      |
|       \*       |    {0,}     |           0번 이상 반복            |                      |
|       +        |    {1,}     |           1번 이상 반복            |                      |
|     ca\*t      |   ca{0,}t   |      "c" + "a 0개 이상" + "t"      | "ct", "cat", "caaat" |
|      ca+t      |   ca{1,}t   |      "c" + "a 1개 이상" + "t"      | "cat", "caaat"       |
|      {m}       |             |          반드시 m번 반복           |                      |
|     {m, n}     |             |            m ~ n번 반복            |                      |
|       ?        |   {0, 1}    |         1번 있거나 없거나          |                      |
|     ca{2}t     |             |          "c" + "aa" + "t"          | "caat"               |
|    ca{2,5}t    |             |    "c" + "a(2~5회 반복)" + "t"     | "caat", "caaaaat"    |
|      ab?c      |             | "a" + "b(1번 있거나 없거나)" + "c" | "ac", "abc"          |

### 정규표현식을 이용한 문자열 검색
```python
import re
p = re.compile('ab*')
```
|     Method | 목적                                                                    |
| ---------: | ----------------------------------------------------------------------- |
|    match() | 문자열의 처음부터 정규식과 매치되는지 조사한다.                         |
|   search() | 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.                    |
|  findall() | 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.           |
| finditer() | 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다. |

## 자료구조 정리

### [List]

### [Deque](Deque.md)
- push/pop 연산이 빈번한 알고리즘에서 list 보다 월등한 속도
- [deque 문제](DataStructure/deque.md)

### [Dictionary](DataStructure/DataStructure.md#dictionary-%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EC%97%AC%EB%9F%AC%EA%B0%80%EC%A7%80-%EB%B0%A9%EC%8B%9D)
- [dictionary, list 문자열로 출력, asterisk(*)](DataStructure/DataStructure.md)   


## 알고리즘 정리

- [✅ 입력 받기](in&out/In-Out.md)  
- [✅ 예외 처리](in&out/Exception.md)   
- [✅ 진법 다루기](math/Numeral-System.md)
- [✅ 시간 복잡도](DataStructure/Time-Complexity.md)
- [✅ 재귀 함수 depth](in&out/Recursion.md)
   
- ✅ 구현하기
  - [좌표 및 방향 구현 예시1 - dx, dy로](This-is-Coding-Test-Book/Implementation/4-1.py)  
  - [좌표 및 방향 구현 예시2 - 저장된 step 으로](This-is-Coding-Test-Book/Implementation/4-3-2.py)  
  - [시:분:초 안에 특정 숫자 있는지 판독](This-is-Coding-Test-Book/Implementation/4-2.py)
  - [행렬 회전](This-is-Coding-Test-Book/Implementation/Rotate-a-Matrix.py)

- ✅ 파이썬 주요 라이브러리
  - [eval()](This-is-Coding-Test-Book/Python-Libraries.md#eval) - 문자열 형식의 수학 수식 계산값 반환
  - [sorted()](This-is-Coding-Test-Book/Python-Libraries.md#sorted) - iterable 객체 정렬값 반환
  - [itertools](This-is-Coding-Test-Book/Python-Libraries.md#itertools) - 순열, 조합 등 반복 데이터 처리 라이브러리
  - [itertools](math/Permutation-Combination.md) - 추가 설명
  - [heapq](This-is-Coding-Test-Book/Python-Libraries.md#heapq) - 힙 (우선순위 큐)
  - [bisect](This-is-Coding-Test-Book/Python-Libraries.md#bisect) - 이진 탐색, insort()
  - [collections](This-is-Coding-Test-Book/Python-Libraries.md#collections) - deque, Counter, defaultdict
  - [math](This-is-Coding-Test-Book/Python-Libraries.md#math)  - 팩토리얼, 제곱근, 최대공약수(GCD), pi
  - [zip](zip.md) - 여러 iterable 의 각 객체를 모아 tuple 로
  
- ✅ BFS, DFS
  - [인접 행렬 & 리스트 (Adjacent Matrix & List)](This-is-Coding-Test-Book/DFS-BFS/Adjacency.py)  
  - [BFS](This-is-Coding-Test-Book/DFS-BFS/BFS.py)  
  - [DFS](This-is-Coding-Test-Book/DFS-BFS/DFS.py)  
  - [DFS & BFS 예시](DFS-BFS/1260.py)  
  
- ✅ Sorting
  - [Bubble Sort](This-is-Coding-Test-Book/Sorting/Bubble-Sort.py)
  - [Selection Sort](This-is-Coding-Test-Book/Sorting/Selection-Sort.py)
  - [Insertion Sort](This-is-Coding-Test-Book/Sorting/Insertion-Sort.py)
  - [Quick Sort](This-is-Coding-Test-Book/Sorting/Quick-Sort.py)
  - [Quick Sort - 전통 방식](This-is-Coding-Test-Book/Sorting/Quick-Sort1.py)
  - [Quick Sort - Python 최적화](This-is-Coding-Test-Book/Sorting/Quick-Sort2.py)
  - [Quick Sort, Heap Sort, Count Sort, 정렬 라이브러리](This-is-Coding-Test-Book/Sorting/Sorting.md)
  
- ✅ 이진 탐색 (Binary Search)
  - [이진 탐색 - 라이브러리](This-is-Coding-Test-Book/Python-Libraries.md#bisect)
  - [이진 탐색 - 재귀 (Binary Search)](This-is-Coding-Test-Book/Search/Binary-Search1.py)  
  - [이진 탐색 - 반복문 (Binary Search)](This-is-Coding-Test-Book/Search/Binary-Search2.py)  
    
- [✅ DP](DP/README.md)

- [✅ Shortest Path](This-is-Coding-Test-Book/Shortest-Path/Shortest-Path.md)
  - [Dijkstra - 우선순위 큐 사용: O(E logV)](This-is-Coding-Test-Book/Shortest-Path/Dijkstra1.py)
  - [Dijkstra - 선형 탐색 사용 : O(V^2)](This-is-Coding-Test-Book/Shortest-Path/Dijkstra2.py)
  - [플로이드 워셜 - 모든점 -> 모든 점 : O(V^3) ](This-is-Coding-Test-Book/Shortest-Path/Floyd-Warshall.py)

- [✅ Graph](This-is-Coding-Test-Book/Graph/Graph.md)  
  - [인접 행렬 & 인접 리스트](This-is-Coding-Test-Book/DFS-BFS/Adjacency.py)
  - 서로소 집합 자료구조 (Disjoint Sets)
    - [구현 코드2 - 경로 압축 기법](This-is-Coding-Test-Book/Graph/Disjoint-Set2.py) (구현코드 1보다 중요!!) - 약 O(V + M logV)
    - [구현 코드1](This-is-Coding-Test-Book/Graph/Disjoint-Set1.py) - O(VM)
  - [서로소 집합을 활용한 사이클 판별](This-is-Coding-Test-Book/Graph/Cycle-Judge.py)
  - [MST: Kruskal 알고리즘](This-is-Coding-Test-Book/Graph/Kruskal.py)
  - [위상 정렬(Topology Sort)](This-is-Coding-Test-Book/Graph/Topology-Sort.py)

---
## 📅 푼 문제 기록 

<details markdown="1">
<summary> 푼 문제 목록 (업데이트 안함..) </summary>

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

</details>

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
- https://wikidocs.net/4308
- [백준](https://code.plus/course/41)
- [블로그](https://plzrun.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4PS-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0)
