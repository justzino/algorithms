# 🛠 자료 구조

## [시간 복잡도](Time-Complexity.md)

## pass 와 continue 차이  
### 1406번
- pass: 단순히 실행할 코드가 없다는 것을 의미
- continue: 다음 순번의 loop를 돌도록 강제

## [deque](deque.md)

## dictionary 를 사용하는 여러가지 방식
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

## int 요소를 갖는 list를 문자열로 출력
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