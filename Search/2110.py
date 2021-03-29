# 문제 풀이 핵심 아이디어
# 집의 개수 N은 최대 200,000이며 집의 좌표 X는 최대 1,000,000,000 이다. -> 값이 너무 크므로 이진탐색 고려
# 이진 탐색을 이용하여 O(N * logX)에 문제를 해결할 수 있다.
# 가장 인접한 두 공유기 사이의 최대 Gap을 이진 탐색으로 찾는다.
# 반복적으로 Gap 을 설정하며, C 개 이상의 공유기를 설치할 수 있는 경우를 찾는다. (N=5, C=3)
# 최대 Gap=8, 최소 Gap=1 -> Gap=mid=4

n, c = list(map(int, input().split(' ')))

array = []
for _ in range(n):
    array.append(int(input()))
array = sorted(array)

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2    # mid는 Gap을 의미합니다.
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:      # C개 이상의 공유기를 설치할 수 있는 경우
        start = mid + 1
        result = mid
    else:       # C개 이상의 공유기를 설치할 수 없는 경우
        end = mid - 1

print(result)