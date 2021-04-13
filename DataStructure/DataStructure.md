# 🛠 자료 구조
## 시간 제한
- 리스트의 슬라이싱은 O(N)
- 삭제나 추가 연산이 모두 O(n)의 시간복잡도


## pass 와 comtinue 차이  
### 1406번
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
(asterisk list)[https://mingrammer.com/understanding-the-asterisk-of-python/]
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
