# Maximum Recursion depth

- 파이썬에서는 재귀를 무한정 허용해서 벌어질 문제들을 고려하여 재귀호출을 1000번으로 제한하고있다.  
- 1000번이상을 호출하면 다음과 같은 에러가 발생한다.

`=> RecursionError: maximum recursion depth exceeded while calling a Python object`
- 따라서, 재귀함수가 있는 경우 재귀 깊이를 설정해야 한다. (python3 의 경우 사용가능 / pypy에서는 사용 불가)
```python
import sys

sys.setrecursionlimit(10**8)     # 10^8 까지 늘림.
  ```
