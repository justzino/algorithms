n = int(input())
parts = list(map(int, input().split()))
m = int(input())
orders = list(map(int, input().split()))

parts.sort()


def binary_search(array, target, start, end):
    # 해당 부품이 없는 경우 False 반환
    if start > end:
        return False

    # 찾은 경우 True 반환
    mid = (start + end) // 2
    if parts[mid] == target:
        return True
    # 중간점의 값보다 찾고자 하는 갑시 작은 경우 왼쪽 확인
    elif target < parts[mid]:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)


for order in orders:
    if binary_search(parts, order, 0, n-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
