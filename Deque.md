### Deque

- push/pop 연산이 빈번한 알고리즘에서 list 보다 월등한 속도

```python
from collections import deque

deq = deque([0, 1, 2, 3, 4, 5])
```

|<b>        method          |                      Return                    |          Example      |
| :------------------------:| :--------------------------------------------: | :----------------------------: |
|<b> deque.append(item)     | item을 deque의 오른쪽 끝에 삽입                   | <div style="text-align: left"> <b> deq.append(7) </b> <br> -> deque([0, 1, 2, 3, 4, 5, 7])|
|<b> deque.appendleft(item) | item을 deque의 왼쪽 끝에 삽입                     | <div style="text-align: left"> <b> deq.appendleft(7) </b> <br> -> deque([7, 0, 1, 2, 3, 4, 5]) |
|<b> deque.pop()            | 오른쪽 끝 원소를 반환하는 동시에 삭제                | <div style="text-align: left"> <b> deq.pop() </b> <br> -> return 5 <br> -> deque([0, 1, 2, 3, 4]) |
|<b> deque.popleft()        | 왼쪽 끝 원소를 반환하는 동시에 삭제                  | <div style="text-align: left"> <b> deq.popleft() </b> <br> -> return 0 <br> -> deque([1, 2, 3, 4, 5]) |
|<b> deque.extend(array)    | 주어진 배열(array)을 순환하면서 deque의 오른쪽에 추가 | <div style="text-align: left"> array = [11, 12, 13] <br> <b> deq.extend(array) </b> <br> -> deque([0, 1, 2, 3, 4, 5, 11, 12, 13]) |
|<b> deque.extendleft(array)| 주어진 배열(array)을 순환하면서 deque의 왼쪽에 추가   | <div style="text-align: left"> array = [11, 12, 13] <br> <b> deq.extendleft(array) </b> <br> -> deque([13, 12, 11, 0, 1, 2, 3, 4, 5]) |
|<b> deque.remove(item)     | item을 데크에서 찾아 삭제                          | <div style="text-align: left"> <b> deq.remove(4) </b> <br> -> deque([0, 1, 2, 3, 5]) |
|<b> deque.reverse()        | deque의 데이터를 뒤집음                           | <div style="text-align: left"> <b> deq.reverse() </b> <br> -> deque([5, 4, 3, 2, 1, 0]) |
|<b> deque.rotate(num)      | deque를 num만큼 회전한다 <br> (양수면 오른쪽, 음수면 왼쪽)  | <div style="text-align: left"> <b> deq.rotate(1) </b> <br> -> deque([5, 0, 1, 2, 3, 4]) <br> <b> deq.rotate(-1) </b> <br> -> deque([1, 2, 3, 4, 5, 0]) <br> <b> deq.rotate(2) </b> <br> -> deque([4, 5, 0, 1, 2, 3]) |
