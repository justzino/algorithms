# 떡의 양이 충분한 경우 고려 안되었으므로 틀린 풀이
# 재귀로 처리하기 쉽지 않음
# 파라메트릭 서치 문제 유형의 경우 반복문을 활용

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    result = 0

    for x in array:
        if x > mid:
            result += x - mid
        else:
            continue

    if result == target:
        return mid

    if result < target:
        return binary_search(array, target, start, mid - 1)

    else:
        return binary_search(array, target, mid + 1, end)


n, m = map(int, input().split())
array = list(map(int, input().split()))

h = binary_search(array, m, 0, max(array))
print(h)
