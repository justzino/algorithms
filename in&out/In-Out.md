# 🛠 입력 받기
## 입출력 속도 비교
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
## 주의/참고 사항
1. 재귀함수가 있는 경우 재귀 깊이를 설정해야 한다. (python3 의 경우 사용가능 / pypy에서는 사용 불가)
2. ```python
   sys.setrecursionlimit(10**8)     # 10^8 까지 늘림.
   ```
3. sys.stdin.readline을 사용할 때, 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 **.strip()**을 추가로 해 주는 것이 좋다.
4. sys.stdin.readline().split()의 split()은  공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누기 때문에 strip을 추가할 필요가 없다.(주로 숫자 다룰 때)


## Reference
- https://infinitt.tistory.com/26