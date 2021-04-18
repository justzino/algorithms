# Quick Sort1

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


# 일반적인(전통적인) 방법의 quick sort
def quick_sort(array, start, end):
    if start >= end:        # 원소가 1개인 경우 종료
        return
    pivot = start           # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗 swap
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았으면 작은 데이터와 큰 데이터 swap
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정력 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
```

# Quick Sort2

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


# 파이썬의 장점을 살린 quick sort
def quick_sort(array):
    # 리스트가 하나 이하의 원소를 담고 있으면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]    # 피벗은 첫 번째 우너소
    tail = array[1:]    # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]         # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]         # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
```

# Count Sort

```python
# 계수 정렬
# 데이터의 크기가 한정되어 있고, 값이 많이 중복되어 있을수록 유리하다.
# 가장 큰 데이터와 가장작은 데이터의 차이가 1,000,000을 넘지 않을때 효과적이다.
# O(N + K), N: 데이터의 개수, K: 데이터 중 최대값의 크기

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1    # 각 데이터에 해당하는 인덱스의 값 증가

# 리스트에 기록된 정렬 정보 확인
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')   # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

```

# 파이썬 정렬 라이브러리

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)
```
`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)
```
`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`

## key에 함수 사용
```python
def setting(data):
    return data[1]


array = [("바나나", 2), ("사과", 5), ("당근", 3)]

result = sorted(array, key=setting)
print(result)
```
`[('바나나', 2), ('당근', 3), ('사과', 5)]`

## key에 lambda 사용
```python
array = [("바나나", 2), ("사과", 5), ("당근", 3)]

# key 를 이용하여 점수를 기준으로 정렬
array = sorted(array, key=lambda fruit: fruit[1])
print(array)
```
`[('바나나', 2), ('당근', 3), ('사과', 5)]`
