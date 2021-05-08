### Deque

```python
from collections import deque

deq = deque([0, 1, 2, 3, 4, 5])
```

|         method        |                      Return                   |          Example      |
| :--------------------:| :-------------------------------------------: | :----------------------------: |
|deque.append(item)     | item을 deque의 오른쪽 끝에 삽입                   | deq.append(7) <br> -> deque([0, 1, 2, 3, 4, 5, 7])|
|deque.appendleft(item) | item을 deque의 왼쪽 끝에 삽입                     | deq.appendleft(7) <br> -> deque([7, 0, 1, 2, 3, 4, 5]) |
|deque.pop()            | 오른쪽 끝 원소를 반환하는 동시에 삭제                | deq.pop() <br> -> return 5 <br> -> deque([0, 1, 2, 3, 4]) |
|deque.popleft()        | 왼쪽 끝 원소를 반환하는 동시에 삭제                  | deq.popleft() <br> -> return 0 <br> -> deque([1, 2, 3, 4, 5]) |
|deque.extend(array)    | 주어진 배열(array)을 순환하면서 deque의 오른쪽에 추가 | array = [11, 12, 13] <br> deq.extend(array) <br> -> deque([0, 1, 2, 3, 4, 5, 11, 12, 13])
|deque.extendleft(array)| 주어진 배열(array)을 순환하면서 deque의 왼쪽에 추가   | array = [11, 12, 13] <br> deq.extendleft(array) <br> -> deque([13, 12, 11, 0, 1, 2, 3, 4, 5])
|deque.remove(item)     | item을 데크에서 찾아 삭제                          | deq.remove(4) <br> -> deque([0, 1, 2, 3, 5])
|deque.rotate(num)      | deque를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽)  | deq.rotate(1) <br> -> deque([5, 0, 1, 2, 3, 4]) <br> deq.rotate(-1) <br> -> deque([1, 2, 3, 4, 5, 0]) <br> deq.rotate(2) <br> -> deque([4, 5, 0, 1, 2, 3])

- push/pop 연산이 빈번한 알고리즘