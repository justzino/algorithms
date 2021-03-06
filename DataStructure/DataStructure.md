# ๐  ์๋ฃ ๊ตฌ์กฐ

## [์๊ฐ ๋ณต์ก๋](Time-Complexity.md)

## pass ์ continue ์ฐจ์ด  
### 1406๋ฒ
- pass: ๋จ์ํ ์คํํ  ์ฝ๋๊ฐ ์๋ค๋ ๊ฒ์ ์๋ฏธ
- continue: ๋ค์ ์๋ฒ์ loop๋ฅผ ๋๋๋ก ๊ฐ์ 

## [deque](deque.md)

## dictionary
### zip์ ํ์ฉํ์ฌ ๋์๋๋ฆฌ ๋ง๋๋ ๋ฐฉ๋ฒ
my_dict1 = dict(zip(['one', 'two', 'three'], [1,2,3]))

### dictionary ๋ฅผ ์ฌ์ฉํ๋ ์ฌ๋ฌ๊ฐ์ง ๋ฐฉ์
1935, 1918๋ฒ ์ฐธ๊ณ 

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
# ์์ ๋ฐฉ๋ฒ์ dict๋ฅผ ์ด์ฉํ์ฌ ์ด๋ ๊ฒ choice_set์ผ๋ก ์ฌ์ฉ๊ฐ๋ฅ
priority = {
    '*': 2
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
}
```

## int ์์๋ฅผ ๊ฐ๋ list๋ฅผ ๋ฌธ์์ด๋ก ์ถ๋ ฅ
```python
result = [1, 2, 3, 4]
print(' '.join(map(str, result)))       # ์ด๊ฒ ๋ฐ์๊ฑฐ๋ณด๋ค ๋๋ฆผ
print(' '.join([str(i) for i in result]))
```

## asterisk(*)
10808 ๋ฒ
[asterisk list](https://mingrammer.com/understanding-the-asterisk-of-python/)
```python
print(' '.join(map(str, result)))
print(*result)
```

## ๋ฌธ์ ํจ์
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
[ํ์ด์ฌ ํด๋ฆฐ์ฝ๋ - ํ์ด์ฌ์ค๋ฌ์ด ์ฝ๋์ ์ด๋ฅผ ๊ธฐ๋ฐ์ผ๋ก ํ ํด๋ฆฐ ์ฝ๋๋ฅผ ์ง๋ ๊ฒ](https://dailyheumsi.tistory.com/221)  
> pythonic ์ฝ๋ ์์ฑ์ ์ํ ์ฐธ๊ณ  ๋งํฌ๋ค  
> [ํ์ด์ฌ์ ํ์ด์ฌ ๋ต๊ฒ. (์ฝ๋ฉ ๋ฌธ์ ํธ)](https://dailyheumsi.tistory.com/31)  
> [ํ์ด์ฌ ์ฝ๋ ์คํ์ผ](https://python-guide-kr.readthedocs.io/ko/latest/writing/style.html)  
> [Pythonic code๊ฐ ๊ณผ์ฐ ํจ์จ์ ์ผ๊น?](https://www.youtube.com/watch?v=Txz7K6Zc-_M&feature=youtu.be)  
> [์ฑ - ํ์ด์ฌ๋ต๊ฒ ์ฝ๋ฉํ๊ธฐ](http://www.yes24.com/Product/Goods/60493752)  

[ํ์ด์ฌ ์ฃผ์์ฌํญ ๋ฐ Tips - BOJ](https://deepwelloper.tistory.com/69)  
[ํ์ด์ฌ ์๋ฃํ ๋ณ ์ฃผ์ ์ฐ์ฐ์์ ์๊ฐ ๋ณต์ก๋ (Big-O)](https://wayhome25.github.io/python/2017/06/14/time-complexity/)    


### List Comprehension ์ ๋ํ ์ดํด
[list comprehension์ ๋ํ ์ดํด](https://shoark7.github.io/programming/python/about-list-comprehension-python)  