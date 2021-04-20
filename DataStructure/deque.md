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