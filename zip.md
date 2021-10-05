# zip(*iterables)

- (길이가 같은) iterables 의 요소들을 모으는 이터레이터를 만듭니다.
- return 튜플의 이터레이터
- i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함합니다.
-  묶어주는 함수

## zip() 의 활용

### 1. 기본형 (행렬 transpose)
case 1.
```python
x = [1, 2, 3]
y = [4, 5, 6]
 
result = zip(x, y)
print(list(result))
```
`[(1, 4), (2, 5), (3, 6)]`

case 2.
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
result = []
for each in zip(*matrix):
    result.append(list(each))
print(result)
```
`[[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]`

case 3. enumerate() 와 함께 사용: idx 를 사용하면서 transpose 해야하는 경우
```python
scores = [
    [1, 6, 11, 16, 21],
    [2, 7, 12, 17, 22],
    [3, 8, 13, 18, 23],
    [4, 9, 14, 19, 24],
    [5, 10, 15, 20, 25]
]
results = []
for i, each in enumerate(zip(*scores)):
    each = list(each)
    each.sort()
    print(i, ': ', each)
```
```
0 :  [1, 2, 3, 4, 5]
1 :  [6, 7, 8, 9, 10]
2 :  [11, 12, 13, 14, 15]
3 :  [16, 17, 18, 19, 20]
4 :  [21, 22, 23, 24, 25]
```

### 2. zip을 활용하여 딕셔너리 쉽게 만드는 방법
```python
my_dict1 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
```

### 3. Dictionary 에서 value 기준 최소, 최대값 구하기

```python
tmp = {'database': 5, 'network': 3, 'os': 1, 'security': 2}
 
min_tmp = min(zip(tmp.values(), tmp.keys()))
max_tmp = max(zip(tmp.values(), tmp.keys()))
print(min_tmp)
print(max_tmp)
```
```
(1, 'os')
(5, 'database')
```
 
### 4. Dictionary 를 value 기준으로 정렬하기
방법 1.
```python
tmp = {'database': 5, 'network': 3, 'os': 1, 'security': 2}

tmp_sorted = sorted(zip(tmp.values(), tmp.keys()))
print(tmp_sorted)
```
```
[(1, 'os'), (2, 'security'), (3, 'network'), (5, 'database')]
```
방법 2.
```python
tmp = {'database': 5, 'network': 3, 'os': 1, 'security': 2}

tmp_sorted2 = sorted(tmp.items(), key=lambda x: x[1])
print(tmp_sorted2)
```
```
[('os', 1), ('security', 2), ('network', 3), ('database', 5)]
```


# Reference
- https://excelsior-cjh.tistory.com/100
